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
