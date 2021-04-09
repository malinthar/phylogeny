import pandas as pd
xls = pd.ExcelFile('./../data/protein_tables.xlsx')

protein_set = ["cytochrome d ubiquinol oxidase subunit II", "LysR family transcriptionalregulator",
               "helix-turn-helix domain-containing protein", "efflux transporterouter membrane subunit"]

bacteria_list = []
def findNames():
    for i in range (0,21):
        sheet = xls.parse(i)
        name = sheet["Replicon Accession"][0]
        proteins = list(sheet["Protein name"])
        count = 0
        for protein in protein_set:
            if(protein in p for p in proteins):
                count = count +1
        if(count == 4):
            bacteria_list.append(name)

def writeToFile():
    findNames()
    file = open("./../data/common_bacteria_file.txt","w")
    for name in bacteria_list:
        file.write(name+"\n")
    file.close()

def main():
    writeToFile()

if __name__=="__main__":
    main()