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

    def meiosis( self ):
        arm = []
        for genePair in genes:
            gene = choice( genePair )
            arm.append( gene.copy() )
        return arm

    def recombine( self, arm1, arm2 ):
        self.genes.append( [arm1, arm2] )

    # Create a fusion with another chromosome
    # @param self
    # @param Chromosome chromosome
    # @return Chromosome
    def fusion( self, chromosome ):
        newTraits = []

        for trait in self.traits:
            trait.mutate( )
            newTraits.append( trait )

        for trait in gene.traits:
            trait.mutate( )
            newTraits.append( trait )

        return Gene( newTraits )

    # Create fission of the chromosome into 2 chromosomes
    # @param self
    # @return tuple Chromosome, Chromosome
    def fission( self ):
        oldTraits = []
        newTraits = []
        lenTraits = len(self.traits)

        for i, trait in enumerate(self.traits):
            trait.mutate( )
            r = randint(0,1)
            if r == 0 or (i == lentraits and len(newTraits) == 0):
                newTraits.append( trait )
            else:
                oldTraits.append( trait )

        return Gene( oldTraits), Gene( newTraits )