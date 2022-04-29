


#This code is to be credited if used
#Authors: TreeBronch
#Website: treebronch.github.io

import sys,time,random

#With help from here @Bill Gross https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing
typing_speed = 120 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(10.0/typing_speed)
    print('')

import math

affine = {
  "a":0,
  "b":1,
  "c":2,
  "d":3,
  "e":4,
  "f":5,
  "g":6,
  "h":7,
  "i":8,
  "j":9,
  "k":10,
  "l":11,
  "m":12,
  "n":13,
  "o":14,
  "p":15,
  "q":16,
  "r":17,
  "s":18,
  "t":19,
  "u":20,
  "v":21,
  "w":22,
  "x":23,
  "y":24,
  "z":25,
}
affine_value_list = list(affine.values())
affine_key_list=list(affine.keys())

def encrypt(s, a, b):
  a= int(a)
  b=int(b)
  s=s.lower()
  if math.gcd(a, 26)!=1:
    print("ERROR, Alpha isn't coprime with 26")
    return False
  else:
    enc=[]
    str=[]
    str[:0] = s
    for x in range(len(s)):
      num=affine[str[x]]
      num = int(num)
      newnum=(a*num+b) % 26
      enc.append(affine_key_list[newnum])
    ciphert="".join(enc)
    print(ciphert.upper())
    
def decrypt(s, a, b):
    a = int(a)
    b=int(b)
    s=s.lower()
    if math.gcd(a, 26)!=1:
        print("ERROR, Alpha isn't coprime with 26")
    else:
        ainv = 0
        enc=[]
        str=[]
        str[:0] = s
        for x in range(27):
            if (a*x) % 26==1:
                ainv=x
                break
        for x in range(len(s)):
            num=affine[str[x]]
            num = int(num)
            newnum=(ainv*(num-b)) % 26
            enc.append(affine_key_list[affine_value_list.index(newnum)])
        ciphert="".join(enc)
        print(ciphert.lower())
        print(ainv)


slow_type("Made by TreeBronch")
slow_type("Go check out my website treebronch.github.io")
while True:
    typ = input("What would you like to do? AE-Affine Encrypt AD-Affine Decrypt\n")
    typ = typ.upper()
    if typ == "AE":
        inp = input("Enter PT\n")
        alp = input("Enter Alpha\n")
        bet = input("Enter Beta\n")
        encrypt(inp, alp, bet)
    if typ == "AD":
        inp = input("Enter CT\n")
        alp = input("Enter Alpha\n")
        bet = input("Enter Beta\n")
        decrypt(inp, alp, bet)
