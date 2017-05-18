import unittest

from utils import make_matrix


class UtilsTesting(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_make_matrix(self):
        self.assertEqual(make_matrix(2, 1), [[0], [0]])
