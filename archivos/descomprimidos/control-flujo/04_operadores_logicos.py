"""Curso de python"""


# and, or, not

combustible = True
encendido = True
licencia = True

if combustible and encendido and licencia:
    print("Puede conducir")

# if not GAS or (ENCENDIDO and LICENCIA):
#     print("Puede conducir")


# NOTA: OPERADORES DE CORTO CIRCUITO QUIERE DECIR QUE SI USAMOS EL OPERADOR LOGICO AND COMO DEBE CUMPLIRSE CADA EVALUACION SI LA PRIMERA ES FALSA EL PROGRAMA YA NO EVALUA LO DEMAS
# EN EL CASO QUE ESTEMEOS USANDO EL OPERADOR LOGICO OR ENTONCES SI LA PRIMERA ES TRUE YA NO EVALUA LO DEMAS PORQUE SOLO TIENE QUE CUMPLIRSE AL MENOS UNA Y SI LA PRIMERA ES FALSA ENTONCES AHI SI PASA A EVALUAR LO SIGUIENTE
