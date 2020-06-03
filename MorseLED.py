from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

## Entry Validation ##
class ValidatingEntry(Entry): #http://effbot.org/zone/tkinter-entry-validate.htm -- Updated Entry to suite python 3
    # base class for validating entry widgets

    def __init__(self, master, value="", **kw):
        Entry.__init__(*(self, master), *kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(value)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(self.newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        return value


class MaxLengthEntry(ValidatingEntry):

    def __init__(self, master, value = "", maxlength = None, **kw):
        self.maxlength = maxlength
        ValidatingEntry.__init__(*(self, master), *kw)

    def validate(self, value): #validate also used to alter light
        if len(value) <= self.maxlength:
            return value
        return None # new value too long



## Morse Code ##
Unit = 0.25 #time unit
dot = 1
dash = 3

def letter(morsecharacter): #list of wait times, i.e. A = [dot, dash] <-- dot and dash
    for wait in morsecharacter:
        Green.on()
        time.sleep(wait*Unit) #wait dot or dash
        Green.off()
        time.sleep(Unit) #next letter wait

def Morse(word):
    for character in word.upper():
        if character == 'A':
            letter([dot, dash])
        elif character == 'B':
            letter([dash, dot, dot, dot])
        elif character == 'C':
            letter([dash, dot, dash, dot])
        elif character == 'D':
            letter([dash, dot, dot])
        elif character == 'E':
            letter([dot])
        elif character == 'F':
            letter([dot, dot, dash, dot])
        elif character == 'G':
            letter([dash, dash, dot])
        elif character == 'H':
            letter([dot, dot, dot, dot])
        elif character == 'I':
            letter([dot, dot])
        elif character == 'J':
            letter([dot, dash, dash, dash])
        elif character == 'K':
            letter([dash, dot, dash])
        elif character == 'L':
            letter([dot, dash, dot, dot])
        elif character == 'M':
            letter([dash, dash])
        elif character == 'N':
            letter([dash, dot])
        elif character == 'O':
            letter([dash, dash, dash])
        elif character == 'P':
            letter([dot, dash, dash, dot])
        elif character == 'Q':
            letter([dash, dash, dot, dash])
        elif character == 'R':
            letter([dot, dash, dot])
        elif character == 'S':
            letter([dot, dot, dot])
        elif character == 'T':
            letter([dash])
        elif character == 'U':
            letter([dot, dot, dash])
        elif character == 'V':
            letter([dot, dot, dot, dash])
        elif character == 'W':
            letter([dot, dash, dash])
        elif character == 'X':
            letter([dash, dot, dot, dash])
        elif character == 'Y':
            letter([dash, dot, dash, dash])
        elif character == 'Z':
            letter([dash, dash, dot, dot])
        elif character == '1':
            letter([dot, dash, dash, dash, dash])
        elif character == '2':
            letter([dot, dot, dash, dash, dash])
        elif character == '3':
            letter([dot, dot, dot, dash, dash])
        elif character == '4':
            letter([dot, dot, dot, dot, dash])
        elif character == '5':
            letter([dot, dot, dot, dot, dot])
        elif character == '6':
            letter([dash, dot, dot, dot, dot])
        elif character == '7':
            letter([dash, dash, dot, dot, dot])
        elif character == '8':
            letter([dash, dash, dash, dot, dot])
        elif character == '9':
            letter([dash, dash, dash, dash, dot])
        elif character == '0':
            letter([dash, dash, dash, dash, dash])
        elif character == ' ':
            time.sleep(5*Unit) #space between words -2
        time.sleep(2*Unit) #space between characters -1

## Lights ##
Green = LED(15)

## Initailse GUI ##
window = Tk()
window.title("Morse LED")

## Actions ##
def Translate():
    Morse(E.get())

def close():
    GPIO.cleanup()
    window.destroy()

## Widgets ##
#v = StringVar()
E = MaxLengthEntry(window, maxlength = 12)
E.grid(row = 0, column = 0)

TranslateButton = Button(window, text = "Translate", command = Translate, height = 1, width = 6)
TranslateButton.grid(row = 0, column = 1)

ExitButton = Button(window, text = "Exit", command = close, height = 1, width = 6)
ExitButton.grid(row = 1, column = 1)
window.protocol("WM_DELETE_WINDOW", close)

## Even Handler ##
window.mainloop()


