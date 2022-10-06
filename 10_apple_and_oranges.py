# Complete the 'countApplesAndOranges' function below.
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
# countApplesAndOranges has the following parameter(s):
#     s: integer, starting point of Sam's house location.
#     t: integer, ending location of Sam's house location.
#     a: integer, location of the Apple tree.
#     b: integer, location of the Orange tree.
#     apples: integer array, distances at which each apple falls from the tree.
#     oranges: integer array, distances at which each orange falls from the tree.

def main():

    s = 7
    t = 11
    a = 5
    b = 15

    apples = [-2, 2, 1]
    oranges = [5, -6]
    countApplesAndOranges(s, t, a, b, apples, oranges)


def countApplesAndOranges(s, t, a, b, apples, oranges):
    '''
    s = starting point of the range
    t = end point of the range
    a = position of the apples tree (first)
    b = position of the oranges tree (after the range)
    apples = distance of the apples fell
    oranges = distance the oranges fell

    '''
    total_apples = 0
    for apple in apples:
        sum = a + (apple)
        if sum >= s and sum <= t:
            total_apples += 1

    total_oranges = 0
    for orange in oranges:
        sum2 = b + (orange)
        if sum2 >= s and sum2 <= t:
            total_oranges += 1

    result = print(f"{total_apples}\n{total_oranges}")

    return result


if __name__ == "__main__":
    main()
