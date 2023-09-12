import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
<<<<<<< HEAD
        name="Ekta"
        upper_name=to_upper(name)
        self.assertEqual(upper_name,"ekta")


if __name__=='__main__':
    unittest.main()
=======
        name="Prachita"
        upper_name=to_upper(name)
        self.assertEqual(upper_name,"Prachita")

    if __name__=='__main__':
        unittest.main()
>>>>>>> 18ec47b4ea95729167660504834ef664b63c56ab
