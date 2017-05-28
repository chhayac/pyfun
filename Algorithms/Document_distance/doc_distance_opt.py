# Program to implement document distance problem to find if we are given two documents, how similar are they.
# It is used in finding similar documents, detect plagiarism / duplicates, web search , etc
# Example:
# Input:
# input_file1.txt 
#
# input_file2.txt
#
# 
# Output:
# The distance between between the documents is 0.574160(radians)
#  43 function calls in 0.077 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 :0(acos)
#        1    0.000    0.000    0.077    0.077 :0(exec)
#        2    0.001    0.001    0.001    0.001 :0(lower)
#        2    0.000    0.000    0.000    0.000 :0(maketrans)
#        2    0.000    0.000    0.000    0.000 :0(nl_langinfo)
#        2    0.000    0.000    0.000    0.000 :0(open)
#        1    0.000    0.000    0.000    0.000 :0(print)
#        2    0.001    0.000    0.002    0.001 :0(read)
#        1    0.001    0.001    0.001    0.001 :0(setprofile)
#        2    0.019    0.010    0.019    0.010 :0(split)
#        1    0.000    0.000    0.000    0.000 :0(sqrt)
#        1    0.000    0.000    0.000    0.000 :0(sum)
#        2    0.001    0.001    0.001    0.001 :0(translate)
#        2    0.001    0.000    0.001    0.000 :0(utf_8_decode)
#        1    0.005    0.005    0.077    0.077 <string>:1(<module>)
#        2    0.000    0.000    0.000    0.000 _bootlocale.py:23(getpreferredencoding)
#        2    0.000    0.000    0.000    0.000 codecs.py:259(__init__)
#        2    0.000    0.000    0.000    0.000 codecs.py:308(__init__)
#        2    0.000    0.000    0.001    0.000 codecs.py:318(decode)
#        2    0.000    0.000    0.022    0.011 doc_distance_opt.py:51(get_words_from_text)
#        2    0.000    0.000    0.000    0.000 doc_distance_opt.py:52(<dictcomp>)
#        2    0.045    0.023    0.045    0.023 doc_distance_opt.py:62(count_words_freq)
#        2    0.002    0.001    0.002    0.001 doc_distance_opt.py:70(sum_square)
#        1    0.000    0.000    0.003    0.003 doc_distance_opt.py:77(vector_angle)
#        1    0.001    0.001    0.001    0.001 doc_distance_opt.py:78(<listcomp>)
#        1    0.000    0.000    0.072    0.072 doc_distance_opt.py:84(main)
#        1    0.000    0.000    0.077    0.077 profile:0(main())
#        0    0.000             0.000          profile:0(profiler)


import math
import string

# Function reads each document into one large string and breaks up the entire
# document into words at once
def get_words_from_text(text):
    translation_table = str.maketrans({key: " " for key in string.punctuation})

    # Library function translate is used here for converting uppercase characters
    # to lowercase and for converting punctuation to spaces
    text = text.translate(translation_table) 
    text = text.lower()
    word_list = text.split()
    return word_list

# Calculate the frequency of words in a wordlist
def count_words_freq(word_list):
    count_doc = {}
    for word in word_list:
        try: count_doc[word] += 1
        except KeyError: count_doc[word] = 1
    return count_doc

# Calculate the sum of squares of a vector
def sum_square(count_doc):
    sum = 0
    for key in count_doc:
        sum  = sum + (count_doc[key] * count_doc[key])
    return sum

# Calculate angle between two vectors
def vector_angle(word_freq_doc1, word_freq_doc2):
    numerator = sum([word_freq_doc1[k] * word_freq_doc2[k] for k in word_freq_doc1 if k in word_freq_doc2])
    sum1 = sum_square(word_freq_doc1)
    sum2 = sum_square(word_freq_doc2)
    denominator = math.sqrt(sum1 * sum2)
    return math.acos(numerator/denominator)

def main():
    text1 = open("input_file1.txt",'r').read()
    word_doc1 = get_words_from_text(text1)

    text2 = open("input_file2.txt", 'r').read()
    word_doc2 = get_words_from_text(text2)

    word_freq_doc1 = count_words_freq(word_doc1)
    word_freq_doc2 = count_words_freq(word_doc2)

    distance = vector_angle(word_freq_doc1, word_freq_doc2)
    print("The distance between between the documents is %0.6f(radians)" %distance)


if __name__ == '__main__':
    # profile gives a set of statistics that describes how often and for how long various parts of the program executed
    import profile
    profile.run("main()")