import funciones as fun
import RPi.GPIO as GPIO
import init
import time

init.inicializar() 	# funcion para inicializar pines
bandera = False

led = 3
pulsador = 7

while(1):
	bandera = fun.led_pulsador(bandera) # se llama a la funcion para prender el led y se actualiza bandera
	print(bandera)
	
