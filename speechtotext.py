import speech_recognition as s 
#create a object of Recognizer
sr=s.Recognizer()
print("Hi this is for you")
with s.Microphone() as m:
 audio=sr.listen(m)
 query=sr.recognize_google(audio,language='eng-in')
 print(query)

