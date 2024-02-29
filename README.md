# Sokoba
## 0. Objetivo 

programar el juego de sokoba en una version retro para consola.

## 1. Reglas del juego

El juego sokoba consiste en acomodar cajas en puntos determinados por las metas.

1. El personaje se puede mover hacia arriba, abajo , izquierda y derecha.
2. El personaje solo puede empujar 1 caja en cualquier sentido.
3. El personae se movera en un mapa predefinido.
4. Para terminar el nivel se tiene que acomodar todas las cajas sobre las metas.

## 2. Elementos del juego

### 2.0  Mapa del juego

Cada nivel del juego se colocara dentro de un array bidimencional, colocando números para representar elementos de juego, a continuacion se tiene un ejemplo basico de nivel.

Mapa=[3,4,4,0,4,4,3]

## 2.1 lista elementos del juego

0. Personaje
1. Caja
2. Metas
3. Pared
4. Piso
5. Personaje-meta
6. Caja-meta

## 3. Controles 
- a=Izquierda
- d=Derecha
- w=Arriba
- s=Abajo

### 4.Lista de movimientos

 | No. | Sentido | Movimiento | Inicio | Fin | Fecha  |
 | --- | ------- | ---------- | ------ | --- | ------ |
 | 1 | derecha | personaje, piso | [0,4] | [4,0] | Succesfull |
 | 2 | izquierda | piso, personaje | [4,0] | [0,4] | Succesfull |
