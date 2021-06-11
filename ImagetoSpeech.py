#image processing

from picamera import PiCamera
from time import sleep
import pytesseract
import pyttsx3
from googletrans import Translator
from PIL import Image

#capture image using Pi Camera
camera=PiCamera()
camera.start_preview()
sleep(3)
camera.capture('/home/pi/Desktop/Project/7.jpeg') #save image at particular location
camera.stop_preview()

#image to text 
image = Image.open('7.jpeg')
print(image)
text=pytesseract.image_to_string(image)
print(text)

#text to speech
engine = pyttsx3.init()
engine.setProperty('rate',100)  #120 words per minute
engine.setProperty('volume',0.6)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.say(text)
engine.runAndWait()