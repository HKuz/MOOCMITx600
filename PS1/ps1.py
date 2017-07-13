#!/usr/bin/Python

'''
Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
'''

s = 'azcbobobegghakl'
num_vowels = 0
for char in s:
    if char in 'aeiou':
        num_vowels += 1
# print('Number of vowels: ' + str(num_vowels))


'''
Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2
'''

s = 'azcbobobegghakl'
word = 'bob'
count = 0
length = len(s)
if length >= 3:
    for i in range(length-2):
        if s[i:i+3] == 'bob':
            count +=1
# print('Number of times bob occurs is: ' + str(count))


'''
Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:

Longest substring in alphabetical order is: abc
'''


s = 'abcdefghijklmnopqrstuvwxyz'
max_subby = s[0]
temp = s[0]
for i in range(1, len(s)):
    if ord(s[i]) >= ord(s[i-1]):
        temp += s[i]
    else:
        # Check if substring is longer than previously found one
        if len(temp) > len(max_subby):
            max_subby = temp
        # Reset temp to current character
        temp = s[i]

if len(temp) > len(max_subby):
    max_subby = temp

print('Longest substring in alphabetical order is: ' + max_subby)
