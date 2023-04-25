import RPi.GPIO as GPIO
#inicializar pines 3 y 7 para pulsador y para led
def inicializar():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3, GPIO.OUT)
	GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	print('Pines Inicializados')