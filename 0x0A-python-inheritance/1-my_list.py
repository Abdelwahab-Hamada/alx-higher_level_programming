#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """MyList props"""

    def print_sorted(self):
        """Print list"""

        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
