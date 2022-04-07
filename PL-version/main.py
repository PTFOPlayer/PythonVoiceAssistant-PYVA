import speech_recognition
import pyttsx3
import os
from googlesearch import search
from datetime import date 


with open("text.txt", "w") as f:
    f.write("file contents\n")
with open("text.txt", "r") as f:
    f.read()

recognizer = speech_recognition.Recognizer()

def search_func (text):
	with speech_recognition.Microphone() as mic: 
		recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
		Saudio = recognizer.listen(mic) 
		Stext = recognizer.recognize_google(Saudio, language = "pl-PL") 
		Stext = Stext.lower()
		query = Stext 
	print("searching for : ", query)
	for j in search(query):
		if j == 10:
			break
		print(j)

def yt_search_func(text):
	with speech_recognition.Microphone() as mic: 
		recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
		Saudio = recognizer.listen(mic) 
		Stext = recognizer.recognize_google(Saudio, language = "pl-PL") 
		Stext = Stext.lower()
		query = Stext + "  +site:youtube.com" 
	print("searching for : ", query)
	for j in search(query):
		if j == 10:
			break
		print(j)

def wiki_search_func(text):
	with speech_recognition.Microphone() as mic: 
		recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
		Saudio = recognizer.listen(mic) 
		Stext = recognizer.recognize_google(Saudio, language = "pl-PL") 
		Stext = Stext.lower()
		query = Stext + "  +site:wikipedia.org" 
		print("searching for : ", query)
		for j in search(query):
			if j == 10:
				break
			print(j)

def filewrite(text):
	with speech_recognition.Microphone() as mic: 
		recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
		Saudio = recognizer.listen(mic) 
		Stext = recognizer.recognize_google(Saudio, language = "pl-PL") 
		Stext = Stext.lower()
	file = open("text.txt", "a")
	file.write(Stext)
	file.close()

def fileread(text):
	file = open("text.txt", "a")
	print(file.read())
	file.close()

   
def network(text):
    os.system('cmd /c "ping 8.8.8.8"')

def date(text):
    today = date.today
    print(today , "\n")

def sr_main():
	while True: 
		try: 
			with speech_recognition.Microphone() as mic: 
				recognizer.adjust_for_ambient_noise(mic, duration=0.2) 
				audio = recognizer.listen(mic) 
				text = recognizer.recognize_google(audio, language = "pl-PL") 
				text = text.lower()
			print(":", text)
	
			if text == "break" or text == "koniec":
				break

			if text == "hello":
				print("hello master \n how can i help you?")
			
			if text == "searching" or text == "wyszukaj": 
				search_func(text)

			if text == "youtube": 
				yt_search_func(text)
	
			if text == "wikipedia":
				wiki_search_func(text)
	
			if text == "network" or text == "sieć":
				network(text)

			if text == "today" or text == "data":
				date(text)

			if text == "notatki":
				filewrite(text)
	
			if text == "otwórz notatki":
				fileread(text)

		except: 
			print("error ocured")
			continue
