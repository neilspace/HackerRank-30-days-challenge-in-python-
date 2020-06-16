# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phone_book = dict()
for i in range(n):
    name,number = input().split()
    phone_book[name]=number


for i in range(n):
    try:
        name = input()
        if name in phone_book:
            print(f"{name}={phone_book[name]}")
        else:
            print("Not found")
    except:
        break
