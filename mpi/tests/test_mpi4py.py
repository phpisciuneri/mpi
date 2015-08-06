import unittest

from mpi4py import MPI
import numpy as np

class TestMpi( unittest.TestCase ):

    def setUp( self ):
        self.comm = MPI.COMM_WORLD
        self.size = self.comm.Get_size()
        self.rank = self.comm.Get_rank()

    def test_rank( self ):
        """Sanity check the value of rank.
        """
        self.assertLess( self.rank, self.size )

    def test_gather( self ):
        """Gather the rank of each process to root (0)
        """
        data = np.array( [-1]*self.size, dtype='i' )
        data = self.comm.gather( self.rank, 0 )
        if self.rank == 0:
            for a, b in zip( data, range( self.size ) ):
                self.assertEqual( a, b )

    def test_allgather( self ):
        """Gather the rank of each process to every process
        """
        data = np.array( [-1]*self.size, dtype='i' )
        data = self.comm.allgather( self.rank )
        for a, b in zip( data, range( self.size ) ):
            self.assertEqual( a, b )

    def test_scatter( self ):
        """
        """
        if self.rank == 0:
            data = np.array( range( self.size ) )
        else:
            data = np.empty( self.size )
        rank = self.comm.scatter( data, 0 )
        self.assertEqual( rank, self.rank )

    def test_Scatter( self ):
        """
        """
        if self.rank == 0:
            data = np.array( range( self.size ), dtype='i' )
        else:
            data = np.empty( self.size )
        rank = np.empty( 1, dtype='i' )
        self.comm.Scatter( [ data, MPI.INT ], [ rank, MPI.INT ], 0 )
        self.assertEqual( rank, self.rank )

    def test_wtime( self ):
        """
        """
        st = MPI.Wtime()
        for i in range( 10 ):
            tick = MPI.Wtick()
        et = MPI.Wtime() - st
        self.assertGreater( et, 0 )


if __name__ == '__main__':
    unittest.main()


        

