from html.parser import HTMLParser

n = int(input())
class MyHTMLParser(HTMLParser):
    
    def handle_starttag(self, tag, attributes):
        print('Start :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attributes):
        print('Empty :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for i in range(0, n)]))


# Sample Input:
# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>

# Sample Output:
# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html




