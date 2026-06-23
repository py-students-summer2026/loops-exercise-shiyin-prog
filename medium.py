def one(numbers):
    print("\nmedium.one:")

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    print("\t", f"largest number = {largest}")


def two(numbers):
    print("\nmedium.two:")

    total = 0
    i = 0

    while i < len(numbers):
        total += numbers[i]
        i += 1

    average = total / len(numbers)
    print("\t", f"average = {average}")


def three(text):
    print("\nmedium.three:")

    cleaned = text.lower()
    reversed_text = ""

    for character in cleaned:
        reversed_text = character + reversed_text

    if cleaned == reversed_text:
        print("\t", f'"{text}" is a palindrome')
    else:
        print("\t", f'"{text}" is not a palindrome')


def four(n):
    print("\nmedium.four:")

    count = 0
    value = 2

    while count < n:
        print("\t", value)
        value *= 2
        count += 1


def five(numbers):
    print("\nmedium.five:")

    largest = numbers[0]
    second_largest = numbers[0]

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
        elif number > second_largest and number != largest:
            second_largest = number

    print("\t", f"second largest = {second_largest}")


def six(number):
    print("\nmedium.six:")

    product = 1
    i = number

    while i > 0:
        product *= i
        i -= 1

    print("\t", f"{number} factorial = {product}")


def seven(number):
    print("\nmedium.seven:")

    is_square = False

    for i in range(1, number + 1):
        if i * i == number:
            is_square = True

    if is_square:
        print("\t", f"{number} is a perfect square")
    else:
        print("\t", f"{number} is not a perfect square")


def eight():
    print("\nmedium.eight:")

    total = 0
    number = 2

    while number <= 100:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            total += number

        number += 1

    print("\t", f"sum of primes from 1 to 100 = {total}")


def nine(sentence):
    print("\nmedium.nine:")

    words = sentence.split()
    count = 0

    for word in words:
        count += 1

    print("\t", f"number of words = {count}")


def ten(list_one, list_two):
    print("\nmedium.ten:")

    common = []
    i = 0

    while i < len(list_one):
        if list_one[i] in list_two and list_one[i] not in common:
            common.append(list_one[i])
        i += 1

    print("\t", f"common elements = {common}")