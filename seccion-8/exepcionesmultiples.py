try:
    
    c = int(input("Ingresa valor: "))
    c/0

except ValueError:
          print("Mistake, u ca use a string")
except Exception as c:
           print(type(c).__name__)
          