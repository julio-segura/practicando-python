tipos_de_persona = 10
x = f"Hay {tipos_de_persona} tipos de personas."

binario = "binario"
no = "no"
y = f"Aquellos que saben {binario} y aquellos que {no}."

print(x)
print(y)

print(f"Dije: {x}")
print(f"También dije: '{y}")

gracioso = False
evaluacion_broma = "¿No es divertida esa broma? {}"

print(evaluacion_broma.format(gracioso))

w = "Este es el lado izquierdo de..."
e = "una cuerda con un lado derecho."

print(w + e)