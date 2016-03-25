import unittest


class MethodTests(unittest.TestCase):

    def test_multiplication_of_two_number(self):
        self.assertEqual(2,2)

    def test_multiplication_of_string_with_number(self):
        self.assertFalse(False)   
        self.assertGreater(9,6)
        self.assertIn("hello", "reyghfgfhello jhgf")

    def test_true(self):
        assertTrue(6 == 6)
        


# import ipdb; ipdb.set_trace()

if __name__ =='__main__':
    unittest.main()        