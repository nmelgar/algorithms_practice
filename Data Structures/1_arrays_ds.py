def main():
    array_1 = [1, 2, 3]

    print(reverseArray(array_1))


def reverseArray(a):
    new_array = list(reversed(a))

    return new_array


if __name__ == "__main__":
    main()
