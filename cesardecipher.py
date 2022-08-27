global alphabet
alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z')
alphabetshort = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z')
letters=[]

def decipher():

    try:
        method = int(input('''What do yout want to do?\n\n(1) Normal translation\n(2) Brute force translation\n(3) Exit\n\n'''))
    except ValueError:
        print('Not a valid number')
        return

    if method == 3:
            exit()
    elif method == 1:
        Rletters = []
        Lletters = []
        try:
            shift = int(input('Input shift value: '))
        except ValueError:
            print('Not a number')
            return

        phrase = input('Input phrase to be decoded:\n')

        for i in phrase:
            if alphabet.count(i) > 0:
                Lletters.append(alphabet[alphabet.index(i)+shift])
                Rletters.append(alphabet[alphabet.index(i)-shift])
        right = ''.join(Rletters)
        left = ''.join(Lletters)
        print(f'Right shift: {right}\nLeft shift: {left}\n')
    elif method == 2:
        Rletters = []
        Lletters = []

        phrase = input('Input phrase to be decoded:\n')

        for x in range(26):
            for i in phrase:
                if alphabet.count(i) > 0:
                    Lletters.append(alphabet[alphabet.index(i)+x])
                    Rletters.append(alphabet[alphabet.index(i)-x])
            right = ''.join(Rletters)
            left = ''.join(Lletters)
            print(f'Right shift: {right}\nLeft shift: {left}\n')
            Rletters.clear()
            Lletters.clear()
            right = ''
            left = ''

        

while True:
    decipher()
