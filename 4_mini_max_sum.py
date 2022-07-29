"""
Given five positive integers, find the minimum and maximum 
values that can be calculated by summing exactly four of 
the five integers. Then print the respective minimum and 
maximum values as a single line of two space-separated long integers. 
"""


def main():
    array_1 = [1, 3, 5, 7, 9]
    miniMaxSum(array_1)


def miniMaxSum(arr):
    # 1 - GET THE MIN SUM
    max_num = 0
    min_sum = 0

    array_length = len(arr)
    allowed_items = 5
    if array_length == allowed_items:
        # get the max number for the min sum
        # also use this to get the max number
        # for i in arr:
        #     if i > max_num:
        #         max_num = i
        max_num = max(arr)
        for j in arr:
            if j < max_num:
                min_sum += j

        # 2 - GET THE MAX SUM
        max_sum = 0
        # get the min number of the array
        min_num = min(arr)
        for k in arr:
            if k > min_num:
                max_sum += k

        final = print(f"{min_sum} {max_sum}")
        return final
    else:
        return print("Error")


if __name__ == "__main__":
    main()
