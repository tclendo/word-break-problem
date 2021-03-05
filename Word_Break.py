# assignment6.py

class SplitPhrase:

    def __init__(self, phrases):

        # initialize the number of phrases we will work with
        self.phrases = phrases
        # initialize our dictionary of words
        self.dictionary = {}
        temp = open("diction10k.txt")
        for line in temp:
            self.dictionary[line.strip()] = ''

        # hold one array for an array of strings, and the other to 
        # see if it can be split into all words in our dictionary
        self.words = []

    def lookup(self, word):

        # if the input word exists in our dictionary,
        # we return true, otherwise return false
        if word in self.dictionary.keys():
            return True

        return False

    def checkPhrase(self, line, size):

        # table where we will keep track of all the values
        table = [True]
        for i in range(0, size):
            table.append(False)

        # iterate from the first to last letter
        for i in range(0, size + 1):

            # iterate from 0 to i
            for j in range(0, i):

                # split the word at those 2 indices
                split = line[j:i]

                # if the j index can split into a word and 
                # j:i is also a word
                if table[j] and self.lookup(split):

                    # set the table index at i to True, to
                    # to represent that a word can be made
                    table[i] = True

                    # add the freshly split word to our word
                    # list for this line
                    self.words[i] = (split,j,i)

        # if the last element in the table can be split, then
        # the whole phrase can be split into words
        return table[size]
    
    def getPhrases(self):

        # as long as we are accepting new lines of test phrases
        for a in range(0, self.phrases):

            # let's get the input and store it, removing the newline
            line = input().splitlines()[0]

            # it's a good idea to store the size of the string
            size = len(line)

            for i in range(0, size + 1):
                #               word, start, end
                self.words.append(("", 0, 0))

            containsWords = self.checkPhrase(line, size)
            
            print("phrase {}".format(a + 1))
            print(line)
            print()
            print("output {}".format(a + 1))

            # if the word can be split
            if containsWords:
                print("YES, can split.")

                # initialize our list for printing
                printList = []

                # we will iterate down our self.word list
                # by starting at the end index of a word and then
                # hopping to the start index of that word, which
                # will always bring us to 0 and print out all
                # of the words in the line
                i = size
                while i != 0:
                    printList.append(self.words[i][0])
                    i = self.words[i][1]

                # reverse the list because we added the word in
                # backwards
                printList.reverse()
                for element in printList:
                    print(element, end=" ")

                print()

            else:
                print("NO, cannot split.")

            print()

            # reset the words list
            self.words.clear()
###

def main():

    '''
    '''

    # get the number of lines to read from the input
    lines = int(input())

    # create a new splitter object
    splitter = SplitPhrase(lines)

    # get the phrases from our input
    splitter.getPhrases()

if __name__ == '__main__':
    main()