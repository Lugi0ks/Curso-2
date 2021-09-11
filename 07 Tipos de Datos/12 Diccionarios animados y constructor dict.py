# Vamos a crear un diccionario llamado gatitos que este tendra mas diccionarios 
#dentro de este
gatitos = {
    "Fluffy" : {
        "nombre":"Fluffy",
        "edad": 4
    },
    "Mamba" : {
        "nombre": "Mamba",
        "edad": 5
    }
}
print(gatitos)

# Otra manera de realizar esto es de la siguiente manera
mj = {
    "Nombre" : "MJ",
    "edad": 3
}
kd = {
    "Nombre" : "KD",
    "edad": 5
}
perritos = {
    "Mj" : mj,
    "Kd" : kd
}
print(perritos)

# La otra manera es utilizar el construcctor 'dict' se tiene que crear una 
#variable
jugador = dict(nombre = "James Harlen", mvp = "Si")
print(jugador)