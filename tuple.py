tea_type =('black',"green","oolong")
print(tea_type[-1])


more_tea = ("herabal","gao ki chai")

alltea = more_tea + tea_type 
print(alltea)

if "herabal" in alltea:
     print("i havbe")
     
print(alltea.count("black"))
