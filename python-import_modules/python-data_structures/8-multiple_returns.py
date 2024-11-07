#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence:
        length = len(sentence)
        first_character = sentence[0]
    else:
        length = 0
        first_character = None

    return (length, first_character)
