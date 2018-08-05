
'''

Two strings, a and b, are said to be twins only if they can be made equivalent by performing some number of operations on one or both strings. There are two possible operations:

SwapEven: Swap a character at an even-numbered index with a character at another even-numbered index.
SwapOdd: Swap a character at an odd-numbered index with a character at another odd-numbered index.

'''






def is_wordtwin(word1,word2):
    '''input: two strings
       output: is string are twin True else False
    '''

    if len(word1)!= len(word2):
        return False

    for i in range(len(word1)):
        odd_word1= set()
        even_word1 = set()
        odd_word2 = set()
        even_word2 = set()
        if i% 2== 0:
            odd_word1.add(word1[i])
            odd_word2.add(word2[i])
        else:
            even_word1.add(word1[i])
            even_word2.add(word2[i])

    if ((odd_word1) == (odd_word2)) & ((even_word1) == (even_word2)):
        return True
    else:
        return False



if __name__ == '__main__':

    word1='abcd'
    word2='cbad'

    twinning=is_wordtwin(word1,word2)
    print (twinning)
