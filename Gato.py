# -*- coding: utf-8 -*-
import os
import time
from random import randint
os.system("CLS")

class Juego():
	def gato(self):
		print("\nGato\n")

	def limpiarPantalla(self):
		os.system("CLS")

	def espacio(self):
		print('\n')

	def endGame(self,victorias_x,victorias_o,rondas):
		print("\n\nFin del Juego\n")
		msj_ganador = True
		print("Total de rondas:",rondas)
		
		if victorias_x > victorias_o:
			if victorias_o == 1:
				print("X ganó",victorias_x,"veces, mientras que O ganó",victorias_o,"vez")
			else:
				if victorias_x == 1:
					print("X ganó",victorias_x,"vez, mientras que O ganó",victorias_o,"veces")
				else:
					print("X ganó",victorias_x,"veces, mientras que O ganó",victorias_o,"veces")
			ganador = 'X'
		
		elif victorias_o > victorias_x:
			if victorias_x == 1:
				print("O ganó",victorias_o,"veces, mientras que X ganó",victorias_x,"vez")
			else:
				if victorias_o == 1:
				 print("O ganó",victorias_o,"vez, mientras que X ganó",victorias_x,"veces")
				else:
					print("O ganó",victorias_o,"veces, mientras que X ganó",victorias_x,"veces")
			ganador = 'O'
		
		else:
			if victorias_x > 1 or victorias_x == 0:
				msj = "X y O han empatado con " + str(victorias_x) + " victorias cada uno!"
				print (msj)
				msj_ganador = False
			else:
				msj = "X y O han empatado con " + str(victorias_x) + " victoria cada uno!"
				print (msj)
				msj_ganador = False
		
		if msj_ganador:
			msj = "Por ende, " + ganador + " ha ganado!"
			print (msj)
		input("\nPresiona la tecla Enter para cerrar el programa")

class Tablero(Juego):
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

	def revertirCambios(self,opcion):
		self.celdas[opcion] = ' '

	def victoria(self,jugador):
		opciones = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
		for combo in opciones:
			x,y,z = combo
			if self.celdas[x] == self.celdas[y] == self.celdas[z] == jugador:
				return True
		return False

	def reiniciarTablero(self):
		self.celdas = [" "," "," "," "," "," "," "," "," "," "]

	def valorValido(self,opcion):
		posibles_valores = [1,2,3,4,5,6,7,8,9]
		if opcion not in posibles_valores:
			return False
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
	
	def exportarCeldas(self):
		return self.celdas

class IA(Tablero):
	def __init__(self,jugador):
		self.jugador = jugador
		if jugador == 'X':
			self.enemigo = 'O'
		else:
			self.enemigo = 'X'
	
	def jugar(self,tablero,flow):
		celdas = tablero.exportarCeldas()
		msj = "Turno de la IA (" + self.jugador + "), por favor espere"
		print('\n' + msj)
		time.sleep(1)
		
		#el 5 es una celda que aumenta las posibilidades de la IA de no perder
		if tablero.valorValido(5) and flow:
			return 5

		##la IA bloqueará al oponente
		else:
			opciones = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
			for combo in opciones:
				x,y,z = combo
				if celdas[x] == celdas[y] == self.enemigo:
					if tablero.valorValido(z):
						return z

				elif celdas[x] == celdas[z] == self.enemigo:
					if tablero.valorValido(y):
						return y

				elif celdas[y] == celdas[z] == self.enemigo:
					if tablero.valorValido(x):
						return x
			
			##las esquinas son un punto estrategico que hay que proteger
			esquinas = [1,3,7,9]	
			for corner in esquinas:
				if tablero.valorValido(corner):
					return corner
			
			#si nada de lo anterior se ha activado, la IA eligirá una posición aleatoria
			casilla = randint(1,9)
			while tablero.valorValido(casilla) == False:
				casilla = randint(1,9)
			return casilla
	
	def evaluarVictoriaIA(self):
		for i in range(1,10):
			if tablero.valorValido(i):
				tablero.actualizarTablero(i,self.jugador)
				if tablero.victoria(self.jugador):
					tablero.revertirCambios(i)
					return i
				else:
					tablero.revertirCambios(i)
		return False

def continuar(eleccion):
	if eleccion.lower() == 'si' or eleccion.lower() == 'sí':
		return True
	return False

def setPantalla(tablero,eleccion,jugador):
	tablero.espacio()
	tablero.limpiarPantalla()
	tablero.gato()
	tablero.actualizarTablero(eleccion,jugador)

def evaluarVictoriaX(tablero,modoDeJuego):
	#determina si es que hay una victoria de X
	if tablero.victoria('X'):
		#victorias_x += 1
		tablero.crearTablero()
		print("\nFelicitaciones X, has ganado esta ronda!")
		if modoDeJuego == 1 or modoDeJuego == 2:
			seguir = input("¿Te gustaría seguir jugando? (si/no): ")
			if continuar(seguir):
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
			else:
				return 'finalizar'
		else:
			print("Iniciando nueva ronda...")
			time.sleep(2)
			if evaluarRondas(rondas + 1,lim_rondas):
				tablero.limpiarPantalla()
				tablero.gato()
				tablero.reiniciarTablero()
				tablero.crearTablero()
				return 'finalizar'
			else:
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
	else:
		return False

