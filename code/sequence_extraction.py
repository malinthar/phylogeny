import pandas as pd
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


# read proteins table excel file. Provide he correct location
xls = pd.ExcelFile('./../data/protein_tables.xlsx')

# The list of proteins that we consider
protein_set = ["cytochrome d ubiquinol oxidase subunit II", "LysR family transcriptional regulator",
               "helix-turn-helix domain-containing protein", "efflux transporter outer membrane subunit"]

# The list of information needed to extract gene seqeunce of each protein in each common speicies .
all_species = []

protein1 = []
protein2 = []
protein3 = []
protein4 = []

# accession numbers of each common species.
acc_numbers = []

# find the start and stop positions of genes that result in each of the above 4 proteins in each species.


def findStartAndStop():
    for i in range(0, 21):  # since we have all 21 species as common species.
        sheet = xls.parse(i)
        name = sheet["Replicon Accession"][0]
        acc_numbers.append(name)
        species = {"species_accession": name, "sequence_ids": {}}
        for protein in protein_set:
            protein_start_end = {}
            index = sheet["Protein name"].str.contains(protein).idxmax()
            protein_start_end["start"] = sheet.iloc[index]["Start"]
            protein_start_end["stop"] = sheet.iloc[index]["Stop"]
            species["sequence_ids"][protein] = protein_start_end
        all_species.append(species)


sequences: []


def extractGeneSequences():
    for species in all_species:
        fileName = "./../data/genomes/"+species["species_accession"]+".fasta"
        with open(fileName) as handle:
            for record in SeqIO.parse(handle, "fasta"):
                for i in range(0, 4):
                    start = species["sequence_ids"][protein_set[i]]["start"]
                    stop = species["sequence_ids"][protein_set[i]]["stop"]
                    temp = [record.id, record.seq[start:stop]]
                    if(i == 0):
                        protein1.append(temp)
                    elif(i == 1):
                        protein2.append(temp)
                    elif(i == 2):
                        protein3.append(temp)
                    else:
                        protein4.append(temp)


def writeSequences():
    for i in range(0, 4):
        if(i == 0):
            seqlist = protein1
            fileName = "protein1.fasta"
        elif(i == 2):
            seqlist = protein2
            fileName = "protein2.fasta"
        elif(i == 3):
            seqlist = protein3
            fileName = "protein3.fasta"
        else:
            seqlist = protein4
            fileName = "protein4.fasta"

        sequences = []
        for seq in seqlist:
            record = SeqRecord(seq[1], id=seq[0], name=seq[0],
                               description=protein_set[i]+" protein of "+seq[0])
            sequences.append(record)
        SeqIO.write(sequences, "./../data/output/"+fileName, "fasta")


def main():
    findStartAndStop()
    extractGeneSequences()
    writeSequences()
    print("Successfully extracted sequeces and saved in /output directory")

if __name__ == "__main__":
    main()
