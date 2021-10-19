![Tec de Monterrey](../../images/logotecmty.png)
# Divide una lista por número de caracteres
## Involucra ciclos, listas, condicionales

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
# Area de funciones aquí

def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Diseña e implementa un programa que recibe datos para conformar una lista de palabras, la despliega a pantalla y posteriormente procesa esa lista y construye dos más, donde en la primera están palabras que empiezan con una letra que te indique el usuario y otra lista donde están las que NO empiezan con esa letra. Para lo anterior DEBES CREAR las siguientes funciones en tu programa:

Función **crea_lista** la cual no tiene parámetros y cuya funcionalidad es recibir palabras o frases del usuario y va creando una lista con ellas. El mensaje para pedirlas será: **">>> "** El proceso de recepción de strings termina cuando el usuario ingresa un **"-"**. La función deberá **regresar** la lista como resultado de la función.

Función **divide_lista** la cual recibe como parámetro una **lista** y un caracter **letra**, la función crea una lista anidada con dos listas internas donde la primera tiene las palabras que empiezan con la letra recibida y la segunda las que NO empiezan con esa letra. La función **regresa** la lista anidada. Tip: Usa indexing de strings (recuerda que los indices empiezan en 0 como en las listas).

En el **main**, se debe desplegar el mensaje **"Ingresa palabras, para terminar de capturar ingresa -"**, luego se ingresan los datos para la lista (llama a la función correspondiente) y despliega la lista, posteriormente, pide la letra para dividir la lista con este mensaje: **"Letra: "** y luego llama a la función correspondiente para que divida la lista de acuerdo a los que empiezan con la letra y con los que no y por último despliega las dos listas, una en cada renglón, primero la lista que tiene las palabras que empiezan con la letra. **Nota:** Asegúrate que la letra recibida para dividir sea un solo caracter, si es más de un caracter despliega el mensaje de **"Error"** y termina el programa. **TIP: recuerda que len nos da el tamaño de un string.**

## Ejemplo de ejecución del programa
```
Ingresa palabras, para terminar de capturar ingresa -
>>> pelota
>>> juguete
>>> carro
>>> muñeca
>>> cosa
>>> -
['pelota', 'juguete', 'carro', 'muñeca', 'cosa']
Letra: c
['carro', 'cosa']       
['pelota', 'juguete', 'muñeca']
```

## Otro ejemplo
Ingresa palabras, para terminar de capturar ingresa -
>>> pelota
>>> juguete
>>> carro
>>> muñeca
>>> cosa
>>> -
['pelota', 'juguete', 'carro', 'muñeca', 'cosa']
Letra: perro
Error


**Nota:** No cambies ni quites el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
