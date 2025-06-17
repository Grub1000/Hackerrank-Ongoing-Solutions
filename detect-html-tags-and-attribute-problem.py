from html.parser import HTMLParser

n = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        [print('-> {} > {}'.format(*attribute)) for attribute in attributes]
    
html = '\n'.join([input() for x in range(0, n)])  
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# Sample Input
# 9
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash" 
#   data="your-file.swf" 
#   width="0" height="0">
#   <!-- <param name="movie" value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>

# Sample Output
# head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0
# param
# -> name > quality
# -> value > high


