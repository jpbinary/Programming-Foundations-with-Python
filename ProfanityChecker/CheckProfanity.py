import urllib

def read_text():
    quotes = open("movie_quotes.txt")
        # use open class to return a file type object
        # this creates an instance of the class open
    file_contents = quotes.read() # read file
    print(file_contents)
    quotes.close() # close file
    check_profanity(file_contents)
    

def check_profanity(text_to_check):
    # http://www.wdyl.com/ is a google website that returns whether profanity is found in a word or text
         # {"response": "false"} # if not profanity
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
        # though it looks like a function, urlopen is class that can be used to
            # initialize a file-like object
    response = connection.read()
    print(response)
    connection.close() # close connection

    if "false" in response:
        print("Document is free of profanity.")
    elif "true" in response:
        print("ALERT!!! Profanity found in document.")
    else:
        print("Error scanning document.")
    
read_text()
