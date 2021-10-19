![Tec de Monterrey](../../images/logotecmty.png)
# Matriz intercalada
### Listas anidadas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Escribe un programa que lea el tamaño de una matriz cuadrada y cree una lista anidada con caracteres **&** y **_** que represente una matriz de números como se ve en el ejemplo.  

Crea dos funciones:  

1) Una función **crea_matriz** que reciba como parámetro el tamaño de la matriz y que cree una matriz cuadrada de ese tamaño y con las características del ejemplo.  

2) Una función **despliega_matriz** que muestra en la pantalla los elementos en forma de tabla, **esta ya la tienes implementada en tu archivo, no la cambies**

3) En tu función **main**, recibe un entero que representa el tamaño para la matriz con el mensaje **">>> "**, si está entre 2 y 20 inclusive, ejecuta la función para generar la matriz intercalada e imprimela a pantalla con la función correspondiente. En caso de que el tamaño no esté en ese intervalo, despliega el mensaje **Error**.

## Entradas
El tamaño de la matriz cuadrada (leerá solamente un número ya que la matriz tiene la misma cantidad de renglones y de columnas).

## Salida  
Una serie de datos acomodados en forma de tabla que contiene los caracteres **&** y **_**, como se muestra en el ejemplo. O Mensaje **Error** si el número es menor a 2 o mayor a 20.

## Ejemplo de ejecución del programa
```
>>> 4   <---- Tamaño de la matriz cuadrada
& _ _ _
& _ _ _
& _ _ _
& & & &
```
## Otro ejemplo
```
>>> 3
& _ _
& _ _
& & &
```
## Otro ejemplo más
& _
& &
```
## Ultimo ejemplo
```
>>> 21
Error
```

**Nota:** No quites ni modifiques el código `if __name__ == '__main__':` 

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
