import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyautogui
from random import *

escuchar = sr.Recognizer()

inicializar = pyttsx3.init()
velocidad_voz = 130
inicializar.setProperty('rate', velocidad_voz)
nombre_ia = "viernes"
intentos = 0

# Inicialización de configuación de la voz
voices = inicializar.getProperty('voices')

# En est sección de abajo, solo estoy seleccionando una voz de las que ya tengo instalado en el equipo
# Mi sistema operativo es el Windows 10, en caso de instalar nuevos paquetes de voces
# solo lo descargan desde la configuración de windows, en mi caso la voz que estoy utilizando 
# es la del id=1, en su caso puede ser distinto

inicializar.setProperty('voice', voices[1].id)

# Función de hablar de la I.A.
def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

# Función que captura la voz
def tomar():
    command = ""

    try:
        with sr.Microphone() as voz:
            print("Escuchando Sr(a)...!!!")
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language="es-ES")
            command = command.lower()

            if nombre_ia in command:
                command = command.replace(nombre_ia, "")
    
    except:
        habla("Disculpa no te entendi")
    
    return command

def viernes():
    command = tomar()
    
    if "reproduce" in command:
        cancion = command.replace("reproduce", '')
        habla("reproduciendo " + cancion)
        pywhatkit.playonyt(cancion)
        
    elif "hora" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        habla("La hora es " + time)
        
    elif "hola" in command:
        nombre_usuario = "Goichi"
        habla("Hola " + nombre_usuario)
        
    elif "diego" in command:
        habla("DIEGO ES EL CAMPEON DE BOMBERMAN")

    elif "como estas" in command:
        valor_random = randint(1, 5)

        if valor_random == 1:
            habla("He estado mejor")
            

        if valor_random == 2:
            habla("Más o menos")
            

        if valor_random == 3:
            habla("Bien")
            

        if valor_random == 4:
            habla("Excelente")
            
        
        if valor_random == 5:
            habla("Muy bien")
    
    
while True:
    viernes()