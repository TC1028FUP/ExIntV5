# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["gato", "perro", "jabali", "la ardilla", "oso", "-", 4],
    ["Ingresa palabras o frases, para terminar de capturar ingresa -",">>> ", ">>> ", ">>> ", 
    ">>> ", ">>> ", ">>> ", "['gato', 'perro', 'jabali', 'la ardilla', 'oso']", "Número de caracteres: ",
    "['gato', 'oso']", "['perro', 'jabali', 'la ardilla']"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
    ["-", "-1"],
    ["Ingresa palabras o frases, para terminar de capturar ingresa -",">>> ","[]","Número de caracteres: ","Error"],
    ["Qué pasa si de entrada recibes un - y el número de caracteres es negativo o cero"]
    )
    ]
