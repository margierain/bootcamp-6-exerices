import unittest

import skeleton

class MethodTests(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEqual(4, skeleton.add_two_numbers(2,2))




if __name__ =='__main__':
    unittest.main()        
