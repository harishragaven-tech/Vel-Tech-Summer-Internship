def sort_numbers(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return even, odd

numbers = [16, 5, 8, 25, 14, 7, 18, 21, 10, 3]

even, odd = sort_numbers(numbers)

print("Even Numbers:", even)
print("Odd Numbers:", odd)