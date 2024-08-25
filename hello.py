chai = {"masala":"yummy ","podina":"good ","tulsi":"green ",}
chai["masala"]="bekar"
print(chai)
for chai1 in chai:
    print(chai1,chai[chai1])
    for key , value in chai.items():
        print(key,value)
        
if "masala" in chai:
    print("i have")

chai["earl grey"]="citrus"
print(chai)