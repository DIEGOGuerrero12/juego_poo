import os
class Soko:
    pasos=0


    def __init__(self):
        self.textura = {
            0: "🚗",
            1: "📦",
            2: "⛪",
            3: "🟥",
            4: "  ",
            5: "🔴",
            6: "⚪",
            7: " ",
        }
        self.mapa = [
            [7,7,3,3,3,3,3,3,3,4,3,3],
            [7,3,4,4,4,1,4,4,2,4,4,3],
            [7,3,0,4,4,4,4,4,4,4,4,3],
            [3,3,3,1,4,4,4,4,4,4,3,7],
            [3,2,4,4,4,4,1,4,4,4,4,3],
            [3,4,4,4,4,4,4,2,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3],
        ]

 

        self.personaje_columna = 2
        self.personaje_fila = 2

    def imprimir_mapa(self):
        for fila in self.mapa:
            file_textura= [self.textura[numero] for numero in fila]
            print(" ".join(file_textura))

    def selecion(self):
        self.mapa=self.mapa
        



        
    def derecha(self): # todos los movimientos derecha
         if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
              self.movimiento_derecha() # Movimiento del lado derecho
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
              self.meter_la_caja_a_la_meta_derecha() # el personaje enpuja la caja y entra a la meta a la derecha
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
              self.sacar_caja_meta_derecha() # el personaje enpuja la caja y sale a un espacio en blanco a la derecha
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
              self.sacar_caja_si_hay_espacio_blanco_derecha() # el personaje enpuja la caja y sale a un espacio en blanco a la derecha si el personaje esta en un espacio en blanco
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
              self.espacio_en_blanco_meter_caja_a_la_meta_derecha() # si el personaje esta en la meta, una caja en un espacio en blanco y una meta a la derecha, entra a la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
              self.mover_caja_derecha() # si hay una caja a la derecha se cumple esta condicion y se ejecuta el codigo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6:
              self.mover_la_caja_en_la_meta_derecha() # el personaje puede mover la caja-meta en la meta a la derecha
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.mover_caja_derecha_meta() # el personaje puede entrar a la meta y empujar la caja-meta a un espacio en la meta hacia la derecha
         
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
              self.meta_derecha() # entra el personaje a la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2:
              self.personaje_meta_derecha() # el personaje se mueve a la derecha en la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
              self.meta_afuera_derecha()# el personaje puede salir de la meta a la derecha
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
              self.mover_caja_per_meta_derecha() #el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia la derecha
        
        
    def izquierda(self): # todos los movimientos izquierda
         if self.mapa[self.personaje_fila][self.personaje_columna -1] == 4 and self.mapa[self.personaje_fila][self.personaje_columna] == 0:
              self.movimiento_izquierda() # movimiento a la izquierda
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
              self.meter_la_caja_a_la_meta_izquierda() # el personaje enpuja la caja y entra a la meta a la izquierda
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
              self.sacar_caja_meta_izquierda() # el personaje enpuja la caja y sale a un espacio en blanco a la izquierda
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
              self.sacar_caja_si_hay_espacio_blanco_izquierda() # el personaje enpuja la caja y sale a un espacio en blanco a la izquierda si el personaje esta en un espacio en blanco
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
              self.espacio_en_blanco_meter_caja_a_la_meta_izquierda() # si el personaje esta en la meta, una caja en un espacio en blanco y una meta a la izquierda, entra a la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1:
              self.mover_caja_izquierda() # si hay una caja del lado izquierdo se ejecuta este bloque de codigo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6:
              self.mover_la_caja_en_la_meta_izquierda() # el personaje puede mover la caja-meta en la meta a la izquierda
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
              self.mover_caja_izquierda_meta() # el personaje puede entrar a la meta y empujar la caja-meta a un espacio en la meta hacia la izquierda
         
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
              self.meta_izquierda() # el personaje entra a la meta del lado izquierdo
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2:
              self.personaje_meta_izquierda() #el personaje se mueve a la izquierda en la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
              self.meta_afuera_izquierda() # el personaje puede salir afuera de la meta del lado izquierdo
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1:
              self.mover_caja_per_meta_izquierda() #el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia la izquierda
            
        
    def arriba(self): # todos los movimientos arriba
         if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
              self.movimiento_arriba() # se mueve hacia arriba si hay espacio
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
              self.meter_la_caja_a_la_meta_arriba() # el personaje enpuja la caja y entra a la meta arriba
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
              self.sacar_caja_meta_arriba() # el personaje enpuja la caja y sale a un espacio en blanco hacia arriba
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
              self.sacar_caja_si_hay_espacio_blanco_arriba() # el personaje enpuja la caja y sale a un espacio en blanco hacia arriba si el personaje esta en un espacio en blanco
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
              self.espacio_en_blanco_meter_caja_a_la_meta_arriba() # si el personaje esta en la meta, una caja en un espacio en blanco y una meta hacia arriba, entra a la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1:
              self.mover_caja_arriba() # si hay una caja arriba del personaje se ejecuta este bloque de codigo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6:
              self.mover_la_caja_en_la_meta_arriba() # el personaje mueve la caja*meta en la meta hacia arriba
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
              self.mover_caja_arriba_meta() # el personaje puede entrar a la meta y empujar la caja-meta a un espacio en la meta hacia arriba
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
              self.meta_arriba() # el personaje entra a la meta hacia arriba
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2:
              self.personaje_meta_arriba() # el personaje se mueve hacia arriba en la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4:
              self.meta_afuera_arriba() # el personaje puede salir de la meta del lado de arriba
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1:
              self.mover_caja_per_meta_arriba() # el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia arriba
        
        
    def abajo(self): # todos los movimientos abajo
         if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
             self.movimiento_abajo() # se mueve hacia abajo si hay espacio
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2 ][self.personaje_columna] == 2:
              self.meter_la_caja_a_la_meta_abajo() # el personaje enpuja la caja y entra a la meta abajo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
              self.sacar_caja_meta_abajo() # el personaje enpuja la caja y sale a un espacio en blanco hacia abajo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
              self.sacar_caja_si_hay_espacio_blanco_abajo() # el personaje enpuja la caja y sale a un espacio en blanco hacia abajo si el personaje esta en un espacio en blanco
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
              self.espacio_en_blanco_meter_caja_a_la_meta_abajo() # si el personaje esta en la meta, una caja en un espacio en blanco y una meta hacia abajo, entra a la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1:
              self.mover_caja_abajo() # si hay una caja debajo del personaje se ejecuta este bloque de codigo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6:
              self.mover_la_caja_en_la_meta_abajo() # el personaje mueve la caja-meta en la meta hacia abajo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6 and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
              self.mover_caja_abajo_meta() # el personaje puede entrar a la meta y empujar la caja-meta a un espacio en la meta hacia abajo
        
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
              self.meta_abajo() # entra a la meta del lado de abajo
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2:
              self.personaje_meta_abajo() # se mueve hacia abajo en la meta
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4:
              self.meta_afuera_abajo() # el personaje puede salir de la meta del lado de abajo
            
         elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1:
              self.mover_caja_per_meta_abajo()# el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia abajo
            
            
    
    # movimientos derecha, izquierda, arriba y abajo
        
    def movimiento_derecha(self): # derecha
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0 
        self.personaje_columna+=1
        self.pasos+=1
    def movimiento_izquierda(self): # izquierda
        self.mapa[self.personaje_fila][self.personaje_columna -1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.personaje_columna-=1
        self.pasos+=1
    def movimiento_arriba(self):# arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila -= 1
        self.pasos+=1
    def movimiento_abajo(self): # abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila += 1
        self.pasos+=1
            
            
            
        # mover caja a un espacio en blanco 
        
    def mover_caja_derecha(self):
         if self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.movimiento_derecha()
            self.pasos+=1
    def mover_caja_izquierda(self):
         if self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.movimiento_izquierda()
            self.pasos+=1
    def mover_caja_arriba(self):
         if self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.movimiento_arriba()
            self.pasos+=1
    def mover_caja_abajo(self):
         if self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.movimiento_abajo()
            self.pasos+=1
            
            
        # movimiento del personaje en la meta
        
    def personaje_meta_derecha(self):# se mueve el personaje a la derecha en la meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.personaje_columna+=1
        self.pasos+=1
    def personaje_meta_izquierda(self): #se mueve el personaje a la izquierda en la meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.personaje_columna-=1
        self.pasos+=1
    def personaje_meta_arriba(self): # el personaje puede moverse hacia arriba en la meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila-=1
        self.pasos+=1
    def personaje_meta_abajo(self): # el personaje puede moverse hacia abajo en la meta
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila+=1
        self.pasos+=1
        
        
        
        # el personaje entra a la meta
        
    def meta_derecha(self): # el personaje entra a la meta del lado derecho
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.personaje_columna+=1
        self.pasos+=1
    def meta_izquierda(self): # el personaje entra a la meta del lado izquierdo
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.personaje_columna-=1
        self.pasos+=1
    def meta_arriba(self): # el personaje entra a la meta del lado de arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.personaje_fila-=1
        self.pasos+=1
    def meta_abajo(self): # el personaje entra a la meta del lado de abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.personaje_fila+=1
        self.pasos+=1
        
        
        
        # el personaje sale de la meta
        
    def meta_afuera_derecha(self):# el personaje es capaz de salir de la meta del lado derecho
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.personaje_columna+=1
        self.pasos+=1
    def meta_afuera_izquierda(self):# el personaje es capaz de salir de la meta del lado izquierdo
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.personaje_columna-=1
        self.pasos+=1
    def meta_afuera_arriba(self): # el personaje es capaz de salir de la meta del lado de arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.personaje_fila-=1
        self.pasos+=1
    def meta_afuera_abajo(self): # el personaje es capaz de salir de la meta del lado de abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.personaje_fila+=1
        self.pasos+=1
        
          
        # mover la caja a un espacio en blanco si esta en la meta
        
    def mover_caja_per_meta_derecha(self): #el personaje puede mover la caja a un espacio en blanco si esta en la meta del lado hacia la derecha
        if self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
            self.meta_afuera_derecha()
            self.pasos+=1
    def mover_caja_per_meta_izquierda(self): #el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia la izquierdo
        if self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4:
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
            self.meta_afuera_izquierda()
            self.pasos+=1
    def mover_caja_per_meta_arriba(self): # el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia arriba
        if self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
            self.meta_afuera_arriba()
            self.pasos+=1
    def mover_caja_per_meta_abajo(self): # el personaje puede mover la caja a un espacio en blanco si esta en la meta hacia abajo
        if self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4:
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
            self.meta_afuera_abajo()
            self.pasos+=1
        
        
        # meter la caja a la meta
        
    def meter_la_caja_a_la_meta_derecha(self): # el personaje puede empujar una caja y meterla a la meta a la derecha
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6 
        self.personaje_columna+=1
        self.pasos+=1
    def meter_la_caja_a_la_meta_izquierda(self): # el personaje puede empujar una caja y meterla a la meta a la izquierda
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6 
        self.personaje_columna-=1
        self.pasos+=1
    def meter_la_caja_a_la_meta_arriba(self): # el personaje puede empujar una caja y meterla a la meta arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6 
        self.personaje_fila-=1
        self.pasos+=1
    def meter_la_caja_a_la_meta_abajo(self): # el personaje puede empujar una caja y meterla a la meta abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6 
        self.personaje_fila+=1
        self.pasos+=1
    
    # mover la caja a un espacio de la meta para que entre el personaje
    
    def mover_caja_derecha_meta(self): # el personaje puede empujar la caja-meta a un espacio en la meta y el personaje puede entrar hacia la derecha
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.meta_derecha()
        self.pasos+=1
    def mover_caja_izquierda_meta(self): # el personaje puede empujar la caja-meta a un espacio en la meta y el personaje puede entrar hacia la izquierda
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.meta_izquierda()
        self.pasos+=1
    def mover_caja_arriba_meta(self): # el personaje puede empujar la caja-meta a un espacio en la meta y el personaje puede entrar hacia arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.meta_arriba()
        self.pasos+=1
    def mover_caja_abajo_meta(self): # el personaje puede empujar la caja-meta a un espacio en la meta y el personaje puede entrar hacia abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.meta_abajo()
        self.pasos+=1
    
    # mover la caja-meta en la meta
    
    def mover_la_caja_en_la_meta_derecha(self): # el personaje mueve la caja-meta en la meta a la derecha
         if self.mapa[self.personaje_fila][self.personaje_columna + 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_meta_derecha()
            self.pasos+=1
            
            
    def mover_la_caja_en_la_meta_izquierda(self): # el personaje mueve la caja-meta en la meta a la izquierda
        if self.mapa[self.personaje_fila][self.personaje_columna - 2] == 2:
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_meta_izquierda()
            self.pasos+=1
            
    def mover_la_caja_en_la_meta_arriba(self): # el personaje mueve la caja-meta en la meta hacia arriba
        if self.mapa[self.personaje_fila - 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_meta_arriba()
            self.pasos+=1
            
            
    def mover_la_caja_en_la_meta_abajo(self): # el personaje mueve la caja-meta en la meta hacia abajo
        if self.mapa[self.personaje_fila + 2][self.personaje_columna] == 2:
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_meta_abajo()
            self.pasos+=1
            
            
    
    # sacar la caja-meta a un espacio en blanco
    
    def sacar_caja_meta_derecha(self): # el personaje puede sacar la caja de la meta hacia la derecha
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.personaje_columna+=1
        self.pasos+=1
    def sacar_caja_meta_izquierda(self): # el personaje puede sacar la caja de la meta hacia la izquierda
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.personaje_columna-=1
        self.pasos+=1
    def sacar_caja_meta_arriba(self): # el personaje puede sacar la caja de la meta hacia arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.personaje_fila-=1
        self.pasos+=1
    def sacar_caja_meta_abajo(self): # el personaje puede sacar la caja de la meta hacia abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.personaje_fila+=1
        self.pasos+=1
    
    # sacar la caja-meta si el personaje esta en un espacio en blanco y enfrente de la caja tambien un espacio en blanco
    
    def sacar_caja_si_hay_espacio_blanco_derecha(self): # si el personaje esta en un espacio en blanco y la caja-meta en la meta la mueve a un espacio en blanco a la derecha
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 1
        self.meta_derecha()
        self.pasos+=1
    def sacar_caja_si_hay_espacio_blanco_izquierda(self): # si el personaje esta en un espacio en blanco y la caja-meta en la meta la mueve a un espacio en blanco a la izquierda
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 1
        self.meta_izquierda()
        self.pasos+=1
    def sacar_caja_si_hay_espacio_blanco_arriba(self): # si el personaje esta en un espacio en blanco y la caja-meta en la meta la mueve a un espacio en blanco hacia arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 1
        self.meta_arriba()
        self.pasos+=1
    def sacar_caja_si_hay_espacio_blanco_abajo(self): # si el personaje esta en un espacio en blanco y la caja-meta en la meta la mueve a un espacio en blanco hacia abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 2
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 1
        self.meta_abajo()
        self.pasos+=1
    
    # meter la caja a la meta si el personaje esta en la meta y la caja en un espacio en blanco
    
    def espacio_en_blanco_meter_caja_a_la_meta_derecha(self): # si el personaje esta en la meta, la caja en un espacio en blanco y despues la meta entra la caja a la derecha 
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
        self.meta_afuera_derecha()
        self.pasos+=1
    def espacio_en_blanco_meter_caja_a_la_meta_izquierda(self): # si el personaje esta en la meta, la caja en un espacio en blanco y despues la meta entra la caja a la izquierda
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
        self.meta_afuera_izquierda()
        self.pasos+=1
    def espacio_en_blanco_meter_caja_a_la_meta_arriba(self): # si el personaje esta en la meta, la caja en un espacio en blanco y despues la meta entra la caja hacia arriba
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
        self.meta_afuera_arriba()
        self.pasos+=1
    def espacio_en_blanco_meter_caja_a_la_meta_abajo(self): # si el personaje esta en la meta, la caja en un espacio en blanco y despues la meta entra la caja hacia abajo
        self.mapa[self.personaje_fila][self.personaje_columna] = 4
        self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
        self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
        self.meta_afuera_abajo()
        self.pasos+=1
    
    def juego_terminado(self):
        if self.contar_cajas()==0:
            print("juego terminado")

    def pasos2(self):
        print(f"pasos",self.pasos )
    


    def contar_cajas(self):
        cajas = 0
        for fila in self.mapa:
            for columna in fila:
                if columna ==1:
                    cajas += 1
        print("numero de cajas:",cajas)
        return cajas
    

    def jugar(self):
        while True:
            self.imprimir_mapa() 
            self.pasos2()
            self.juego_terminado()
            movimiento = input("Selecciona el movimiento (a: izquierda, d: derecha, w: arriba, s: abajo):")
            if movimiento == 'a':
                self.izquierda()
            elif movimiento == 'd':
                self.derecha()
            elif movimiento == 'w':
                self.arriba()
            elif movimiento == 's':
                self.abajo()
            
 
soko=Soko()
soko.jugar()