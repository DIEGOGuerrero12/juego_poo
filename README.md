# SOKOBAN
## 1.Objetivo
### 1.1 General
Programar el juego Sokoban en una versión retro para consola.
### 1.2 Especificos
* Aplicar los conocimientos básicos de programación orientada a objetos con Python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).
* Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.
* Utilizar Kanban para dar seguimiento a las actividades a realizar ToDo, Doing, Done.
* Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.
*Documentar el código generado.

### 2. Reglas del juego
El juego sokoban consiste en recorrer un mapa en forma de laberinto para empujar cajas que estan repartidas en el mapa, hacia puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.

2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.

3. El personaje se moverá en un mapa predefinido.

4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.

5. Cada nivel tiene distinto número de cajas y metas.

6. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.
### 3.Elementos del juego
Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).
### 3.1 Mapa de juego
Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
mapa = [
            [3,3,3,3,3,3,3],
            [3,4,4,4,4,4,3],
            [3,4,0,4,1,2,3],
            [3,4,4,4,4,4,3],
            [3,3,3,3,3,3,3]
        ]
````

### 3.2 Lista de elementos
Para esta versión del sokoban se utilizarán numeros para representar cada uno de los elementos del juego.
| Número | Interpretación |
| --- | --- |
| 0 | Personaje |
| 1 | Cajas |
| 2 | Metas |
| 3 | Paredes |
| 4 | Piso |
| 5 | Pesonaje_meta |
| 6 | Caja_meta |
### 4. Controles
Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:
| Letra | Dirección del movimiento |
| -- | -- |
| a | Izquierda |
| d | Derecha |
| w | Arriba |
| s | Abajo |

### 5. Modo de juego

El juego consiste mostrar el mapa y solicitar al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se presiona enter, se evalua el moviento, si es un movimiento valido se realiza el cambio en el array, es decir se actualiza el mapa, y se repite este proceso forma infinita, hasta que se hayan terminado de acomodar todas las cajas sobre las metas.


### 6. Funciones a implementar

Después de realizar un análisis del juego sokoban se identifican funciones necesarias para completarlo, a continuación se crea una tabla con la lista de estas funciones para tener un mejor control sobre el avance del desarrollo del juego.
Para llevar un mejor control del avance del desarrollo se utiliza la metodología Kanban, indicando en que estatus de desarrollo se encuentra cada función del juego
| Valor | Interpretación |
| -- | -- |
| ToDo | Por hacer |
| Doing | Programando y validando |
| Done | Programada y validada con éxito |

### 6.1 Funciones Generales
| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | - | - |
| 1. | Repetir el juego hasta terminar el nivel. | - | - |
| 2. | Imprimir mapa.| Done | 19-02-2024 |
| 3. | Leer el movimiento. | Done | 19-02-2024 |
| 4. | Evaluar el movimiento del usuario. | Done | 19-02-2024 |

### 6.2 **creacion de movimientos de derecha**
Ejemplo de movimientos Inicio y Fin:
- Personaje, Espacio [0,4] -> Espacio, Personaje [4,0]

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Done | [0,4] | [ 4,0] | 21-02-2024 |
| 6. | Personaje, meta  | Done | [0,2] | [4,5] | 21-02-2024 |
| 7. | Personaje, caja, espacio | Done | [0,1,4] | [4,0,1] | 21-02-2024 |
| 8. | Personaje, caja,  meta | Done | [0,1,2] | [4,0,6] | 21-02-2024 |
| 9. | Personaje, caja_meta, espacio | Done | [0,6,4] | [4,5,1] | 21-02-2024 |
| 10. |Personaje, caja_meta, meta | Done | [0,6,2] | [4,5,6] | 21-02-2024 |
| 11. | Personaje_meta, espacio | Done | [5,4] | [2,0] | 21-02-2024 |
| 12. | Personaje_meta, meta | Done | [5,2] | [2,5] | 21-02-2024 |
| 13. | Personaje_meta, caja, espacio | Done | [5,1,4] | [2,0,1] | 21-02-2024 |
| 14. | Personaje_meta, caja, meta | Done | [5,1,2] | [2,0,6] | 12-04-2024 |
| 15. | Personaje_meta, caja_meta, espacio | Done | [5,6,4] | [2,5,1] | 12-04-2024 |
| 16. | Personaje_meta, caja_meta, meta | Done | [5,6,2] | [2,5,6] | 12-04-2024 |
   
