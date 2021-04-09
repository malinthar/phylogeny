from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from Bio import Phylo
from Bio import Nexus
import matplotlib
import matplotlib.pyplot as plt
# import dendropy
# from dendropy.calculate import treecompare
from ete3 import Tree
# Before runing this class the sequence files(protein1.fasta, ..) should be aligned using clustalx.Use the output file location in drawTree method

def calDistance():
    t1 = Tree("./../data/trees/protein1.ph")
    t2 = Tree("./../data/trees/protein2.ph")
    t3 = Tree("./../data/trees/protein3.ph")
    t4 = Tree("./../data/trees/protein4.ph")

    rf1 = t1.robinson_foulds(t2)
    rf2 = t1.robinson_foulds(t3)
    rf3 = t1.robinson_foulds(t4)
    rf4 = t2.robinson_foulds(t3)
    rf5 = t2.robinson_foulds(t4)
    rf6 = t3.robinson_foulds(t4)

    print("Tree 1 and tree 2:" + str(rf1[0]))
    print("Tree 1 and tree 3:" + str(rf2[0]))
    print("Tree 1 and tree 4:" + str(rf3[0]))
    print("Tree 2 and tree 3:" + str(rf4[0]))
    print("Tree 2 and tree 4:" + str(rf5[0]))
    print("Tree 3 and tree 4:" + str(rf6[0]))
    
def drawTrees():
    t1 = Phylo.read("./../data/trees/protein1.ph", "newick")
    t2 = Phylo.read("./../data/trees/protein2.ph", "newick")
    t3 = Phylo.read("./../data/trees/protein3.ph", "newick")
    t4 = Phylo.read("./../data/trees/protein4.ph", "newick")

    Phylo.draw(t1)
    Phylo.draw(t2)
    Phylo.draw(t3)
    Phylo.draw(t4)
    
def main():
    calDistance()
    drawTrees()
 
if __name__ == "__main__":
    main()

# def drawTree():
#     # Provide correct file locations.
#     constructor = DistanceTreeConstructor()
#     calculator = DistanceCalculator('identity')
#     trees = []
#     for i in range(1,5):
#         alignment = AlignIO.read(open("./../data/alignments/protein"+str(i)+"/protein"+str(i)+".nxs"), 'nexus')
#         distancem = calculator.get_distance(alignment)
#         upgmatree = constructor.upgma(distancem)
#         upgmatree.rooted = True
#         #print(upgmatree)
#         Phylo.write(upgmatree, "protein"+str(i)+".nwk", "newick")
#         # matplotlib.rc('font', size=5)
#         # fig = plt.figure(figsize=(15, 40), dpi=100)
#         # axes = fig.add_subplot(1, 1, 1)
#         # Phylo.draw(upgmatree, axes=axes)