import webbrowser


def check_profanity(text_to_check):
    html = webbrowser.open('http://www.wdylike.appspot.com/?q=QUERY' + text_to_check).read()
    print(html)


def read_text():
    quotes = open("/Users/Daniela/Desktop/Important shit?/test_text.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


read_text()
