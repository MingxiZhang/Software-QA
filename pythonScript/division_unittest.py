import unittest
from division import local_division

class DivisionTest(unittest.TestCase):
    def test1(self):
       
        division_result = local_division(5,2)
        self.assertEqual(division_result,2)

    def test2(self):
        
        division_result = local_division(0,5)
        self.assertEqual(division_result,0)


if __name__ == '__main__':
    unittest.main()