import random
import os
from ascii_magic import AsciiArt
import pyfiglet


logo = AsciiArt.from_image("LOGO.png")
logo.to_terminal(columns=80,width_ratio=2.5)

text = pyfiglet.print_figlet(text=" GAME_ AHORCADO",colors="RED")
Nombre = pyfiglet.print_figlet(text="BY DANIEL LOPEZ",colors="BLUE")

inciar =(input("INICIAR EL JUEGO, ESCRIBIR S/N : "))
if inciar == "S":
   os.system("cls")

def run():
 
 try:
   
  with open (r"C:\Users\Usuario\OneDrive\Escritorio\CURSOS\PYTHON INTERMEDIO\PROYECTOFINAL\datos.txt","r",encoding="utf-8") as f:
    

    #EXTRAER PALABRA
    palabras = list(f)
    aleatorio = random.choice(palabras).strip().replace("Ã³","o").replace("Ã¡","a").replace("Ã©","e").replace("Ã","i").replace("Ãº","u")   #"EXTRAER PALABRA ALEATORIA DEL ARCHIVO"
      
    
    # DEFINIR CANTIDAD DE CARACTERES
    pista = ["_"]*len(aleatorio)
    

    print("".join(pista))
    
    # ENUMERAR LETRAS DE LA PALBRA
    fallas = 0
    
    
  while "".join(pista) != aleatorio.upper():
     ingresaletra =  (input ("ADIVINA LA PALABRA MARICON Y SI PIERDES MORIRAS :  ")).upper()
     
     

     for i in range(len(aleatorio)):
       if ingresaletra.upper() == aleatorio[i].upper():
        pista[i]= ingresaletra
       if "".join(pista) == aleatorio.upper():
         print(" GANASTE, EXCELENTE PARTIDA AMIGO")   
         break
     if ingresaletra.upper() not in aleatorio.upper():
        fallas += 1

     print (pista)
     print("".join(pista)).__str__
     print(fallas)
  
     if fallas == 1:
         print( """
     
       +---+
       |   |
           |
           |  LETRA EQUIVOCADA, SIGUE INTENTADO
           |
           |
     =========
     """)

     if fallas == 2:
       print( """
     
       +---+
       |   |
       O   |
           |  OJO, NO TE EQUIVOQUES TANTO
           |
           |
     =========
     """)
      
     if fallas == 3:
   
       print( """
     
       +---+
       |   |
       O   |
       |   |   JMMM, POR POCO..
           |
           |
     =========
     """)
     
     if fallas == 4:
   
       print( """
     
       +---+
       |   |
       O   |
      /|   |   TE ACERCAS MAS A LA DERROTA, QUE A LA VICTORIA...
           |
           |
     =========
     """)
     
     if fallas == 5:
   
       print( """
     
       +---+
       |   |
       O   |
      /|\  |   PORTATE SERIO....
           |
           |
     =========
     """)
       
     if fallas == 6:
   
       print( """
     
       +---+
       |   |
       O   |
      /|\  |   IMAGINATE QUE ERES TU EL QUE ESTA COLGADO, TE FALTA UNA PIERNA AMIGO
      /    |
           |
     =========
     """)
       
     if fallas == 7:
     
       print( "PERDISTE CAMPEON, LARGATE DE AQUI")
       print("LA PALBRA ERA" +" " + aleatorio.upper())
       break
 

 except FileNotFoundError:
  return None
 


if __name__ == "__main__":
 run()


