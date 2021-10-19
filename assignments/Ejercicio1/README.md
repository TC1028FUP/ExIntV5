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

Diseña e implementa un programa que recibe datos para conformar una listas de palabras, la despliega a pantalla y posteriormente procesa esa lista y construye dos más, donde en la primera están palabras de menos o n caracteres y otra lista donde están las de más de n caracteres. Para lo anterior DEBES CREAR las siguientes funciones en tu programa:

Función **crea_lista** la cual no tiene parámetros y cuya funcionalidad es recibir palabras o frases del usuario y va creando una lista con ellas. El mensaje para pedirlas será: **">>> "** El proceso de recepción de strings termina cuando el usuario ingresa un **"-"**. La función deberá **regresar** la lista como resultado de la función.

Función **divide_lista** la cual recibe como parámetro una lista y un número n, la función crea una lista anidada con dos listas internas donde la primera tiene las palabras con n o menos caracteres y la segunda con más de n caracteres. La función **regresa** la lista anidada.

En el **main**, se debe desplegar el mensaje **"Ingresa palabras o frases, para terminar de capturar ingresa -"**, luego se ingresan los datos para la lista (llama a la función correspondiente) y despliega la lista, posteriormente, pide el número de caracteres para dividir la lista con este mensaje: **"Número de caracteres: "** y luego llama a la función correspondiente para que divida la lista de acuerdo al número n de caracteres y por último despliega las dos listas, una en cada renglón, primero la de n o menos caracteres y luego de la más de n caracteres. **Nota:** El número de caracteres deberá ser mayor que cero, de lo contrario, deberá desplegar el mensaje **"Error"** y termina el programa.

## Ejemplo de ejecución del programa
```
Ingresa palabras o frases, para terminar de capturar ingresa -
>>> pelota
>>> la niña
>>> juguete
>>> carro
>>> muñeca
>>> escondidas
>>> -
['pelota', 'la niña', 'juguete', 'carro', 'muñeca', 'escondidas']
Número de caracteres: 6
['pelota', 'carro', 'muñeca']       
['la niña', 'juguete', 'escondidas']
```
.


**Nota:** No cambies ni quites el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
