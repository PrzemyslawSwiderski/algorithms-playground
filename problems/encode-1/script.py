#!/bin/python3

if __name__ == '__main__':

    test_input = "aaabbccca"  # expected out -> 3a2b3c1a

    output = ""
    current_elem = test_input[0]
    counter = 1
    i = 1
    while i < len(test_input):
        if current_elem != test_input[i]:
            output += str(counter)
            output += current_elem
            current_elem = test_input[i]
            counter = 1
        else:
            counter += 1
        i += 1

    output += str(counter)
    output += current_elem
    print(output)
