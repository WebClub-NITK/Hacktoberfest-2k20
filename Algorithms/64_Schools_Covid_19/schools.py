"""Solution to Schools During Covid-19 problem."""

import io
import sys
from typing import Iterable, List, Set, Tuple


class NoSolutionError(Exception):
    """Raised when there is no solution."""
    pass


class SchoolClass:
    """School class with number of students and friendships."""

    def __init__(self, num_students: int, friendships: List[Set[int]]):
        self.num_students = num_students
        self.friendships = friendships  # Friends of n are stored in n - 1

    @classmethod
    def from_iter(cls, it: Iterable[Tuple[int, int]]):
        num_students, num_friendships = next(it)
        friendships = [set() for _ in range(num_students)]
        for _ in range(num_friendships):
            student, friend = next(it)
            friendships[student - 1].add(friend)
            friendships[friend - 1].add(student)
        return cls(num_students, friendships)

    @classmethod
    def from_list(cls, l: List[Tuple[int, int]]):
        return SchoolClass.from_iter(iter(l))

    def make_groups(self) -> Tuple[Set[int], Set[int]]:
        """Make two groups with no friendship in each group.

        Returns a valid solution if there is any, otherwise raise
        NoSolutionError.
        """
        groups = [set(), set()]  # Group n is stored in index n - 1
        unvisited = set(range(1, self.num_students + 1))
        while unvisited:
            to_visit = [(unvisited.pop(), 0)]
            while to_visit:
                student, group = to_visit.pop()
                groups[group].add(student)
                other_group = group ^ 1  # Toggle index between 0 and 1
                for friend in self.friendships[student - 1]:
                    if friend in groups[group]:
                        raise NoSolutionError
                    if friend in unvisited:
                        to_visit.append((friend, other_group))
                        unvisited.remove(friend)
        return groups

    def print_groups(self, out: io.TextIOBase = sys.stdout) -> None:
        """Make two groups with no friendship in each group and print solution.

        If there is no solution, print -1.
        """
        try:
            groups = self.make_groups()
            for student in range(1, self.num_students + 1):
                if student in groups[0]:
                    group = 1
                elif student in groups[1]:
                    group = 2
                else:
                    raise Exception(
                        f'Student {student} is not listed in any group.')
                out.write(f'{student} {group}\n')
        except NoSolutionError:
            out.write('-1\n')
