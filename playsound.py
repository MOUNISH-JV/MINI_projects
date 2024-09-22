import pyttsx3
#initialize text-to-speech engine
engine = pyttsx3.init()
#convert this to text to speach
f = open("C:\\Users\\Mounish\\OneDrive\\Desktop\\file.txt")
text = f.read()
print(text)
engine.say(text)
#play the speech
engine.runAndWait()