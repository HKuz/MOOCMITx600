#!/usr/local/bin/python3

def main():
    test_sum_digits = False
    test_max_val = False
    test_cipher = False
    test_bag_class_1 = False
    test_bag_class_2 = False
    test_bag_class_3 = False
    test_tent_class = True

    # Problem 3
    if test_sum_digits:
        print('\n===== Testing Sum Digits Problem =====\n')
        suite_1 = ['', 'abc', 'a;35d4', 'A4BN,8tja.|+52']
        results_1 = [False, False, 12, 19]
        for i, item in enumerate(suite_1):
            try:
                test = sum_digits(item)
                if test == results_1[i]:
                    print('PASSED: sum_digits({}) returned {}'.format(item, test))
                else:
                    print('FAILED: sum_digits({}) returned {}, should have returned {}'.format(item, test, results_1[i]))
            except ValueError:
                print('PASSED ValueError test')

    # Problem 4
    if test_max_val:
        print('\n===== Testing Max Val Problem =====\n')
        suite_2 = [(5, (1,2), [[1],[2]]), (5, (1,2), [[1],[9]]), [1, 2, 3]]
        results_2 = [5, 9, 3]
        for i, item in enumerate(suite_2):
            test = max_val(item)
            if test == results_2[i]:
                print('PASSED: max_val({}) returned {}'.format(item, test))
            else:
                print('FAILED: max_val({}) returned {}, should have returned {}'.format(item, test, results_2[i]))

    # Problem 5
    if test_cipher:
        print('\n===== Testing Cipher Problem =====\n')
        suite_3 = [["abcd", "dcba", "dab"]]
        result_dict = [{'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}]
        result_decoded = ['adc']
        for i, item in enumerate(suite_3):
            d, decoded = cipher(item[0], item[1], item[2])
            if d == result_dict[i] and decoded == result_decoded[i]:
                print('PASSED: cipher({}, {}, {}) returned {} and {}'.format(item[0], item[1], item[2], d, decoded))
            else:
                print('FAILED: cipher({}, {}, {}) returned {} and {}, should have returned {} and {}'.format(item[0], item[1], item[2], d, decoded, result_dict[i], result_decoded[i]))

    # Problem 6
    if test_bag_class_1:
        print('\n===== Testing Bag Class Problem 1 =====\n')
        d1 = Bag()
        d1.insert(4)
        d1.insert(4)
        print(d1)
        print('Should have printed: 4:2')
        d1.remove(2)
        print(d1)
        print('Should have printed: 4:2')
        print('------------------------------')

        d1 = Bag()
        d1.insert(4)
        d1.insert(4)
        d1.insert(4)
        print(d1.count(2))
        print('Should have printed: 0')
        print(d1.count(4))
        print('Should have printed: 3')

    if test_bag_class_2:
        print('\n===== Testing Bag Class Problem 2 =====\n')
        a = Bag()
        a.insert(4)
        a.insert(3)
        b = Bag()
        b.insert(4)
        print(a+b)
        print('Should have printed: \n3:1\n4:2')

    if test_bag_class_3:
        print('\n===== Testing Bag Class Problem 3 =====\n')
        d1 = ASet()
        d1.insert(4)
        d1.insert(4)

        d1.remove(2)
        print(d1)
        print('Should have printed: 4:2')

        d1.remove(4)
        print(d1)
        print('Should print nothing')

        d1 = ASet()
        d1.insert(4)
        print(d1.is_in(4))
        print('Should have printed True')
        d1.insert(5)
        print(d1.is_in(5))
        print('Should have printed True')
        d1.remove(5)
        print(d1.is_in(5))
        print('Should have printed False')

    # Problem 7
    if test_tent_class:
        c = MITCampus(Location(1,2))
        print(c.add_tent(Location(2,3)))
        print('Should have printed True')
        print(c.add_tent(Location(1,2)))
        print('Should have printed True')
        print(c.add_tent(Location(0,0)))
        print('Should have printed False')
        print(c.add_tent(Location(2,3)))
        print('Should have printed False')
        print(c.get_tents())
        print("Should have printed ['<0,0>', '<1,2>', '<2,3>']")
        c.remove_tent(Location(0,0))
        print(c.get_tents())
        print("Should have printed ['<1,2>', '<2,3>']")


# Problem 3
def sum_digits(s):
    '''
    Assumes s is a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception.
    '''
    import string
    if len(s) < 1:
        raise ValueError

    digits = string.digits

    dig_only = [int(num) for num in s if num in digits]
    if len(dig_only) < 1:
        raise ValueError
    else:
        return sum(dig_only)


# Problem 4
def max_val(t):
    '''
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t
    '''
    # Helper function to squash the nested lists or tuples
    def squash(seq):
        '''
        Recursively flattens nested lists or tuples in seq
        Assumes seq is not empty
        Returns a list of the items
        '''
        if len(seq) < 1:
            return seq
        elif isinstance(seq[0], list) or isinstance(seq[0], tuple):
            return list(squash(seq[0])) + list(squash(seq[1:]))
        else:
            return list(seq[:1]) + list(squash(seq[1:]))

    squashed = squash(t)
    # print(squashed)
    return max(squashed)


# Problem 5
def cipher(map_from, map_to, code):
    '''
    map_from, map_to: strings where each contain
                          N unique lowercase letters.
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where
        each key is a letter in map_from at index i and the corresponding
    value is the letter in map_to at index i.
    decoded is a string that contains the decoded version
        of code using the key_code mapping.
    '''
    result_dict = {k: v for k, v in zip(map_from, map_to)}
    coded = ''.join([result_dict[s] for s in code])

    return result_dict, coded


# Problem 6
class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        return self.vals.get(e, 0)

    def __add__(self, other):
        new_bag = Bag()
        # Find union of two bags
        new_vals = dict(self.vals)
        for k in other.vals:
            if k in new_vals:
                new_vals[k] += other.vals[k]
            else:
                new_vals[k] = other.vals[k]
        # Insert keys into the new bag
        for k, v in new_vals.items():
            for i in range(v):
                new_bag.insert(k)

        return new_bag


class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            del self.vals[e]
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals


# Problem 7
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        # List of Location objects for all tents on campus
        self.tents = []
        self.tents.append(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        for t in self.tents:
            temp_dist = t.dist_from(new_tent_loc)
            if temp_dist < 0.5:
                return False
        self.tents.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc not in self.tents:
            raise ValueError
        for t in self.tents:
            if tent_loc == t:
                self.tents.remove(t)

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        # Your code here
        return [str(t) for t in sorted(self.tents, key=lambda item: item.x)]


if __name__ == '__main__':
    main()