def evaluarEmpateX(tablero,modoDeJuego):
	#determinar si es que hay un empate en la partida
	if tablero.empate():
		tablero.crearTablero()
		print("\nX y O han empatado!")
		if modoDeJuego == 1 or modoDeJuego == 2:
			seguir = input("¿Te gustaría seguir jugando? (si/no): ")
			if continuar(seguir):
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
			else:
				return 'finalizar'
		else:
			print("Iniciando nueva ronda...")
			time.sleep(2)
			if evaluarRondas(rondas + 1,lim_rondas):
				tablero.limpiarPantalla()
				tablero.gato()
				tablero.reiniciarTablero()
				tablero.crearTablero()
				return 'finalizar'
			else:
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
	else:
		return False

def inicio_o(reinicio,tablero,flow,modoDeJuego,aiO,humanoO,Obot):
	if reinicio:
		tablero.gato()
	tablero.crearTablero()
	
	if modoDeJuego == 1 or humanoO:
		o_eleccion = int(input("\nTurno de O, elige una posición del 1 al 9: "))
		while tablero.valorValido(o_eleccion) == False:
			print("\nOpción Inválida. Intente de nuevo.")
			o_eleccion = int(input("Turno de O, elige una posición del 1 al 9: "))
	
	elif modoDeJuego == 2 and aiO:
		if aiO:
			o_eleccion = ai.jugar(tablero,flow)
			
			ia_move = ai.evaluarVictoriaIA()
			
			if ia_move:
				o_eleccion = ia_move

	elif modoDeJuego == 3:
		o_eleccion = Obot.jugar(tablero,flow)
			
		ia_move = Obot.evaluarVictoriaIA()
		if ia_move:
			o_eleccion = ia_move
	
	setPantalla(tablero,o_eleccion,'O')

def evaluarEmpateO(tablero,modoDeJuego):
	#determinar si es que hay un empate en la partida
	if tablero.empate():
		tablero.crearTablero()
		print("\nX y O han empatado!")
		if modoDeJuego == 1 or modoDeJuego == 2:
			seguir = input("¿Te gustaría seguir jugando? (si/no): ")
			if continuar(seguir):
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
			else:
				return 'finalizar'
		else:
			print("Iniciando nueva ronda...")
			time.sleep(2)
			if evaluarRondas(rondas + 1,lim_rondas):
				tablero.limpiarPantalla()
				tablero.gato()
				tablero.reiniciarTablero()
				tablero.crearTablero()
				return 'finalizar'
			else:
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
	else:
		return 'activar Flag'

def evaluarVictoriaO(tablero,modoDeJuego):
	#determina si es que hay una victoria de O
	if tablero.victoria('O'):
		tablero.crearTablero()
		print("\nFelicitaciones O, has ganado esta ronda!")
		if modoDeJuego == 1 or modoDeJuego == 2:
			seguir = input("¿Te gustaría seguir jugando? (si/no): ")
			if continuar(seguir):
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
			else:
				return 'finalizar'
		else:
			print("Iniciando nueva ronda...")
			time.sleep(2)
			if evaluarRondas(rondas + 1,lim_rondas):
				tablero.limpiarPantalla()
				tablero.gato()
				tablero.reiniciarTablero()
				tablero.crearTablero()
				return 'finalizar'
			else:
				tablero.reiniciarTablero()
				tablero.limpiarPantalla()
				return 'seguir'
	else:
		return 'activar Flag'

def menu(tablero):
	print("\n\nBienvenido a gato!\n\n")
	print("Modos de juego:\n")
	print("1) Jugar contra otra persona")
	print("2) Jugar contra la IA")
	print("3) Batalla de las IAs\n")
	decision = int(input("Por favor, elige una opción: "))
	
	while decision != 1 and decision != 2 and decision != 3:
		print("\nOpción Inválida. Intente de nuevo")
		decision = int(input("Por favor, elige una opción: "))
	
	if decision == 2:
		letra = input("Escoja que letra desea ocupar (X/O): ")
		n_rondas = float("inf")
		
		while letra.upper() != 'X' and letra.upper() != 'O' and letra.upper() != '0':
			print("\nOpción Inválida. Intente de nuevo")
			letra = input("Escoja que letra desea ocupar (X/O): ")
		
		if letra.upper() == 'X':
			player = 'X'
		else:
			player = 'O'
	else:
		player = ''
		n_rondas = float("inf")
		if decision == 3:
			n_rondas = int(input("Ingrese el numero de rondas que quiere observar: "))
			while n_rondas <= 0:
				print("\nOpción Inválida. Intente de nuevo")
				n_rondas = int(input("Ingrese el numero de rondas que quiere observar: "))

	return decision,player,n_rondas

