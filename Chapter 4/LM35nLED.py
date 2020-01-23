import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.GPIO as GPIO
import time

RedLED = "P8_19"
GreenLED = "P8_13"
GPIO.setup(RedLED, GPIO.OUT)
GPIO.setup(GreenLED, GPIO.OUT)
GPIO.output(RedLED, GPIO.LOW)
GPIO.output(GreenLED, GPIO.LOW)

ADC.setup()

try:	
    while True:
        reading = ADC.read('P9_40')
        millivolts = reading * 1800  
        temp_c = (millivolts - 500) / 10
        temp_f = (temp_c * 9/5) + 32
        if (temp_c > 51):
            print("Temperature is high: %d " % temp_c)
            GPIO.output(RedLED, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(RedLED, GPIO.LOW)
            time.sleep(5)
            GPIO.output(GreenLED, GPIO.LOW)
        if (temp_c < 50):
            print("Temperature is normal: %d " % temp_c)
            GPIO.output(RedLED, GPIO.LOW)
            GPIO.output(GreenLED, GPIO.HIGH)
        if (temp_f > 81):
            print("The temp. is high at: %d " % temp_f)		    
        time.sleep(2)

except KeyboardInterrupt:
    print "Keyboard Interrupt"
    GPIO.cleanup()
    print "GPIO Cleaned"
