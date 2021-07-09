# I am assuming sentences in the file are seperated by a new line
# File Read using open function. File closing is done by means of with function
with open('content.txt', mode='r') as data:

    # Storing the content in a list using readlines function

    content_list = data.readlines()

    # If the file is empty
    if content_list == []:
        print('No data found in file')

    # I have included a list of slur words marked as slur1 , slur2 , slur3 etc. which denotes the slur words in a list

    slur_words = ['slur1', 'slur2', 'slur3', 'slur4', 'slur5']

    # Function to find out the number of slur words used in a single sentence

    def slur_count(sentence):

        # Assigning the count variable to zero
        count = 0

        # Splitting the sentence into list of words
        words = sentence.split()
        for word in words:
            for slur in slur_words:
                if(word.lower() == slur):
                    count = count+1

        # Returning the slur word count
        return count

    # I am using the function for each sentence taken from the file
    # Enumerate for knowing the sentence number for reference

    for value, content in enumerate(content_list):

        count = slur_count(content)

        # Making the index as 1
        value = value + 1

        # I am assuming the degree of profanity as zero,first,second and intolerable based on the number of slur words present in a sentence
        if count == 0:
            print(value, 'This sentence is of zero degree and no action required')
        elif count == 1:
            print(value, 'This sentence is of first degree and warning is needed')
        elif count == 2:
            print(
                value, 'This sentence is of second degree and serious warning is needed')
        else:
            print(
                value, 'This sentence is of intolerable degree and tweet must have to be removed')
