"""
Given a time in 12-hour AM/PM format, convert it to military 
(24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock. 
"""


def main():
    time = "12:00:00AM"
    timeConversion(time)


def timeConversion(s):
    # hour in a 12-hour format
    hour = s[0:2]
    hour = int(hour)

    # am or pm, get the last 2 characters
    am_or_pm = s[-2:]

    # format without the am or pm, remove las 2 characters
    new_format = s[2:-2]

    if am_or_pm == "PM" and hour < 12:
        new_hour = hour + 12
        new_hour = str(new_hour)
    elif am_or_pm == "AM" and hour != 12:
        new_hour = hour
        new_hour = str(new_hour)
    elif am_or_pm == "AM" and hour == 12:
        new_hour = "00"
    final_hour = f"{new_hour}{new_format}"

    return final_hour


if __name__ == "__main__":
    main()
