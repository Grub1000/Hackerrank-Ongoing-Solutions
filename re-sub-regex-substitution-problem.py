import re
n = int(input())

fullText = ""
for i in range(n):
    fullText += input() + '\n'
print(re.sub(r'(?<=\s)&&(?=\s)|(?<=\s)\|\|(?=\s)', lambda i: "and" if i.group() == "&&" else "or", fullText))


# Sample Input:
# 11
# a = 1;
# b = input();
# 
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides.
# 
# 
# Sample Output:
# a = 1;
# b = input();

# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b)) 
# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides. 
# 
# 
# 
# 
# 
# 
