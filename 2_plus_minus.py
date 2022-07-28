"""
Given an array of integers, calculate the ratios of its elements 
that are positive, negative, and zero. Print the decimal 
value of each fraction on a new line with places after the decimal.

"""


def main():
    array_1 = [1, 1, 0, -1, -1]
    plusMinus(array_1)


def plusMinus(arr):
    array_length = len(arr)
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0

    for x in arr:
        if x > 0:
            positive_counter += 1
        elif x < 0:
            negative_counter += 1
        elif x == 0:
            zero_counter += 1

    positive_ratio = positive_counter / array_length
    negative_ratio = negative_counter / array_length
    zero_ratio = zero_counter / array_length

    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == "__main__":
    main()
