# -------- TestBehavior.py --------

# Imports
from tests.TestCase import TestCase
from life.organism.trait.behavior.Behavior import Behavior

# -------- TestBehavior --------
class TestBehavior( TestCase ):

    def setUp( self ):
        self.factory = Behavior( )
    
    def testEnact( self ):
        self.factory.enact( )