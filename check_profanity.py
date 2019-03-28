def check_profanity(text_to_check):
    from urllib.request import urlopen
    html = urlopen('http://www.wdylike.appspot.com/?q=QUERY' + text_to_check).read()
    print(html)


def read_text():
    quotes = open("/Users/Daniela/Desktop/Coding stuff/test_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


read_text()
