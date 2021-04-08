import pandas as pd

# include correct file directory here.
# This class prints the relevant species and gene start and stop index information.
xls = pd.ExcelFile('protein_tables.xlsx')

protein_set = ["cytochrome d ubiquinol oxidase subunit II", "LysR family transcriptional regulator",
               "helix-turn-helix domain-containing protein", "efflux transporter outer membrane subunit"]

all_species = []
for i in range(0, 21):
    sheet = xls.parse(i)
    name = sheet["Replicon Accession"][0]
    species = {"species_accession": name, "sequence_ids": {}}
    for protein in protein_set:
        protein_start_end = {}
        index = sheet["Protein name"].str.contains(protein).idxmax()
        protein_start_end["start"] = sheet.iloc[index]["Start"]
        protein_start_end["stop"] = sheet.iloc[index]["Stop"]
        species["sequence_ids"][protein] = protein_start_end
    all_species.append(species)


def printTable(myDict, colList=None):
    for record in myDict:
        print("species:", record["species_accession"], " p1: {", record["sequence_ids"]["cytochrome d ubiquinol oxidase subunit II"]["start"],
              record["sequence_ids"]["cytochrome d ubiquinol oxidase subunit II"]["stop"],
              "} p2: {", record["sequence_ids"]["LysR family transcriptional regulator"]["start"],
              record["sequence_ids"]["LysR family transcriptional regulator"]["stop"],
              " p3: {", record["sequence_ids"]["helix-turn-helix domain-containing protein"]["start"],
              record["sequence_ids"]["helix-turn-helix domain-containing protein"]["stop"],
              "} p4: {", record["sequence_ids"]["efflux transporter outer membrane subunit"]["start"],
              record["sequence_ids"]["efflux transporter outer membrane subunit"]["stop"], "}")


printTable(all_species)
