import sys
import curses
import time
import RPi.GPIO as GPIO

def confiGPIO(param1):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    return 0

def RESET_DISPLAY(param1):
    if param1 == 0:
        GPIO.output(14, False)
        GPIO.output(15, False)
        GPIO.output(18, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, False)
        GPIO.output(8, False)
        GPIO.output(7, False)
    else:
        GPIO.output(14, True)
        GPIO.output(15, True)
        GPIO.output(18, True)
        GPIO.output(23, True)
        GPIO.output(24, True)
        GPIO.output(25, True)
        GPIO.output(8, True)
        GPIO.output(7, True)
        return 0

def TEST_DISPLAY(param1):
    RESET_DISPLAY(0)
    GPIO.output(14, True)
    time.sleep(param1)
    GPIO.output(15, True)
    time.sleep(param1)
    GPIO.output(18, True)
    time.sleep(param1)
    GPIO.output(23, True)
    time.sleep(param1)
    GPIO.output(24, True)
    time.sleep(param1)
    GPIO.output(25, True)
    time.sleep(param1)
    GPIO.output(8, True)
    time.sleep(param1)
    GPIO.output(7, True)
    return 0

def SHOW_DISPLAY(param1):
    RESET_DISPLAY(0)
    if param1 == 48:    #  0
        SHOW_ZERO()
    elif param1 == 49: #  1
        SHOW_ONE()
    elif param1 == 50: #  2
        SHOW_TWO()
    elif param1 == 51: #  3
        SHOW_THREE()
    elif param1 == 52: #  4
        SHOW_FOUR()
    elif param1 == 53: #  5
        SHOW_FIVE()
    elif param1 == 54: #  6
        SHOW_SIX()
    elif param1 == 55: #  7
        SHOW_SEVEN()
    elif param1 == 56: #  8
        SHOW_EIGHT()
    elif param1 == 57: #  9
        SHOW_NINE()
    elif param1 == 46: # DP 
        GPIO.output(7, True)
    return 0
       
def SHOW_ZERO():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(24, True) # segm. e
    GPIO.output(25, True) # segm. f
    return 0

def SHOW_ONE():
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    return 0

def SHOW_TWO():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(23, True) # segm. d
    GPIO.output(24, True) # segm. e
    GPIO.output(8, True) # segm. g
    return 0

def SHOW_THREE():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(8, True) # segm. g
    return 0

def SHOW_FOUR():
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    GPIO.output(25, True) # segm. f
    GPIO.output(8, True) # segm. g
    return 0

def SHOW_FIVE():
    GPIO.output(14, True) # segm. a
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(25, True) # segm. f
    GPIO.output(8, True) # segm. g
    return 0

def SHOW_SIX():
    GPIO.output(14, True) # segm. a
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(24, True) # segm. e
    GPIO.output(25, True) # segm. f
    GPIO.output(8, True) # segm. g
    return 0

def SHOW_SEVEN():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    return 0

def SHOW_EIGHT():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(24, True) # segm. e
    GPIO.output(25, True) # segm. f
    GPIO.output(8, True) # segm. g
    return 0
    
def SHOW_NINE():
    GPIO.output(14, True) # segm. a
    GPIO.output(15, True) # segm. b
    GPIO.output(18, True) # segm. c
    GPIO.output(23, True) # segm. d
    GPIO.output(25, True) # segm. f
    GPIO.output(8, True) # segm. g
    return 0

confiGPIO(0)
RESET_DISPLAY(0)
SHOW_EIGHT()

