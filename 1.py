from PyPDF2.pdf import PdfFileReader
import pyttsx3
import pdfplumber
import PyPDF2 
file='a.pdf'
pdfFileObj=open(file,'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pages=PdfFileReader.numPages
with pdfplumber.open(file) as pdf:
    for i in range(0,pages):
        page=pdf.pages[i]
        text=page.extract_text()
        speaker=pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()

