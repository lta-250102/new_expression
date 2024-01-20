from enum import Enum

class WordType(Enum):
    NOUN = 1
    VERB = 2
    ADJECTIVE = 3
    ADVERB = 4
    PRONOUN = 5
    PREPOSITION = 6
    CONJUNCTION = 7
    INTERJECTION = 8
    DETERMINER = 9
    PUNCTUATION = 10
    UNKNOWN = 11