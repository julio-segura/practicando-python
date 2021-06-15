
nombre = "Julio"
edad = 36
altura = 168
peso = 70
ojos = "marron"
dientes = "blancos"
pelo = "castaño"

print(f"Hablemos sobre {nombre}.")
print(f"Él mide {altura} centimetros.")
print(f"Él pesa {peso} kilos.")
print("No pesa mucho.")
print(f"Tiene los ojos color {ojos} y el pelo {pelo}.")
print(f"Sus dientes suelen ser {dientes} dependiendo del café.")

# esta línea es complicada, intenta hacerla exactamente igual

total = edad + altura + peso
print(f"Si sumo {edad}, {altura}, {peso}, obtengo {total}.")

print("\n")

print("Convertir centímetros y kilos en pulgadas y libras, usando variables.")

kilo = 2.20462 # libras
centimetro = 0.393701 # pulgadas
libra = 0.453592 # kilogramos
pulgada = 2.54 # centimetros

print(f"Un kilo son {kilo} libras.")
print(f"Un centimetro son {centimetro} pulgadas.")



print(f"Mi peso en libras es de {round(peso*kilo)} libras.")
print(f"Mi altura en pulgadas es de {round(altura*centimetro)} pulgadas.")