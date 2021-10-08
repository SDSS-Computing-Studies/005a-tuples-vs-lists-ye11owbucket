#! python3
"""
Sort the given list by numerical value
Find the smallest and the largest value and display them:

inputs:
none

outputs:
string containing the 2 numbers:

example:
The smallest number is 3 and the largest number is 9
"""

List = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]
List.sort()
least = str(List.pop(0))
most = str(List.pop(10))
print("The smallest number is " + least +" and the largest number is " +most)
