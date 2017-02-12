# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def unique_characters(input):
    seen_characters = []
    for letter in input:
        if letter in seen_characters:
            return False
        else:
            seen_characters.append(letter)

    return True


def unique_characters_without_struct(input):
    for lead in input:
        for follow in input:
            if input[lead] == input[follow]:
                return False
