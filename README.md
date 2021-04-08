## Phylogeny assignemnt 
 steps to reproduce


### Prerequisite: 
- The provided excel file `protein_tables` should be in the root directory.
- The genomes of `common_bacteria_set` should be in the `./sequences/` relative directory. (The genomes have been included in the data folder)
-  python 3
-  Following python libs installed
    - Bio
    - Pandas
    - ete3
    - Matplotlib
- Clustax software

### Step 1: Finding the cpmmon bacteria set (Optional)
execute script [find_common_bacteria](./code/find_common_bacteria.py) 

> Note: We have got all 21 given species as the common bacteria set
)
### Step 2: Extracting gene sequences for each protein in each species (homologous_gene_sequencces)
execute script [sequence_extraction](./sequence_extraction.py)

> Note: Resulting fasta files for each protein is saved in the output folder

### Step 3: Align the files using the Clustalx Software

### Step 4: Construct phylogenetic trees

After creating the alignments in `nexus` format, execute script  [tree_construction](./tree_construction.py) to generate phylogentic trees and calculate RF distance. 

