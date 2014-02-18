import unittest, os, shutil
from pickler import list_pickler, unpickler


class PickleTests(unittest.TestCase):
    def setUp(self):                #setUp gets run before all tests
        self.my_list = [1, 2, 3]    # here its used to create a temp list
        self.path = './pickle_temp' # to hold our pickled list
        os.mkdir(self.path)
        self.file = os.path.join(self.path, 'list.pkl')
        print self.file


    def test_original_and_unpickled_list(self):
        list_pickler(self.file, self.my_list)       
        unpickled_list = unpickler(self.file)
        self.assertEqual(self.my_list, unpickled_list)

    def tearDown(self): # tearDown gets run after the test have been run,
                        # whether they fail or pass. In this case , we're 
                        # using tear down to delete our temp folder and its contents         
                        
        shutil.rmtree(self.path) #shutil.rmtree deletes a directory and all of its contents



