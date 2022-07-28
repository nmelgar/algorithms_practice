"""Given a square matrix, calculate the absolute difference 
between the sums of its diagonals.
For example, the square matrix
is shown below:

1 2 3
4 5 6
9 8 9  

left-to-right 1 + 5 + 9 = 15
right-to-left 3 + 5 + 9 = 17
absolute difference is |15-17| -2
"""


def main():
    # array_1 = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    array_1 = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]

    result = diagonalDifference(array_1)
    print(result)


def diagonalDifference(arr):
    # left to right sum
    counter_1 = 0
    left_to_right = 0
    # x is to iterate the row by row
    for x in arr:
        # y is for the values present in each row
        for y in x:
            if counter_1 < len(arr):
                number = arr[counter_1][counter_1]
                # print(number)
                counter_1 += 1
                left_to_right += number

    # right to left sum
    counter_2 = 0
    final_index = -1
    right_to_left = 0
    for a in arr:
        for b in a:
            if counter_2 < len(arr):
                number = arr[counter_2][final_index]
                # print(number)
                counter_2 += 1
                final_index -= 1
                right_to_left += number

    # get the absolute value
    difference = (left_to_right) - (right_to_left)
    total = abs(difference)
    return total


if __name__ == "__main__":
    main()
