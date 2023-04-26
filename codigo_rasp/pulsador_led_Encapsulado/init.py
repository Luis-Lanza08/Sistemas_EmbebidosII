import RPi.GPIO as GPIO

led = 3
pulsador = 7

# inicializar pines 3 y 7 para pulsador y para led
def inicializar():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(led, GPIO.OUT)
	GPIO.setup(pulsador, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	print('Pines Inicializados')
