import unittest


def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form
            # the conditional statement, although this was
            # not introduced above.
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos


class SmallestPositiveTest(unittest.TestCase):
    def run_test(self, in_list, expected_output):
        self.assertEqual(smallest_positive(in_list), expected_output)

    def test_positive_int(self):
        self.run_test([4, -6, 7, 2, -4, 10], 2)

    def test_positive_float(self):
        self.run_test([.2, 5, 3, -.1, 7, 7, 6], 0.2)

    def test_all_negative(self):
        self.run_test([-6, -9, -7], None)

    def test_empty_list(self):
        self.run_test([], None)


unittest.main()
