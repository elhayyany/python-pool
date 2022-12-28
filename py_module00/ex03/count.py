import re

def text_analyzer(olk = None):
    """This function counts the number of upper characters, lower characters,punctuation and spaces in a given tex."""
    if olk is None:
        print("What is the text to analyze")
        olk  = input(">>")
    if not str(olk).isdigit():
        res = list(filter(str.isupper, str(olk)))
        print(str(len(res)) + " lower letter(s)")
        res = list(filter(str.islower, str(olk)))
        print(str(len(res)) + " lower letter(s)")
        count = 0
        for c in olk:
            if c in ('!#$%&()\'*+,.:;-?@[]^_`{|}~'):
                count += 1
        print(str(count) + " punctuation mark(s)")
        print(str(len(re.findall('\s+', olk))) + " space(s)")
    else:
        print("AssertionError: argument is not a string")

text_analyzer("Python is an interpreted, high-level,general-purpose programming language. Created by Guido vanRossum and first released in 1991, Python's design philosophyemphasizes code readability with its notable use of significantwhitespace.")