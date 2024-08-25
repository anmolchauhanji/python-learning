a = ["anmol", "jii", "haiu"]
for jii in a:
    print(jii)
    

    
a.append("added")
if "added" in a :
    print('i have')
    
print(a)  

a.pop()
print(a)

a.remove("jii")
print(a)

a.insert(2,"element")
print(a)

acopy = a.copy()
print(acopy)

squarenum = [x**2 for x in range(10)]
print(squarenum)
