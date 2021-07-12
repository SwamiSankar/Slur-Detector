import slur_count as slur
# I am assuming sentences in the file are seperated by a new line
# File Read using open function. File closing is done by means of with function
with open('content.txt', mode='r') as data:

    # Storing the content in a list using readlines function

    content_list = data.readlines()

    # If the file is empty
    if content_list == []:
        print('No data found in file')

    # I am using the function for each sentence taken from the file
    # Enumerate for knowing the sentence number for reference

    for value, content in enumerate(content_list):

        count = slur.slur_count(content)

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
