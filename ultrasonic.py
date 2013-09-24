import RPi.GPIO as GPIO 	## Import GPIO library
import time 			## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) 	## Use board pin numbering

	# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print "Ultrasonic Measurement"

for num in range(10,200):			
		# Set pins as output and input	
	GPIO.setup(GPIO_TRIGGER,GPIO.OUT)	# Trigger
	GPIO.setup(GPIO_ECHO,GPIO.IN)		# Echo
	
	GPIO.output(GPIO_TRIGGER, False)	# Set trigger to False (Low)
	
	time.sleep(0.5)				# Allow module to settle
		
	GPIO.output(GPIO_TRIGGER, True)		# Send 10us pulse to trigger
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	
	while GPIO.input(GPIO_ECHO)==0:
	  start = time.time()
	
	while GPIO.input(GPIO_ECHO)==1:
	  stop = time.time()
	
	elapsed = stop-start			# Calculate pulse length
	
		# Distance pulse travelled in that time is time
		# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34300
	
	distance = distance / 2			# Calculate pulse length
	
	print "Distance : %.1f" % distance

GPIO.cleanup()					# Reset GPIO settings