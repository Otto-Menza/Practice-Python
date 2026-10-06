#Alcance de variables, local y global

variable_global = 0
def incrementar_contador():
     variable_local = 0
     # llamamos a la variable global:
     global variable_global
     #incrementamos la variable global:
     variable_global += 1

     #incrementamos la variable local:
     variable_local += 1
     print(f'Variable local: {variable_local}')
     print(f'Variable global: {variable_global}\n')
incrementar_contador()
incrementar_contador()
incrementar_contador()