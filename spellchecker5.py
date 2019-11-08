import re
import difflib
wordsFile = open("English.txt")                     # to import the data from the text to the code
wordsList = []
for elem in wordsFile:
    elem = elem.rstrip()
    wordsList.append(elem)                          # saves is in wordsList

def spellChecker():
    correctWords = 0
    incorrectWords = 0                                 # to count the correct and incorrect Words

    sentence = input("**Enter sentence to spellcheck**: ")
    lowerWords = sentence.lower()                   # to replace all letters to lower case
    lowerWords = re.sub('[^a-zA-z \n]','',lowerWords)
    splitWords = (lowerWords.split())               # to split the sentance to words

    for word in splitWords:
        if word not in wordsList:
            print (word + " : not found in dictionary")
            incorrectWords += 1                   # to count the number of incorrect Words
        else:
            print (word + " : spelt correctly")
            correctWords += 1                      # to count the number of correct Words

    wordsNumber = len(splitWords)
    print ("\n" + "Number of words: " + str(wordsNumber))                                  
    print ("Number of correctly spelt words: " + str(correctWords))                        # shows all the counters
    print ("Number of incorrectly spelt words: " + str(incorrectWords))
    change()

def file_cheker():
    correctWords = 0
    incorrectWords = 0
    ignoredWords = 0
    markedWords = 0                                       # to count the ignore and added and ignored Words
    addedWords = 0
    import datetime, time
    today = datetime.datetime.now()
    beginning = time.clock()

    print ("\n ________________________________________________",
    "\n\u2502                                                \u2502",
    "\n\u2502  *** L O A D  F I L E ***                      \u2502",
    "\n\u2502                                                \u2502",
    "\n\u2502         Enter the file name                    \u2502",
    "\n\u2502         then press [enter]                     \u2502",
    "\n\u2502________________________________________________\u2502")

    check_file = True
    while check_file:
        try:
            file_name = open(input ("\u2502Name of the file: "), "r")
            result = open("*checked* " + str(file_name.name), "w+")  # to produce a new file with a new name
            result.write(today.strftime("%d-%m-%Y %H:%M:%S""\n"))
            sentence = file_name.read()
            lowerWords = sentence.lower()                   # to replace all letters to lower case
            lowerWords = re.sub('[^a-zA-z \n]','',lowerWords)
            splitWords = (lowerWords.split())

            for word in splitWords:
                if word not in wordsList:
                    incorrectWords += 1                   # to count the number of incorrect Words
                    recomend = difflib.get_close_matches(word, wordsList)
                    recomend_word = str(recomend[0])
                    print ("\n ________________________________________________",
                    "\n\u2502                                                \u2502",
                    "\n\u2502  *** W O R D   N O T   F O U N D ***           \u2502")
                    print ("\u2502   " + word )
                    print ("\u2502                                                \u2502")
                    print ("\u2502  did you mean:                                 \u2502")
                    print ("\u2502  " + recomend_word )
                    print ("\u2502________________________________________________\u2502")

                    recomend_choice = True
                    while recomend_choice:                                            # asks if the user  ment the recommened word or not
                        recomend_choice = input (" Enter [y] or [n]: ")
                        if recomend_choice == "y" or recomend_choice == "Y":
                            result.write(str(recomend[0]) + " ")                     # replace the old word by a new word
                            break
                        elif recomend_choice == "n" or recomend_choice == "N":
                            print (
                            "\n ________________________________________________",
                            "\n\u2502                                                \u2502",
                            "\n\u2502  *** W O R D   N O T   F O U N D ***           \u2502",
                            "\n\u2502                                                \u2502")
                            print ("\u2502        " + word )
                            print (
                            "\u2502          1. Ignore the word                    \u2502",
                            "\n\u2502          2. Mark the word as incorrect         \u2502",
                            "\n\u2502          3. Add the word to dictionary         \u2502",
                            "\n\u2502________________________________________________\u2502")
                            word_choice = True
                            while word_choice:                                       # askes if the user wnats to ignor if press 1, mark if press 2 or add the word if press 3
                                word_choice = input("\nEnter choice: ")
                                if word_choice == "1":
                                    result.write ("!" + word + "! ")
                                    ignoredWords += 1
                                    break
                                elif word_choice == "2":
                                    result.write ("?" + word + "? ")
                                    markedWords += 1
                                    break
                                elif word_choice == "3":
                                    addedWords += 1
                                    result.write ("*" + word + "* ")
                                    f = open("English.txt","a")
                                    f.write(word + "\n")                                      # adds the new word to the dictionary
                                    break
                                else:
                                    print ("you can only choose between (1), (2) or (3)")

                            break
                        else:
                             print ("\nyou can only enter (y) or (n) ")

                else:
                    result.write (word + " ")
                    correctWords += 1                      # to count the number of correct Words

            wordsNumber = len(splitWords)
            print ("\n" + "The total umber of words: " + str(wordsNumber))
            print ("Number of correctly spelt words: " + str(correctWords))
            print ("Number of incorrectly spelt words: " + str(incorrectWords))
            print ("\nNumber of words ignored: " + str(ignoredWords))            # shows all counters
            print ("Number of words marked: " + str(markedWords))
            print ("Number of words added: " + str(addedWords))
            print ("\nTime elapsed: ", (time.clock() - beginning), "seconds")

            result.write("\nNumber of words: " + str(wordsNumber))
            result.write("\nNumber of correctly spelt words: " + str(correctWords))
            result.write("\nNumber of incorrectly spelt words: " + str(incorrectWords))      #write all counters in a new file
            result.write("\nNumber of words ignored: " + str(ignoredWords))
            result.write("\nNumber of words marked: " + str(markedWords))
            result.write("\nNumber of words added: " + str(addedWords))
            change()
            break
        except FileNotFoundError:
            print ("File not found")                                                          # print file not found if the user inputed a wrong file name

def change():                                                                                 # a function appear after finishing spell checking a file or a sentence
    changeinput = input ("\nPress (q) to quit , press (f) to check a file, press (s) to spell check a sentence: ")
    if changeinput == "q" or changeinput == "Q":
        exit()
    elif changeinput == "f" or changeinput == "F":
        file_cheker()
    elif changeinput == "s" or changeinput == "S":
        spellChecker()
    else:
        print ("You must only enter (q), (f) or (s)")
        change()

def exit():
    print (" **Good bye** ")                                                                  # to close the programe

def intro():                                                                                  # appear in the beginning
    choice = input ("\u2502_______ Enter your choice: ")                                      #allow the user to choose to spell check a file of a sentence
    if choice == "1":
        file_cheker()
    elif choice == "2":
        spellChecker()
    elif choice == "q" or choice == "Q":
        exit()
    else:
        print ("You can only chose between (1), (2) or (q)")
        intro()


print (
"\n ________________________________________________",
"\n\u2502                                                \u2502",
"\n\u2502  *** S P E L L   C H E C K E R ***             \u2502",
"\n\u2502          1. Check a file                       \u2502",
"\n\u2502          2. Check a sentence                   \u2502",
"\n\u2502          q. Quit                               \u2502",
"\n\u2502________________________________________________\u2502")
intro()