### 6.3 **creacion de movimientos de izquierda**
| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje, espacio | Done | [4,0] | [0,4] | 21-02-2024 |
| 18. | Personaje, meta | Done | [2,0] | [5,4] | 21-02-2024 |
| 19. | Personaje, caja, espacio | Done | [4,1,0] | [1,0,4] | 21-02-2024 |
| 20. | Personaje, caja, meta | Done | [2,1,0] | [6,0,4] | 21-02-2024 |
| 21. | Personaje, caja_meta, espacio | Done | [4,6,0] | [1,5,4] | 21-02-2024 |
| 22. | Personaje, caja_meta, meta | Done | [2,6,0] | [6,5,4] | 13-03-2024 |
| 23. | Personaje_meta, espacio | Done | [4,5] | [0,2] | 21-02-2024 |
| 24. | Personaje_meta, meta | Done | [2,5] | [5,2] | 21-02-2024 |
| 25. | Personaje_meta, caja, espacio | Done | [4,1,5] | [1,0,2] | 21-02-2024 |
| 26. | Personaje_meta, caja, meta | Done | [2,1,5] | [6,0,2] | 13-04-2024 |
| 27. | Personaje_meta, caja_meta, espacio | Done | [4,6,5] | [1,5,2] | 13-04-2024 |
| 28. | Personaje_meta, caja_meta, meta | Done | [2,6,5] | [6,5,2] | 13-04-2024 |


### 6.4 **creacion de movimientos de arriba**
| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje, espacio | Done | [0][4] | [4][0] | 21-03-2024 |
| 30. | Personaje, meta | Done | [0][2] | [4][5] | 21-03-2024 |
| 31. | Personaje, caja, espacio | Done | [0][1][4] | [4][0][1] | 21-03-2024 |
| 32. | Personaje, caja, meta | Done | [0][1][2] | [4][0][6] | 21-03-2024 |
| 33. | Personaje, caja_meta, espacio | Done | [0][6][4] | [4][5][1] | 21-03-2024 |
| 34. | Personaje, caja_meta, meta | Done | [0][6][2] | [4][5][6] | 13-04-2024 |
| 35. | Personaje_meta, espacio | Done | [5][4] | [2][0] | 13-04-2024 |
| 36. | Personaje_meta, meta | Done | [5][2] | [2][5] | 13-04-2024 |
| 37. | Personaje_meta, caja, espacio | Done | [5][1][4] | [2][0][1] | 13-04-2024 |
| 38. | Personaje_meta, caja, meta | Done | [5][1][2] | [2][0][6] | 13-04-2024 |
| 39. | Personaje_meta, caja_meta, espacio | Done | [5][6][4] | [2][5][1] | 13-04-2024 |
| 40. | Personaje_meta, caja_meta, meta | Done | [5][6][2] | [2][5][6] | 13-04-2024 |
### 6.5 **creacion de movimientos de abajo**
| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje, espacio | - | [4][0] | [0][4] | 21-03-2024 |
| 42. | Personaje, meta | - | [2][0] | [5][0] | 21-03-2024 |
| 43. | Personaje, caja, espacio | - | [4][1][0] | [1][0][4] | 21-03-2024 |
| 44. | Personaje, caja, meta | - | [2][1][0] | []6[0][4] | 21-03-2024 |
| 45. | Personaje, caja_meta, espacio | - | [4][6][0] | [1][5][4] | 21-03-2024 |
| 46. | Personaje, caja_meta, meta | - | [2][6][0] | [6][5][4] | 21-03-2024 |
| 47. | Personaje_meta, espacio | Done | [4][5] | [5][4] | 21-03-2024 |
| 48. | Personaje_meta, meta | Done | [2][5] | [5][2] | 13-04-2024 |
| 49. | Personaje_meta, caja, espacio | - | [4][1][5] | [1][0][2] | 13-04-2024 |
| 50. | Personaje_meta, caja, meta | - | [2][1][5] | [6][0][2] | 13-04-2024 |
| 51. | Personaje_meta, caja_meta, espacio | - | [4][6][5] | [1][5][2] | 13-04-2024 |
| 52. | Personaje_meta, caja_meta, meta | - | [2][6][5] | [6][5][2] | 13-04-2024 |
### 6.6 Determina si se completo el nivel

Está función determina si todas las cajas estan en una meta, cuando esto sucede se debe cargar el siguiente nivel de juego.
| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | Done | 13-04-2024 |
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | - | - |

### 6.7 Funcion extra
Como parte del reto de programar un Sokoban, hay que agregar alguna función especial al juego, como por ejemplo bajo ciertas condiciones empujar 2 cajas, colocar un temporizador por nivel, etc.
| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | - | - |
