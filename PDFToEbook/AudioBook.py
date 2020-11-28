"""
Installs:
    pip install pyttsx3
    pip install PyPDF2

Credits: Instagram @coding_elite , "https://www.instagram.com/p/CIIksetA8r1/?utm_source=ig_web_copy_link"
"""

import pyttsx3
import PyPDF2

book = open('PDFToEbook\CS.pdf', "rb") #Opens the book.
pdfReader = PyPDF2.PdfFileReader(book) #Reads the book.
pages = pdfReader.numPages #Stores the number of pages.

speaker = pyttsx3.init() #Initialises the speaker object.
for num in range(0, pages): #Loops through the pages.
    page = pdfReader.getPage(num) #Accesses the individual page.
    text = page.extractText() #Accesses the individual pieces of texr.
    speaker.say(text) #Actually says the text.
    speaker.runAndWait() #Small pause so that it's humanlike.
