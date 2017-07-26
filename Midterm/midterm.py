#!/usr/local/bin/python3

def main():
    test_is_triangular = True
    test_print_without_vowels = True
    test_largest_odd_times = True
    test_dict_invert = True
    test_general_poly = True
    test_is_list_permutation = True

    if test_is_triangular:
        nums = [-1, 0, 0.5, 1, 2, 3, 4, 6, 10, 12, 15]
        res = [False, False, False, True, False, True, False, True, True, False, True]
        for i, k in enumerate(nums):
            test = is_triangular(k)
            if test == res[i]:
                print('PASSED: is_triangular({}) returned {}'.format(k, test))
            else:
                print('FAILED: is_triangular({}) returned {}, should have returned {}'.format(k, test, res[i]))

    if test_print_without_vowels:
        strings = ['This is great!', 'THIs is greAt!']
        res_2 = ['Ths s grt!', 'THs s grt!']
        for i, s in enumerate(strings):
            test_2 = print_without_vowels(s)
            if test_2 == res_2[i]:
                print('PASSED: print_without_vowels({}) returned {}'.format(s, test_2))
            else:
                print('FAILED: print_without_vowels({}) returned {}, should have returned {}'.format(s, test_2, res_2[i]))

    if test_largest_odd_times:
        lists = [[], [2, 2, 4, 4], [3, 9, 5, 3, 5, 3]]
        res_3 = [None, None, 9]
        for i, L in enumerate(lists):
            test_3 = largest_odd_times(L)
            if test_3 == res_3[i]:
                print('PASSED: largest_odd_times({}) returned {}'.format(L, test_3))
            else:
                print('FAILED: largest_odd_times({}) returned {}, should have returned {}'.format(L, test_3, res_3[i]))

    if test_dict_invert:
        dicts = [
            {1:10, 2:20, 3:30},
            {1:10, 2:20, 3:30, 4:30},
            {4:True, 2:True, 0:True}
        ]
        res_4 = [
            {10: [1], 20: [2], 30: [3]},
            {10: [1], 20: [2], 30: [3, 4]},
            {True: [0, 2, 4]}
        ]
        for i, D in enumerate(dicts):
            test_4 = dict_invert(D)
            if test_4 == res_4[i]:
                print('PASSED: dict_invert({}) returned {}'.format(D, test_4))
            else:
                print('FAILED: dict_invert({}) returned {}, should have returned {}'.format(D, test_4, res_4[i]))

    if test_general_poly:
        polys = [
            [[1,2,3,4], 10]
        ]
        res_5 = [
            1234
        ]
        for i, p in enumerate(polys):
            test_5 = general_poly(p[0])(p[1])
            if test_5 == res_5[i]:
                print('PASSED: general_poly({})({}) returned {}'.format(p[0], p[1], test_5))
            else:
                print('FAILED: general_poly({})({}) returned {}, should have returned {}'.format(p[0], p[1], test_5, res_5[i]))

    if test_is_list_permutation:
        perms = [
            [['a', 'a', 'b'], ['a', 'b']],
            [[1, 'b', 1, 'c', 'c', 1], ['c', 1, 'b', 1, 1, 'c']],
            [[], []]
        ]
        res_6 = [
            False,
            (1, 3, type(1)),
            (None, None, None)
        ]
        for i, p in enumerate(perms):
            test_6 = is_list_permutation(p[0], p[1])
            if test_6 == res_6[i]:
                print('PASSED: is_list_permutation({}, {}) returned {}'.format(p[0], p[1], test_6))
            else:
                print('FAILED: is_list_permutation({}, {}) returned {}, should have returned {}'.format(p[0], p[1], test_6, res_6[i]))

    return 0


def is_triangular(k):
    '''
    k, a positive integer
    returns True if k is triangular and False if not
    Triangular number is a sum of sequential integers (1+2+3=6, 6 is triangular)
    '''
    if type(k) is not int or k <= 0:
        return False

    tri = 0
    for n in range(1, k+1):
        tri += n
        if tri == k:
            return True

    return False

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the
    same order they appear in s. Prints this version of s.
    Does not return anything (REMOVE RETURN AND UNCOMMENT PRINT AFTER TESTING)
    '''
    vowels = 'AEIOUaeiou'
    no_vowel_for_you = ''
    for char in s:
        if char not in vowels:
            no_vowel_for_you += char

    # print(no_vowel_for_you)
    return no_vowel_for_you


def largest_odd_times(L):
    '''
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number
    of times in L. If no such element exists, returns None
    '''
    if not L:
        return None

    sorted_L = sorted(L, reverse=True)
    for num in sorted_L:
        count = sorted_L.count(num)
        if count % 2 == 1:
            return num
    return None


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary where keys are d's values, and values
    are a list of all d's keys that mapped to that original value
    '''
    inverted = {}
    for k, v in d.items():
        try:
            inverted[v].append(k)
        except KeyError:
            inverted[v] = [k]

    for k, v in inverted.items():
        inverted[k] = sorted(v)

    return inverted


def general_poly (L):
    '''
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    '''
    global k
    k = len(L) - 1
    def f(x):
        global k
        result = 0
        for n in L:
            result += n * (x ** k)
            k -= 1
        return result

    return f


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
        If they are permutations of each other, returns a
        tuple of 3 items in this order:
        the element occurring most, how many times it occurs, and its type
    '''
    if len(L1) != len(L2):
        return False

    if not L1 and not L2:
        return (None, None, None)

    max_count = 0
    max_item = None
    for item in L1:
        L1_count = L1.count(item)
        if item not in L2 or L2.count(item) != L1_count:
            return False

        if L1_count > max_count:
            max_count = L1_count
            max_item = item

    return (max_item, max_count, type(max_item))


if __name__ == '__main__':
    main()
