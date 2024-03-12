import os

class Soko:
    

    def __init__(self):
        self.textura = {
            0: "🐥",
            1: "📦",
            2: "🚩",
            3: "🧱",
            4: "⬜",
        }
        self.mapa = [
            [3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,3],
            [3,4,0,4,4,4,2,4,4,3],
            [3,4,4,1,4,4,4,4,4,3,3,3,3,3,],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
        ]
        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimir_mapa(self):
        for fila in self.mapa:
            fila_textura = [self.textura[numero] for numero in fila]
            print(" ".join(fila_textura))

    def mover_personaje(self, nueva_columna, nueva_fila):
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[nueva_fila][nueva_columna] = 0
        self.personaje_columna = nueva_columna
        self.personaje_fila = nueva_fila

    def movimiento5(self):
        #mueve al personaje y la caja hacia abajo
        self.mapa[self.personaje_fila][self.personaje_columna]=4
        self.mapa[self.caja_fila][self.caja_columna]=0
        self.personaje_columna+=1
        self.caja_columna+=0
        self.mapa[self.caja_fila][self.caja_columna]=1

    def perso_caja(self):
        #verifica si el movimiento del personaje y la caja hacia abajo es valido
         if self.mapa[self.personaje_fila][self.personaje_columna]==0 and self.mapa[self.personaje_fila +1][self.personaje_columna]==4:
           self.mapa[self.personaje_fila+1][self.personaje_columna]==4 or self.mapa[self.personaje_fila+1][self.personaje_columna]==0
           self.moviminto5()

    def derecha(self):
        if self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
            self.mover_personaje(self.personaje_columna + 1, self.personaje_fila)

    def izquierda(self):
        if self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
            self.mover_personaje(self.personaje_columna - 1, self.personaje_fila)

    def arriba(self):
        if self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
            self.mover_personaje(self.personaje_columna, self.personaje_fila - 1)

    def abajo(self):
        if self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
            self.mover_personaje(self.personaje_columna, self.personaje_fila + 1)

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        self

    def jugar(self):
        while True:
            self.limpiar_pantalla()
            self.imprimir_mapa()
            movimiento = input("Selecciona el movimiento (a: izquierda, d: derecha, w: arriba, s: abajo): ")

            if movimiento == 'a':
                self.izquierda()
            elif movimiento == 'd':
                self.derecha()
            elif movimiento == 'w':
                self.arriba()
            elif movimiento == 's':
                self.abajo()
 
                

soko = Soko()
soko.jugar()


