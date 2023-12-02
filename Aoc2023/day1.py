import re

def load_file_into_array(file_path):
    array = []
    with open(file_path, 'r') as file:
        for line in file:
            array.append(line.strip())
    return array

def extract_numbers(array):
    return [[int(num) for num in re.findall(r'\d', string)] for string in array]


def calibrate(array):
    return [int(str(subarray[0]) + str(subarray[-1])) for subarray in array]

array = load_file_into_array('day1.txt')
numbers = extract_numbers(array)
calibrated_numbers = calibrate(numbers)
print(calibrated_numbers)
total = sum(calibrated_numbers)

print(total)


#--------------------------------------------------------------Part2
import sys
file = open('day1.txt').read().strip()

answer = 0

for line in file.split('\n'):
    digits = []
    for i,c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(['one','two', 'three','four','five', 'six', 'seven', 'eight','nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    score = int(digits[0] + digits[-1])
    answer += score

print(answer)

