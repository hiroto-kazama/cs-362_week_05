import unittest
import calc

def test_inclass_activity_02(self):
    result = in_class_activity_02.add(1,2)
    self.assertEqual(result, 3)

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(7,2), 9)
    
    def test_sub(self):
        self.assertEqual(calc.sub(4,2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2,2), 4)

    def test_div(self):
        self.assertEqual(calc.div(4,2), 2)
        

if __name__ == '__main__':
    unittest.main()