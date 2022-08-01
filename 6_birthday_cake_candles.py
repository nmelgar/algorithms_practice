"""
candles = [4,4,1,3]
The maximum height candles are units high. There are 
of them, so return 2.
"""
from operator import countOf


def main():
    candles_array = [4, 4, 1, 3]
    birthdayCakeCandles(candles_array)

# way 1
def birthdayCakeCandles(candles):
    max_candle = max(candles)
    total = 0
    for candle in candles:
        if candle == max_candle:
            total += 1
    print(total)
    return total

# way 2
# def birthdayCakeCandles(candles):
#     max_candle = max(candles)
#     total = 0
#     total = countOf(candles, max_candle)
#     print(total)
#     return total


if __name__ == "__main__":
    main()
