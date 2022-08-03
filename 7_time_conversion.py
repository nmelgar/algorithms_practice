"""
Given a time in 12-hour AM/PM format, convert it to military 
(24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 
"""


def main():
    time = "12:00:00PM"
    timeConversion(time)


def timeConversion(s):
    # hour in a 12-hour format
    hour = s[0:2]
    hour = int(hour)

    #am or pm, get the last 2 characters
    format = s[-2:]

    # format without the am or pm, remove las 2 characters
    new_format = s[0:-2]


if __name__ == "__main__":
    main()
