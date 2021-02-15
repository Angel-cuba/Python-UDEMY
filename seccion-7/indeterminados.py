def infinito(*args):
    print(args)

infinito("Angel", 20, 10.4, [1,2,3])    


#############

def infinito(*args):
            for args in args:                            
              print(args)

infinito("Angel", 20, 10.4, [1,2,3])    
#########___LISTA___###########
def infinito(**kwargs):
              print(kwargs)

infinito(a="Angel Luis", b= 20, c=10.4, d=[1,2,3])    

########___BIBLIOTECA___########
def infinito(**kwargs):
           for kwarg in kwargs:
                            
              print(kwarg,"-->", kwargs[kwarg])

infinito(a="Angel Luis", b= 20, c=10.4, d=[1,2,3])    