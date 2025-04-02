#shanmai
def r1(w):
    if w=="o":
        return 0
    if w=="i":
        return 1
    elif w=="ii" :
        return 2
    elif w == "iii" :
        return 3
    elif w == "iv" :
        return 4
    elif w=="v" :
        return 5
    elif w=="vi" :
        return 6
    elif w=="vii" :
        return 7
    elif w=="viii" :
        return 8
    elif w=="ix" :
        return 9
    elif w=="x" :
        return 10
    elif w=="xi" :
        return 11
def r2(z):
    if w=="o":
        return 0
    if z=="i":
        return 1
    elif z=="ii" :
        return 2
    elif z == "iii" :
        return 3
    elif z == "iv" :
        return 4
    elif z=="v" :
        return 5
    elif z=="vi" :
        return 6
    elif z=="vii" :
        return 7
    elif z=="viii" :
        return 8
    elif z=="ix" :
        return 9
    elif z=="x" :
        return 10
    elif z=="xi" :
        return 11
w=input("Enter the 1st Number:    ")
z=input("Enter the 2nd Number:   ")
e=r1(w) + r2(z)
print("The solution is ",e)
if e==0:
    print("sol= o")
if e==1:
    print("sol= i")
if e==2:
    print("sol= ii")
if e==3:
    print("sol= iii")
if e==4:
    print("sol= iv")
if e==5:
    print("sol= v")
if e==6:
    print("sol= vi")
if e==7:
    print("sol= vii")
if e==8:
    print("sol= viii")
if e==9:
    print("sol= ix")
if e==10:
    print("sol= x")
if e==11:
    print("sol= xi")



