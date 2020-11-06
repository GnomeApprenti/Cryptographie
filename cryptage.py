alphabet = {"A": 0, "B" : 1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25," " : 26,",":27,"'":28 ,".":29}
keys=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " " ,",", "'", "."]
n=len(keys)
values=alphabet.values()
a = int(input('Saisissez un nombre parmi cette liste : [1,7,9,11,13,17,19,21,23,29] : '))
b = int(input('Saisissez un nombre entre 1 et 30 : '))
caract = input('Saisissez un message à crypter uniquement en majuscules : ')
print('la clé de cryptage est : ', a, 'x + ',b)


def crypt(car):
    crypt = ""
    for k in car:
        x=alphabet[k]
        y=(a*x+b)%n
        crypt += keys[y]
    return crypt



def cryptage(car, tour=0):
    if tour == len(car):
        return car
    else:
        car = crypt(car)
        return cryptage(car, tour+1)

print('Votre message crypté est : ', cryptage(caract))

def findAB(a,b):
    for i in range(1,n+1):
        if (a*i)%n == 1:
            k=i
            break
    a=k
    b*=-k
    b=b%n

    return a,b


ab = findAB(a,b)

def decrypt(car,a,b):
    decrypt = ""
    for k in car:
        y=alphabet[k]
        x=(a*y+b)%n
        decrypt += keys[x]
    return decrypt

def decryptage(car, tour=0):
    if tour == len(car):
        return car
    else:
        car = decrypt(car, ab[0], ab[1])
        return decryptage(car, tour+1)

print(cryptage(caract), 'décrypté donne : ', decryptage(cryptage(caract)))
