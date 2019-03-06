# Unit test for boggle

import unittest
import boggle

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid
        """
        
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equal to the *height
        """
        
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid),6)
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates
        inside of the grid
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0,1), grid)
        self.assertIn((1,0), grid)
        self.assertIn((1,1), grid)
        # Assert not in method to check - 2,2 is not in grid
        self.assertNotIn((2,2), grid)
        
        # assertion error as 0 is not equal to 6 - make grid function is empty

# class test_boggle(unittest.TestCase):
#     def test_is_this_thing_on(self):
#         self.assertEqual(1,1)