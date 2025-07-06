def wrapper(f):
    def phone(l):
        f(["+91 "+c[-10:-5]+" "+c[-5:] for c in l])
    return phone

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)



# Sample Input:
# 3
# 07895462130
# 919875641230
# 9195969878

# Sample Output:

# +91 78954 62130
# +91 91959 69878
# +91 98756 41230