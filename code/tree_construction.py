from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio import AlignIO
from Bio import Phylo
import dendropy
from dendropy.calculate import treecompare
from ete3 import Tree


# Before runing this class the sequence files(protein1.fasta, ..) should be aligned using clustalx.Use the output file location in drawTree method

def treeConstructor():
    tree1 = Phylo.read("output/protein1.ph", 'newick')
    tree2 = Phylo.read("output/protein1.ph", 'newick')

    # Phylo.draw_ascii(tree)
    tree1.rooted = True
    tree2.rooted = True
    Phylo.compare(tree1, tree2)
    # Phylo.draw(tree)


def drawTree():
    # Provide correct file locations.
    alignment1 = AlignIO.read(open('output/protein1.nxs'), 'nexus')
    alignment2 = AlignIO.read(open('output/protein2.nxs'), 'nexus')
    alignmnet3 = AlignIO.read(open('output/protein3.nxs'), 'nexus')
    alignmnet4 = AlignIO.read(open('output/protein4.nxs'), 'nexus')
    constructor = DistanceTreeConstructor()
    calculator = DistanceCalculator('identity')
    distancem1 = calculator.get_distance(alignment1)
    distancem2 = calculator.get_distance(alignment2)
    upgmatree1 = constructor.upgma(distancem1)
    upgmatree2 = constructor.upgma(distancem2)
    upgmatree1.rooted = True
    upgmatree2.rooted = True
    Phylo.draw(upgmatree1)
    Phylo.draw(upgmatree2)
    #tree1= Tree(upgmatree1)
    # tree2=Tree(upgmatree2)
    #rf, max_rf, common_leaves, parts_t1, parts_t2 = tree1.robinson_foulds(tree2)
    # print(rf)
    # print(upgmatree)


def calculateDistance():
    print("vfjnvfj")


def main():
    drawTree()
    calculateDistance()


if __name__ == "__main__":
    main()
