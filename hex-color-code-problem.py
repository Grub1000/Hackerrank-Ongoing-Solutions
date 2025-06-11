import re
n = int(input())
fullInputText = ""
for i in range(n):
    string = input()
    fullInputText = fullInputText + "\n" + string
match = re.findall(r":?.(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})", fullInputText)
for i in range(len(match)):
    string = match[i]
    print(string)

# Sample Input:
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# } 

# Sample Output:
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff