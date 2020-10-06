import io
import schools
import unittest


class TestSchoolClass(unittest.TestCase):

    def test_make_groups_single_student(self):
        """Test make_groups with single student."""
        school_class = schools.SchoolClass.from_list([
            (1, 0)
        ])
        actual = school_class.make_groups()
        expected = [{1}, set()]
        self.assertCountEqual(expected, actual)

    def test_make_groups_linear_friendships(self):
        """Test make_groups with linear friendships.

        Friendships:
        1 - 2 - 3 - 4
        """
        school_class = schools.SchoolClass.from_list([
            (4, 3),
            (1, 2),
            (3, 4),
            (2, 3)
        ])
        actual = school_class.make_groups()
        expected = [{1, 3}, {2, 4}]
        self.assertCountEqual(expected, actual)

    def test_make_groups_tree_friendships(self):
        r"""Test make_groups with tree-shaped friendships.

        Friendships:
            _ 1 _
           /     \
          2       3
         / \     / \
        4   5   6   7
        """
        school_class = schools.SchoolClass.from_list([
            (7, 6),
            (1, 2),
            (1, 3),
            (2, 4),
            (2, 5),
            (3, 6),
            (3, 7)
        ])
        actual = school_class.make_groups()
        expected = [{1, 4, 5, 6, 7}, {2, 3}]
        self.assertCountEqual(expected, actual)

    def test_make_groups_disconnected_friendships(self):
        """Test make_groups with two disconnected groups of friends.

        Friendships:
        1 - 2    5 - 6
        |   |
        3 - 4
        """
        school_class = schools.SchoolClass.from_list([
            (6, 5),
            (1, 2),
            (5, 6),
            (1, 3),
            (2, 4),
            (3, 4)
        ])
        actual = school_class.make_groups()
        expected = [{1, 4, 5}, {2, 3, 6}]
        self.assertCountEqual(expected, actual)

    def test_make_groups_all_friends(self):
        r"""Test make_groups where every students are friends.

        Friendships:
          1
         / \
        2 - 3 
        """
        school_class = schools.SchoolClass.from_list([
            (3, 3),
            (1, 2),
            (2, 3),
            (3, 1)
        ])
        self.assertRaises(schools.NoSolutionError, school_class.make_groups)

    def test_make_groups_odd_number_cycle(self):
        r"""Test make_groups with cycle of odd number of students.

        Friendships:
          1
         / \
        2   3
        |   |
        4 - 5 
        """
        school_class = schools.SchoolClass.from_list([
            (5, 5),
            (1, 2),
            (1, 3),
            (2, 4),
            (3, 5),
            (4, 5)
        ])
        self.assertRaises(schools.NoSolutionError, school_class.make_groups)

    def test_print_groups_with_solution(self):
        """Test print_groups with valid solution (linear friendships).

        Friendships:
        1 - 2 - 3 - 4
        """
        school_class = schools.SchoolClass.from_list([
            (4, 3),
            (1, 2),
            (3, 4),
            (2, 3)
        ])
        out = io.StringIO()
        school_class.print_groups(out)
        self.assertEqual(out.getvalue(), '1 1\n2 2\n3 1\n4 2\n')

    def test_print_groups_with_error(self):
        r"""Test print_groups with no valid solution (all friends).

        Friendships:
          1
         / \
        2 - 3 
        """
        school_class = schools.SchoolClass.from_list([
            (3, 3),
            (1, 2),
            (1, 3),
            (2, 3)
        ])
        out = io.StringIO()
        school_class.print_groups(out)
        self.assertEqual(out.getvalue(), '-1\n')


if __name__ == '__main__':
    unittest.main()
