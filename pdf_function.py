import PyPDF2
import pyttsx3

def pdf_reader(path):
    engine = pyttsx3.init()
    f = open(path, "rb")
    reader = PyPDF2.PdfReader(f)
    text = " "
    for page in reader.pages:
        text += page.extract_text()
    f.close()
    engine.say(text)

    engine.runAndWait()
