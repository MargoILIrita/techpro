import unittest
import legacycode as l

class MyTestCase(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(l.derivative(0,0), 0)
        self.assertEqual(l.derivative(1,0), 0)
        self.assertEqual(l.derivative(1,1), 0)
        self.assertEqual(l.derivative(2,3), -3.5)
        self.assertNotEqual(l.derivative(0,0),1)


if __name__ == '__main__':
    unittest.main()
