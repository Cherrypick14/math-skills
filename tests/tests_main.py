import unittest

from main import calculate_average,calculate_median,calculate_variance,calculate_standard_deviation 

class TestStatisticsFunctions(unittest.TestCase):
     
     def setUp(self):
         self.data = [189, 113, 121, 114, 145, 110]

     def test_calculate_average(self):
         self.assertEqual(round(calculate_average(self.data)), 132)
    
     def test_calculate_median(self):
         self.assertEqual(round(calculate_median(self.data)), 118)
     
     def test_calculate_variance(self):
         self.assertEqual(round(calculate_variance(self.data)), 942)
    
     def test_calculate_standard_deviation(self):
         self.assertEqual(round(calculate_standard_deviation(self.data)), 31)


if __name__ == "__main__":
    unittest.main()