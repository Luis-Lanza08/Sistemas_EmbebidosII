import funciones as fun
import RPi.GPIO as GPIO
import init
import time

init.inicializar() 	# funcion para inicializar pines
bandera = False

while(1):
	fun.led_pulsador(bandera) # se llama a la funcion para prender el led