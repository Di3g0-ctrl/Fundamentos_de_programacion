import json

Biblioteca = {
    "978-84-376-0494-7": {
        "Título": "Cien años de soledad",
        "Autor": ["Gabriel García Márquez"],
        "Géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "Título": "Don Quijote de la Mancha",
        "Autor": ["Miguel de Cervantes Saavedra"],
        "Géneros": ["Novela de caballería", "Satira"]
    },
      "978-84-9889-839-9": {
        "Título": "El nombre del viento",
        "Autor": ["Patrick Rothfuss"],
        "Géneros": ["Fantasía épica"]
    },
      "978-84-08-03793-3": {
        "Título": "La sombra del viento",
        "Autor": ["Carlos Ruiz Zafón"],
        "Géneros": ["Misterio", "Novela histórica contemporánea"]
    },  
      "978-0-06-112008-4": {
        "Título": "Matar a un ruiseñor",
        "Autor": ["Harper Lee"],
        "Géneros": ["Novela clásica", "Drama social"]
    }
}

Isbn = "978-84-376-0494-7"
Info_libro = Biblioteca.get(Isbn)          
print("\nInformación del libro:", Info_libro)