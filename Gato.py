import os
os.system("CLS")


class Tablero():
	def __init__(self):
		self.celdas = [" "," "," "," "," "," "," "," "," "," "]

	def crearTablero(self):
		linea = "{} | {} | {}"
		print(linea.format('  ' + self.celdas[1],self.celdas[2],self.celdas[3]))
		print("-------------")
		print(linea.format('  ' + self.celdas[4],self.celdas[5],self.celdas[6]))
		print("-------------")
		print(linea.format('  ' + self.celdas[7],self.celdas[8],self.celdas[9]))

	def actualizarTablero(self,opcion,jugador):
		#jugador puede ser X o O
		if self.celdas[opcion] == ' ':
			self.celdas[opcion] = jugador

	def victoria(self,jugador):
		opciones = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
		for combo in opciones:
			x,y,z = combo
			if self.celdas[x] == self.celdas[y] == self.celdas[z] == jugador:
				return True

	def reiniciarTablero(self):
		self.celdas = [" "," "," "," "," "," "," "," "," "," "]

	def valorValido(self,opcion):
		if self.celdas[opcion] == ' ':
			return True
		return False

	def empate(self):
		celdas_ocupadas = 0
		for celda in self.celdas:
			if celda != ' ':
				celdas_ocupadas += 1
		if celdas_ocupadas == 9:
			return True
		return False


def gato():
	print("\nGato\n")

def limpiarPantalla():
	os.system("CLS")

def espacio():
	print('\n')

def continuar(eleccion):
	if eleccion.lower() == 'si' or eleccion.lower() == 'sí':
		return True
	return False

def endGame():
	print("\n\nFin del Juego\n")
	if victorias_x > victorias_o:
		print("X ganó",victorias_x,"veces, mientras que O ganó",victorias_o,"veces")
		ganador = 'X'
	elif victorias_o > victorias_x:
		print("O ganó",victorias_o,"veces, mientras que X ganó",victorias_x,"veces")
		ganador = 'O'
	else:
		if victorias_x > 1:
			msj = "X y O han empatado con " + str(victorias_x) + " victorias cada uno!"
			return msj
		else:
			msj = "X y O han empatado con " + str(victorias_x) + " victoria cada uno!"
			return msj
	msj = "Por ende, " + ganador + " ha ganado!"
	return msj

tablero = Tablero()
posibles_valores = [1,2,3,4,5,6,7,8,9]
victorias_x = 0
victorias_o = 0

while True:
	
	#esta Flag hace que la transición al agregar una O se vea visualmente mejor
	reinicio = False
	Flag = False
	
	limpiarPantalla()
	gato()
	tablero.crearTablero()
	
	x_eleccion = int(input("\nTurno de X, elige una posición del 1 al 9: "))
	while x_eleccion not in posibles_valores or tablero.valorValido(x_eleccion) == False:
		print("\nOpción Inválida. Intente de nuevo.")
		x_eleccion = int(input("Turno de X, elige una posición del 1 al 9: "))
	
	espacio()
	limpiarPantalla()
	gato()
	tablero.actualizarTablero(x_eleccion,'X')
	
	#determina si es que hay una victoria de X
	if tablero.victoria('X'):
		victorias_x += 1
		tablero.crearTablero()
		print("\nFelicitaciones X, has ganado esta ronda!")
		seguir = input("¿Te gustaría seguir jugando? (si/no): ")
		if continuar(seguir):
			tablero.reiniciarTablero()
			limpiarPantalla()
			reinicio = True	
		else:
			break
	
	#determinar si es que hay un empate en la partida
	if tablero.empate():
		tablero.crearTablero()
		print("\nX y O han empatado!")
		seguir = input("¿Te gustaría seguir jugando? (si/no): ")
		if continuar(seguir):
			tablero.reiniciarTablero()
			limpiarPantalla()
			reinicio = True
		else:
			break
	
	if reinicio:
		gato()
	tablero.crearTablero()
	
	o_eleccion = int(input("\nTurno de O, elige una posición del 1 al 9: "))
	while o_eleccion not in posibles_valores or tablero.valorValido(o_eleccion) == False:
		print("\nOpción Inválida. Intente de nuevo.")
		o_eleccion = int(input("Turno de O, elige una posición del 1 al 9: "))
	
	espacio()
	limpiarPantalla()
	gato()
	tablero.actualizarTablero(o_eleccion,'O')

	#determinar si es que hay un empate en la partida
	if tablero.empate():
		tablero.crearTablero()
		print("\nX y O han empatado!")
		seguir = input("¿Te gustaría seguir jugando? (si/no): ")
		if continuar(seguir):
			tablero.reiniciarTablero()
			limpiarPantalla()
		else:
			break
	else:
		Flag = True

	#determina si es que hay una victoria de O
	if tablero.victoria('O'):
		tablero.crearTablero()
		victorias_o += 1
		print("\nFelicitaciones O, has ganado esta ronda!")
		seguir = input("¿Te gustaría seguir jugando? (si/no): ")
		if continuar(seguir):
			tablero.reiniciarTablero()
			limpiarPantalla()
		else:
			break
	else:
		Flag = True

	if Flag:
		tablero.crearTablero()

print(endGame())
input("\nPresiona la tecla Enter para cerrar el programa")