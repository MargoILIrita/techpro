import unittest
import legacycode as l

class MyTestCase(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(l.derivative(0,0), 0)
        self.assertEqual(l.derivative(2,3), -3.5)
        self.assertNotEqual(l.derivative(0,0),1)
        self.assertRaises(ValueError,l.derivative,-1,1)


    def test_third(self):
        self.assertEqual(l.third(0,0,1), 0)
        self.assertEqual(l.third(10,10, 0.1), 7.152476877619735)
        self.assertNotEqual(l.third(0,0,1),2)


    def test_forth(self):
        self.assertEqual(l.forth(0, 0, 1), 0)
        self.assertEqual(l.forth(10,10,0.01), 9.532261307476578)
        self.assertNotEqual(l.third(0, 0, 1), 2)


    def test_thirdfordraw(self):
        a_true = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        b_true = [1, 1.1379846643518519, 0.999087974993131, 0.8414414771230798,
                  0.7135764486360278, 0.6147429353293963, 0.5379273346218882, 0.4771805595790072,
                  0.428225587563995, 0.38807143580082043, 0.35461347565906287]
        a, b = l.thirdfordraw(10, 10)
        self.assertCountEqual(a_true,a)
        self.assertCountEqual(b_true, b)


    def test_forthfordraw(self):
        a_true = [0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
        b_true = [1, 1.1380351524140855, 0.9970844640831762, 0.8405775289935526,
                  0.7134345765667318, 0.6148724618196856, 0.5381323392184878,
                  0.47738876439509, 0.4284135108248589, 0.38823381744055807, 0.35475148037296556]
        a, b = l.forthfordraw(10,10)
        self.assertCountEqual(a_true,a)
        self.assertCountEqual(b_true,b)

if __name__ == '__main__':
    unittest.main()
