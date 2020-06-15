n = int(input())
for i in range(n) :
        strings = input()
        even = ''
        odd = ''
        for i in range(len(strings)):
            if (i%2==0):
                even += strings[i]
            else :
                odd += strings[i]
        print('{} {}'.format(even,odd))
