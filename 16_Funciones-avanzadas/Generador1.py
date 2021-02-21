def devolver_pais(*paises):
    for item in paises:
#         for subitem in item:
#                       yield subitem
            yield from item
resultado = devolver_pais("Cuba", "Espana", "EU", "Noruega", "Nigeria")
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
