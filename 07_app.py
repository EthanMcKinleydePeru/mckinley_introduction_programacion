#Converciones de tipos de datos

# int() -> convierte a numero entero
# Sirve para convertir un valor a un numero entero
# Si el valor es un numero decimal, corta la parte decimal (no redondea)
# Si el valor es  un texto que representa un numero entero, tambien functiona

int("25")  # (cadena a entero)
int(3.9)   # (decimal a entero, elimina los decimales)
int(True)  # (True equivale a 1)
int(False) # (False equivale a 0)

float("3.14")   # (cadena a decimal)
float(10)       # (entero a decimal)
float(True)
float(False)

str(100)       #"100"
str(3.14)      #"3.14"
str(True)      #"True"
str([1, 2, 3])   #"[1, 2, 3]"

bool(0)       # False
bool(1)       # True
bool("")      # False
bool("Hola")  # True
bool([])      # False
bool([1,2])   # True