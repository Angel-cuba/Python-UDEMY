set_conjunto = set({1,2,3,4})
print(set_conjunto)
set_conjunto.add(12)
print(set_conjunto)
#####################
set_conjunto1 = set({1.1, "Audi", False})
set_conjunto2 = set_conjunto1.copy()
set_conjunto1 == set_conjunto2
print("segundo conjunto --->", set_conjunto2)

######################
#Discard
pakete = set({"angel", 3,4,5})
print(pakete)
pakete.discard(4)
print(pakete)

##################
#remove
pakete1 = set({"angel", 3,4,5,  "Python"})
print("pakete1: ", pakete1)
pakete1.remove("angel")
print(pakete1)
