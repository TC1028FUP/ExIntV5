# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["gato", "perro", "jabali", "perico", "oso", "-", "p"],
    ["Ingresa palabras, para terminar de capturar ingresa -",">>> ", ">>> ", ">>> ", 
    ">>> ", ">>> ", ">>> ", "['gato', 'perro', 'jabali', 'perico', 'oso']", "Letra: ",
    "['perro', 'perico']", "['gato', 'jabali', 'oso']"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
    ["-", "pe"],
    ["Ingresa palabras, para terminar de capturar ingresa -",">>> ","[]","Letra: ","Error"],
    ["Qué pasa si de entrada recibes un - y la letra no es un string de tamaño 1"]
    )
    ]
