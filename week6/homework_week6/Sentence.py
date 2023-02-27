'''
Pedro Ramirez
Class: CS 521 - Spring 1
Date: 2/26/2023
Homework Problem #6_1
Description:
Write a python class library called Sentence that evaluates and manipulates
an English sentence. Your program will be called Sentence.py and contain 
the following class attributes and methods: 

A constructor that takes a sentence string as input.
it must contain several methods, sucha as:
get_all_words, get_word, set_word, scramble, and repr

In Sentence.py, include a unit test that does the following: 
Runs inside an if __name__ block and validates set_word() method
Use assert command when checking for errors 
At the end of your unit test, print:
a message that the sentence worked correctly and
the original scrambled and fianl version of your sentence
'''
import string
from random import shuffle
import unittest


class Sentence:
    # constructor
    def __init__(self, sentence=""):
        # remove punctuation
        self.s = sentence.translate(str.maketrans('', '', string.punctuation))
        self.__sentence = self.s.split()

    def get_all_words(self):
        # return all words as a list
        return self.__sentence

    def get_word(self, index):
        # return the word at the given index
        try:
            return self.__sentence[index]
        except IndexError:
            return ''

    def set_word(self, index, new_word):
        # set the word at the given index
        self.__sentence[index] = new_word

    def scramble(self):
        # scramble the words in the sentence from a copy
        scrambled_sentence = self.__sentence.copy()
        shuffle(scrambled_sentence)
        return scrambled_sentence

    def __repr__(self):
        # return the sentence as a string
        return " ".join(self.__sentence) + "."


if __name__ == "__main__":
    s1 = Sentence("Python! is a great! programm@ing language.")

    class TestSentence(unittest.TestCase):
        def test_set_word(self):
            s1.set_word(3, "fantastic")
            # assertion to validate the set_word() method
            assert (
                s1.get_all_words()[3] == "fantastic"
            ), "The word at index 3 from the sentence should be 'fantastic'"
            print("--- Sentence unit test was successful! ---")
            print("The original sentence is:", s1.s)
            print("The scrambled version is:", " ".join(s1.scramble()))
            print("The final version is:", " ".join(s1.get_all_words()))

    unittest.main()
