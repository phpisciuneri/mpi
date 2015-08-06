import unittest

from mpi4py import MPI

class TestMpi( unittest.TestCase ):

    def test_rank( self ):
        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()
        self.assertEqual( 0, rank )

