from ..unrolled_linked_list import UnrolledLinkedList
import unittest


class UnrolledLinkedList_Test(unittest.TestCase):
    """This is an example of a Testing class. You are welcome to make multiple
    classes to organize your code if you would like to, but it is in no way
    required or expected. You'll want to replace this comment with your own.
    """
    def test_default_node_capacity(self):
        """Test that the default node capacity is being set, and is set to 16
        """
        l = UnrolledLinkedList()
        self.assertEqual(l.max_node_capacity, 16)
