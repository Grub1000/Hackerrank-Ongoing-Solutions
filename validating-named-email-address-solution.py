import email.utils
import re

n = int(input())

regex = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
for i in range(0, n):
    parsedAddress = email.utils.parseaddr(input())
    if re.search(regex, parsedAddress[1]):
        print(email.utils.formataddr(parsedAddress)) 





# Sample Input:
# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>

# Sample Output:
# DEXTER <dexter@hotmail.com>















