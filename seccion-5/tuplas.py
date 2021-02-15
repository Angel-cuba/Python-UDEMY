tupla = (4, "Angel", 4, 1.2, True, [1,2,3,4], 33)
tutu = [4, "Angel", 1.2, True, [1,2,3,4], 33]
tutu.append(22)
print(tutu)

print(tupla[:-1])
print("Angel" in tupla)
print(tupla.index(33))
print(tupla.count(4))
print("Cantidad de elementos en la tupla: ", len(tupla))