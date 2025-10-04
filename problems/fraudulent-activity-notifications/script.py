#!/bin/python3

import bisect


# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true
# Complete the 'activity_notifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def activity_notifications(expenditure, d):
    notifs_count = 0
    # Initialize sorted trailing window
    trailing = sorted(expenditure[:d])

    for today in range(d, len(expenditure)):
        # Get median from sorted trailing list
        if d % 2 == 1:
            median = trailing[d // 2]
        else:
            median = (trailing[d // 2] + trailing[d // 2 - 1]) / 2

        today_value = expenditure[today]
        if today_value >= 2 * median:
            notifs_count += 1

        # Slide the window
        # Remove the element going out of the window
        old_value = expenditure[today - d]
        del trailing[bisect.bisect_left(trailing, old_value)]

        # Insert the new value to maintain sorted order
        bisect.insort(trailing, today_value)

    return notifs_count

def activity_notifications_2(expenditure, d):
    counts = [0] * 200

    for x in expenditure[:d]:
        counts[x] += 1

    def median():
        total_left = 0
        for l in range(200):
            total_left += counts[l]
            if total_left > d - total_left: # same as total_left > d / 2
                return l
            elif total_left == d - total_left: # same as total_left == d / 2
                r = l + 1
                # skip all 0 to find the nearest value
                while not counts[r]:
                    r += 1
                return (l + r) / 2.
        return None

    res = 0
    for i in range(d, len(expenditure)):
        res += (expenditure[i] >= median() * 2)
        counts[expenditure[i-d]] -= 1
        counts[expenditure[i]] += 1

    return res

if __name__ == '__main__':
    d = 4
    # d = 3
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    # expenditure = [10, 20, 30, 40, 50]

    # result = activity_notifications(expenditure, d)
    result = activity_notifications_2(expenditure, d)
    print(f"{result=}")
