alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z')

letters=[]
r=input("please input shift value: ")
phrase=input("frase: ")
size = len(phrase)

for i in phrase:
    letters.append(i)

for i in range(len(letters)):
    if letters[i] != ' ':
        letters[i]=alphabet[alphabet.index(letters[i])-int(r)]
print(''.join(letters))
