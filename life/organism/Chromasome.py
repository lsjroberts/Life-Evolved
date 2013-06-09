# -------- Chromosome.py --------
# A collection of genes
# --------

# General imports
from random import choice

# Panda3D imports

# Game imports

# -------- Chromosome --------
class Chromosome( ):
    
    # Init
    # @param self
    # @return void
    def __init__( self, genes = None ):
        if genes is None: genes = []
        self.genes = genes

    def meiosis( self, mutate = False ):
        arm = []
        for genePair in self.genes:
            gene = choice( genePair )
            arm.append( gene.copy(mutate) )
        return arm

    def recombine( self, arm1, arm2 ):
        self.genes.append( [arm1, arm2] )

    # Create a fusion with another chromosome
    # @param self
    # @param Chromosome chromosome
    # @return Chromosome
    def fusion( self, chromosome ):
        return Chromosome( self.genes + chromosome.genes )

    # Create fission of the chromosome into 2 chromosomes
    # @param self
    # @return tuple Chromosome, Chromosome
    def fission( self ):
        genesOne = []
        genesTwo = []
        lenGenes = len(self.genes)

        for i, gene in enumerate(self.genes):
            r = randint(0,1)
            # Ensure genesTwo has at least one gene by checking it's length on the last loop
            if r == 0 or (i == lenGenes and len(genesTwo) == 0):
                genesTwo.append( trait )
            else:
                genesOne.append( trait )

        return Chromosome( genesOne ), Chromosome( genesTwo )