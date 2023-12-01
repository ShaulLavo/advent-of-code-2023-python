

# 1
with open("input", "r") as file:
    total = 0

    for line in file:
        digits = [char for char in line if char.isdigit()]

        if digits:
            total += int(digits[0] + digits[-1])

import timeit
# 2


def replace_spelled_numbers(line, numbers_spelled_out):
    for i, number in enumerate(numbers_spelled_out):
        if number in line:
            line = line.replace(number, number[0] + str(i) + number[-1])
    return line


def process_file():
    with open("input", "r") as file:
        total = 0
        numbers_spelled_out = ["zero", "one", "two", "three",
                               "four", "five", "six", "seven", "eight", "nine"]

        for line in file:
            line = replace_spelled_numbers(line, numbers_spelled_out)

            digits = [char for char in line if char.isdigit()]
            if digits:
                total += int(digits[0] + digits[-1])

        print(total)


# Measure the execution time
execution_time = timeit.timeit(
    "process_file()", setup="from __main__ import process_file", number=1)

print(f"Execution time: {execution_time} seconds")
