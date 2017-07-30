#!/usr/local/bin/python3

def main():
    test_sum_digits = False
    test_max_val = False
    test_cipher = True

    if test_sum_digits:
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

    if test_max_val:
        suite_2 = [(5, (1,2), [[1],[2]]), (5, (1,2), [[1],[9]]), [1, 2, 3]]
        results_2 = [5, 9, 3]
        for i, item in enumerate(suite_2):
            test = max_val(item)
            if test == results_2[i]:
                print('PASSED: max_val({}) returned {}'.format(item, test))
            else:
                print('FAILED: max_val({}) returned {}, should have returned {}'.format(item, test, results_2[i]))

    if test_cipher:
        suite_3 = [["abcd", "dcba", "dab"]]
        result_dict = [{'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}]
        result_decoded = ['adc']
        for i, item in enumerate(suite_3):
            d, decoded = cipher(item[0], item[1], item[2])
            if d == result_dict[i] and decoded == result_decoded[i]:
                print('PASSED: cipher({}, {}, {}) returned {} and {}'.format(item[0], item[1], item[2], d, decoded))
            else:
                print('FAILED: cipher({}, {}, {}) returned {} and {}, should have returned {} and {}'.format(item[0], item[1], item[2], d, decoded, result_dict[i], result_decoded[i]))


def sum_digits(s):
    '''
    Problem 3
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

def max_val(t):
    '''
    Problem 4
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


def cipher(map_from, map_to, code):
    '''
    Problem 5
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


if __name__ == '__main__':
    main()
