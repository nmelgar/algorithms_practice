"""
Given an array of integers, find the sum 
of its elements.
It must return the sum of the array elements 
as an integer. simpleArraySum has the following 
parameter(s):
    ar: an array of integers

"""


def main():
    array_1 = [1, 2, 3]
    simpleArraySum(array_1)

# first way
def simpleArraySum(ar):
    suma = sum(ar)
    print(suma)
    return suma

# second way
# def simpleArraySum(ar):
#     total = 0
#     for number in ar:
#         total += number
#     print(total)
#     return total


if __name__ == "__main__":
    main()
