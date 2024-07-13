#!/bin/python3
import os


#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n chapters count
#  2. INTEGER k max problems per pages
#  3. INTEGER_ARRAY arr problems count per chapter
#
# https://www.hackerrank.com/challenges/lisa-workbook

def workbook(n, k, arr):
    pages = []
    special_problems_sum = 0
    for i in range(n):
        chap_problems = arr[i]
        problems_counter = 1
        while problems_counter <= chap_problems:
            if problems_counter + k > chap_problems:
                max_page = chap_problems
            else:
                max_page = problems_counter + k - 1
            pages.append({
                "chapter": i + 1,
                "startPg": problems_counter,
                "endPg": max_page
            })
            problems_counter = problems_counter + k

    for idx, page in enumerate(pages):
        page_num = idx + 1
        # print(f"Page: {page_num}, {page}")
        if page["startPg"] <= page_num <= page["endPg"]:
            special_problems_sum = special_problems_sum + 1

    return special_problems_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
