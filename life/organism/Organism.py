# -------- Organism.py --------
# Generic organism model.
# 
# An organism is built from 1 or more components. A component can be internal
# or external and can perform functions. For example a 'joint' can enable
# rotation around an axis.
# --------

# General imports

# Panda3D imports

# Game imports

# -------- Organism --------
class Organism( object ):
    chromosomes = []
    components = []
    
    # Init
    # @param self
    # @return void
    def __init__( self ):
        pass

    # Get the genotype of the organism
    # @param self
    # @return list
    def genotype( self ):
        return self.genes

    # Set the genotype of the organism
    # @param self
    # @param list genotype
    # @return void
    def setGenotype( self, genotype ):
        pass

    def addComponent( self, component, parent = None ):
        pass

    # Spawn a child organism
    # @param self
    # @return
    def spawn( self, partner = None ):
        organism = Organism( )

        # Sexual reproduction
        if partner:
            for i, c in enumerate( self.chromosomes ):
                chromosome = Chromsome( )
                chromosome.recombine( c.meiosis(mutate=True), partner.chromosomes[i].meiosis(mutate=True) )
                organism.chromosomes.append( chromosome )

        # Asexual reproduction
        else:
            for c in self.chromosomes:
                chromosome = Chromosome( )
                chromosome.recombine( c.meiosis(), c.meiosis() )
                organism.chromosomes.append( chromosome )

        return organism