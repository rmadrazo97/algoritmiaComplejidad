# ASCII MergeSort -Algoritmia y Complejidad 2018
Oraciones ordenadas por ASCII utilizando el algoritmo de ordenamiento MergeSort.

## 1

Clonar el repositorio.

### 2 Requisitos
Para facilitar la exploración de este proyecto, se ha agregado un docker file. Si desea evaluarlo por medio de docker, es necesario que tenga docker instalado. Si no es el caso, puede probar el proyecto localmente, el único requisito sería tener python en su computadora.
### 3 Preparando el proyecto

-Paso a Paso...

#### Docker:
Si se usa docker:
construir la imagen
```
docker build -t mergesort .

```

levantar contenedor con puerto expuesto y sh para explorar el contenedor.
```
$ docker run -it -p 5000:5000 -v $(pwd):/code mergesort1 sh

```

### Con Python en computadora local
Teniendo python instalado...
```
pip install jug

```
```
pip install os

```
```
pip install dispy

```
```
pip install flask

```


## 4. Tests

Como testear el proyecto.
-Agregar las oraciones a ordenar en el archivo llamado>> "unorderedFile.txt"
--las oraciones se separan por [ENTER] y no existe limite para la cantidad de oraciones.

### paso 1
Al finalizar este paso, jug imprime un resumen de las "tasks" ejecutadas de manera paralela
```
jug execute main.py

```
### paso 2
Ver el estado de las tareas ejecutadas por jug
```
jug status main.py

```
### paso 3
Ver el resultado
```
cat orderedFile.txt

```
Ver el resultado en un navegador web con flask
--Este paso permite observar el resultado en el puerto expuesto en el levantamiento del contenedor. 
```
python app.py

```

## Authors

* **Alejandro Madrazo** 

