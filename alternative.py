#input string
str_given = input("Enter a sentence: ")

#function for alternating upper and lower case for each letter
def alternating_letters(s):

    #blank string for result to go in
    s_formatted = ""

    for count, value in enumerate(s):

        #odd and even differentiation & adding the aternating letters to blank string
        if count % 2 == 0:
            s_formatted += value.upper()
        else:
            s_formatted += value.lower()

    #print result
    print(s_formatted)

def alternating_words(s):

    #get each word and blank string for results to go into
    words = s.split()
    s_formatted = ""

    for count, value in enumerate(words):

        if count % 2 == 0:
            s_formatted += value.upper()
            s_formatted += ' '
        else:
            s_formatted += value.lower()
            s_formatted += ' '

    print(s_formatted)

alternating_letters(str_given)
alternating_words(str_given)
