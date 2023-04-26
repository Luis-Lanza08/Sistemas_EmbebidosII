import RPi.GPIO as GPIO
import time

led = 3
pulsador = 7

def led_pulsador(bandera): # funcion que cambia el estado del led al pulsar 1 vez
	estados = GPIO.input(pulsador) 
	# se utiliza una variable bandera para detectar si el pulsador fue presionado
	if(estados == GPIO.LOW):
		bandera = not bandera
		time.sleep(0.04)
	if(bandera == True):
		GPIO.output(led, GPIO.HIGH)
		print("ON")
	if(bandera == False):
		GPIO.output(led, GPIO.LOW)
		print("OFF")
	return bandera
