# profanity-filter-python

To run this program, save it to a file (e.g., profanity.py) and run it from the command line with the name of the file you want to analyze, like so:

        python profanity.py input.txt
        
Where input.txt is the name of the file you want to analyze. The program will split the text into sentences, clean up each sentence, and score the level of profanity in each sentence using the profanity_check package. Finally, it will output a pandas DataFrame with two columns: "Sentence" and "Profanity Score", which indicates the degree of profanity for each sentence in the file.