def evaluarRondas(rondas,lim_rondas):
	if rondas == lim_rondas:
		return True
	return False

tablero = Tablero()
victorias_x = 0
victorias_o = 0
rondas = 0
flow = False
aiX = False
aiO = False
humanoX = True
humanoO = True
Xbot = ''
Obot = ''


modoDeJuego,player,lim_rondas = menu(tablero)
if player == 'X':
	ai = IA('O')
	aiO = True
	humanoO = False
elif player == 'O':
	ai = IA('X')
	aiX = True
	humanoX = False

if modoDeJuego == 3:
	humanoX = False
	humanoO = False
	aiX = True
	aiO = True
	Xbot = IA('X')
	Obot = IA('O')

while True and rondas < lim_rondas:

	#esta Flag hace que la transición al agregar una O se vea visualmente mejor
	reinicio = False
	Flag = False
	saltar = False
	revertirFlow = False
	transicion = True
	
	tablero.limpiarPantalla()
	tablero.gato()
	tablero.crearTablero()
	
	#turno de X
	if modoDeJuego == 1 or humanoX:
		x_eleccion = int(input("\nTurno de X, elige una posición del 1 al 9: "))
		while tablero.valorValido(x_eleccion) == False:
			print("\nOpción Inválida. Intente de nuevo.")
			x_eleccion = int(input("Turno de X, elige una posición del 1 al 9: "))
	
	elif aiX and modoDeJuego == 2:
		if rondas % 2 != 0:
			flow = True
			revertirFlow = True
		
		x_eleccion = ai.jugar(tablero,flow)

		if revertirFlow:
			flow = False
			
			ia_move = ai.evaluarVictoriaIA()
			if ia_move:
				x_eleccion = ia_move

	elif modoDeJuego == 3:
		if rondas % 2 != 0:
			flow = True
			revertirFlow = True
		x_eleccion = Xbot.jugar(tablero,flow)

		if revertirFlow:
			flow = False
			
		ia_move = Xbot.evaluarVictoriaIA()
		if ia_move:
			x_eleccion = ia_move
	
	setPantalla(tablero,x_eleccion,'X')
	
	victoriaX = evaluarVictoriaX(tablero,modoDeJuego)
	
	#determinar si X ganó la ronda
	if victoriaX == 'seguir':
		victorias_x += 1
		reinicio = True
		rondas += 1
		saltar = True
		if evaluarRondas(rondas,lim_rondas):
			Flag = True
	
	elif victoriaX == 'finalizar':
		rondas += 1
		victorias_x += 1
		break
	
	#determinar si es que hay un empate en la partida
	empateX = evaluarEmpateX(tablero,modoDeJuego)

	if empateX == 'seguir':
		reinicio = True
		rondas += 1
		if evaluarRondas(rondas,lim_rondas):
			Flag = True
	elif empateX == 'finalizar':
		rondas += 1
		break

	#flow determina quién debe partir en la próxima ronda
	#saltar permite no repetir el turno de O
	#si flow = True, parte X, de lo contrario parte O
	if rondas % 2 == 0:
		flow = True
	else:
		flow = False
	
	#turno de O
	if saltar and flow:
		pass
	else:
		inicio_o(reinicio,tablero,flow,modoDeJuego,aiO,humanoO,Obot)

		#determinar si es que hay un empate en la partida
		empateO = evaluarEmpateO(tablero,modoDeJuego)
		
		if empateO == 'seguir':
			rondas += 1
			Flag = False
			transicion = False
			pass

		elif empateO == 'finalizar':
			rondas += 1
			break
		else:
			Flag = True


		#determina si es que hay una victoria de O
		victoriaO = evaluarVictoriaO(tablero,modoDeJuego)

		if victoriaO == 'seguir':
			victorias_o += 1
			reinicio = True
			transicion = False
			rondas += 1
			
			if rondas % 2 != 0:
				
			
				inicio_o(reinicio,tablero,rondas,modoDeJuego,aiO,humanoO,Obot)
				
				#determinar si es que hay un empate en la partida
				empateO = evaluarEmpateO(tablero,modoDeJuego)
				
				if empateO == 'seguir':
					rondas += 1
					Flag = False
					transicion = False
					pass

				elif empateO == 'finalizar':
					rondas += 1
					break
				else:
					Flag = True

				#determina si es que hay una victoria de O
				victoriaO = evaluarVictoriaO(tablero,modoDeJuego)

				if victoriaO == 'seguir':
					victorias_o += 1
					rondas += 1
					transicion = False
					pass

				elif victoriaO == 'finalizar':
					victorias_o += 1
					rondas += 1
					break
				else:
					Flag = True

		elif victoriaO == 'finalizar':
			victorias_o += 1
			rondas += 1
			break
		else:
			Flag = True

	if evaluarRondas(rondas,lim_rondas):
		tablero.gato()
		Flag = True
	
	if Flag and transicion:
		tablero.crearTablero()
	
tablero.endGame(victorias_x,victorias_o,rondas)