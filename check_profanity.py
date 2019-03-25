def read_text():
    quotes = open("/Users/Daniela/Desktop/Important shit?/test_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()


read_text()
