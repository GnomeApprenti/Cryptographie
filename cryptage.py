alphabet = {"A": 0, "B" : 1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25," " : 26,",":27,"'":28 ,".":29}
keys=list(alphabet.keys())
values=alphabet.values()


def crypt(car):
    crypt = ""
    for k in car:
        x=alphabet[k]
        y=(7*x+5)%30
        newCar = keys[y]
        crypt += newCar
    return crypt



def cryptage(car, tour=0):
    if tour == len(car):
        return car
    else:
        car = crypt(car)
        return cryptage(car, tour+1)

print(cryptage("RAPPER LA RUE NE VEUT PAS DIRE ETRE UN BANDIT DE LA VILLE"))

def decrypt(car):
    decrypt = ""
    for k in car:
        y=alphabet[k]
        x=(13*y+25)%30
        newCar = keys[x]
        decrypt += newCar
    return decrypt

def decryptage(car, tour=0):
    if tour == len(car):
        return car
    else:
        car = decrypt(car)
        return decryptage(car, tour+1)

print(decryptage("OPAANORCPROFNRQNRMNF'RAPVRGLONRN'ONRFQRWPQGL'RGNRCPRMLCCN"))

