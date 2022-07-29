"""
Staircase detail

This is a staircase of size n = 4:

   #
  ##
 ###
####

Its base and height are both equal to. It is drawn using 
# symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n. 
"""


def main():
    staircase(4)


def staircase(n):

    for x in range(1, n + 1):
        y = "#"
        result = y * x
        # >{n} this will make the last item to don't have spaces
        print(f"{result: >{n}}")


if __name__ == "__main__":
    main()
