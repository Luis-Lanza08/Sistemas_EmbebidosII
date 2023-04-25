import RPi.GPIO as GPIO
import time
def led_pulsador(bandera) #funcion que cambia el estado del led al pulsar 1 vez
	estados = GPIO.inpurt(7)
	print(bandera)
	# se utiliza una variable bandera para detectar si el pulsador fue presionado
	if(estados == 0):
		bandera = not bandera
	if(bandera):
		GPIO.output(3, GPIO.HIGH)
		print("ON")
	else:
		GPIO.output(3, GPIO.LOW)
		print("OFF")