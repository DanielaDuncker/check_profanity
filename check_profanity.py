from urllib.request import urlopen


def read_text():
    quotes = open("/Users/Daniela/Desktop/Coding stuff/test_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q=shot" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if True in output:
        print("Profanity Alert!!")
    elif False in output:
        print("This document has no curse words!")
    else:
        print("Could not scan tha document properly.")


read_text()
