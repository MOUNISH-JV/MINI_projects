import PyPDF2
import pyttsx3
#initiate the text to speech engine
engine = pyttsx3.init()
#open the pdf you want to read, pdf will be in binary mode so use "rb" which mean read binary
f = open("C:\\Users\\Mounish\\OneDrive\\Documents\\RESUMES\\cover letter.pdf","rb")
#here reader is an object created to use Pdfreader() method form PyPDF2.
reader = PyPDF2.PdfReader(f)
#creating an empty sting to extract the content in the pdf
text = " "
# for loop is used to iterate through multiple pages if pdf contains number of pages
for page in reader.pages: # here we iterate though each page
    text += page.extract_text() # here we append the content of each page to text.
                                #that text will be converted into speech.

f.close() #closing the file
engine.say(text)

engine.runAndWait()
