# Day 1 Python Practice
# Topic: Functions, Lists, Conditions

def find_even_numbers(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def find_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

numbers = [10, 15, 20, 25, 30, 35]
print("Original List:", numbers)

even_numbers = find_even_numbers(numbers)
print("Even Numbers:", even_numbers)

total = find_sum(numbers)
print("Sum:", total)

maximum = find_max(numbers)
print("Maximum:", maximum)

text = "Python Developer"
vowel_count = count_vowels(text)
print("Vowel Count:", vowel_count)
