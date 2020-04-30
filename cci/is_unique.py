import unittest

def is_unique_array(s):
    ''' Determine if a string has all unique characters.
        - Uses an array to keep track of already
            seen characters
        - O(n) runtime
        - O(1) extra space requirements
    '''
    # If there are more characters in the string than
    # there are characters in ASCII, they can not be unique
    # -- We use 256 for the extended ASCII
    if len(s) > 256:
        return False
    # Use an array to check for duplicate characters
    a = [False]*256
    for char in s:
        index = ord(char)
        if a[index]:
            return False
        else:
            a[index] = True
    return True

def is_unique_bit_vector(s):
    ''' Determine if a string has all unique characters.
        - Uses a bit vector bv to keep track of already
            seen characters
        - Using a bit vector reduces space usage by a factor of 8.
        - O(n) runtime
        - O(1) extra space requirements
    '''
    # Use a bitvector to check for duplicate characters
    bv = 0
    for char in s:
        index = ord(char)
        if ((bv >> index) & 1):
            return False
        else:
            bv |= (1 << index)
    return True

def is_unique_no_extra_ds(s):
    ''' Determine if a string has all unique charactres
        without using additional datastructures.

        Note: This does extra space because sorted() is based
        on mergesort.
    '''
    s = sorted(s)
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
    return True

class IsUniqueTest(unittest.TestCase):
    
    def setUp(self):
        self.empty_string = ''
        self.single_letter_string = '5'
        self.is_unique_string = 'kasenbqp391'
        self.not_unique_string = 'kasdfkesa234sdsf'
        self.double_letter = 'dd'

        self.methods = [is_unique_array, is_unique_bit_vector, is_unique_no_extra_ds]
    
    def run_tests_on_fcn(self, fcn):
        self.assertEqual(fcn(self.empty_string), True)
        self.assertTrue(fcn(self.single_letter_string))
        self.assertTrue(fcn(self.is_unique_string))
        self.assertFalse(fcn(self.not_unique_string))
        self.assertFalse(fcn(self.double_letter))
        

    def test_is_unique_array(self):
        self.run_tests_on_fcn(is_unique_array)

    def test_is_unique_bit_vector(self):
        self.run_tests_on_fcn(is_unique_bit_vector)

    def test_is_unique_no_extra_ds(self):
        self.run_tests_on_fcn(is_unique_no_extra_ds)

if __name__ == '__main__':
    unittest.main()