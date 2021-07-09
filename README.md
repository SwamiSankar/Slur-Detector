# Slur-Detector

In various social media platforms we tend to see several kinds of abusive comments which are against the guidelines of the site (Twitter , Facebook etc.). So inorder to filter out these comments based on number of slur words, I have written a code that does this work on a file that contains these comments. I have segregated into 4 degrees of abusive content based on my assumption: (Degree : Message)

1. Zero Degree : This level comprises of zero slur words and no action required
2. First Degree : This level comprises of 1 slur word and moderate action is needed
3. Second Degree : This level comprises of 2 slur words and serious warning is needed
4. Intolerable Degree : This level comprises of more than 2 slur words and the post needs to be removed

In this code present in the file filter.py , the slur words are stored in a list 'slur_words' and are mentioned as 'slur1' , 'slur2' , 'slur3' etc.

The content.txt file contains some example sentences with slur words.

The file is read through in-built file reading function (open) and using 'with' function, closing of the file is handled.

The sentences are stored in a list by means of readlines function.

Each sentence is split into words and are compared with the slur words list. If the word matches then count is increased by 1.

Based on the count at the end of the sentence, the degree is assigned.

In the same way , all the sentences in the file are allocated the degree of profanity
