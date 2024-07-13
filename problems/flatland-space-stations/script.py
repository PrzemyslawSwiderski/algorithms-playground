#!/bin/python3
import os


# https://www.hackerrank.com/challenges/flatland-space-stations/problem
#
# Complete the flatlandSpaceStations function below.
def flatland_space_stations(n, c):
    max_dist = 1

    c.sort()

    # all cities have space stations
    if len(c) == n:
        return 0

    # first station dist check
    if c[0] != 0:
        first_stat_dist = c[0]
        if first_stat_dist > max_dist:
            max_dist = first_stat_dist

    # intermediate stations check
    previous_station_dist = 0
    for station in c:
        dist = (station - previous_station_dist) // 2
        if dist > max_dist:
            max_dist = dist
        previous_station_dist = station

    # last station dist check
    if c[-1] != n - 1:
        last_stat_dist = n - 1 - c[-1]
        if last_stat_dist > max_dist:
            max_dist = last_stat_dist

    return max_dist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatland_space_stations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
