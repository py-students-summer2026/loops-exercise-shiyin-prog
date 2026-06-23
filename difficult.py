def one(number):
    print("\ndifficult.one:")

    print("\t", f"prime factors of {number}: ", end="")

    for factor in range(2, number + 1):
        while number % factor == 0:
            print(factor, end=" ")
            number = number // factor

    print()


def two(n):
    print("\ndifficult.two:")

    first = 0
    second = 1
    count = 1

    while count < n:
        next_number = first + second
        first = second
        second = next_number
        count += 1

    print("\t", f"fibonacci term {n} = {first}")


def three(text):
    print("\ndifficult.three:")

    sorted_text = sorted(text)
    result = ""

    for character in sorted_text:
        result += character

    print("\t", f'anagram sorted = "{result}"')


def four(n):
    print("\ndifficult.four:")

    value = 2
    count = 0

    while count < n:
        print("\t", value)
        value += 2
        count += 1


def five(numbers):
    print("\ndifficult.five:")

    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)

    if length % 2 == 1:
        median = sorted_numbers[length // 2]
    else:
        middle_one = sorted_numbers[length // 2 - 1]
        middle_two = sorted_numbers[length // 2]
        median = (middle_one + middle_two) / 2

    print("\t", f"median = {median}")


def six(number):
    print("\ndifficult.six:")

    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    if total == number:
        print("\t", f"{number} is a perfect number")
    else:
        print("\t", f"{number} is not a perfect number")


def seven(number):
    print("\ndifficult.seven:")

    total = 0

    for digit in str(number):
        total += int(digit)

    print("\t", f"sum of digits in {number} = {total}")


def eight(sentence):
    print("\ndifficult.eight:")

    words = sentence.split()
    longest = words[0]

    i = 0
    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1

    print("\t", f"longest word = {longest}")


def nine(sentence):
    print("\ndifficult.nine:")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()

    is_pangram = True

    for letter in alphabet:
        if letter not in sentence:
            is_pangram = False

    if is_pangram:
        print("\t", "this is a pangram")
    else:
        print("\t", "this is not a pangram")


def ten():
    print("\ndifficult.ten:")

    number = 2

    while number <= 1000:
        is_prime = True
        divisor = 2

        while divisor < number:
            if number % divisor == 0:
                is_prime = False
            divisor += 1

        if is_prime:
            print("\t", number)

        number += 1