"""
You are choreographing a circus show with various animals. For one act, you are 
given two kangaroos on a number line ready to jump in the positive 
direction (i.e, toward positive infinity).

 - The first kangaroo starts at location x1 and moves at a rate of v1 meters 
 per jump.
 - The second kangaroo starts at location x2 and moves at a rate of v2
    meters per jump.

You have to figure out a way to get both kangaroos at the same location 
at the same time as part of the show. If it is possible, return YES, 
otherwise return NO. 

kangaroo has the following parameter(s):

    int x1, int v1: starting position and jump distance for kangaroo 1
    int x2, int v2: starting position and jump distance for kangaroo 2


"""


def main():
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    kangaroo(x1, v1, x2, v2)


def kangaroo(x1, v1, x2, v2):
    position_1 = x1
    position_2 = x2

    position_1 += v1
    position_2 += v2

    print(position_1)
    print(position_2)


if __name__ == "__main__":
    main()
