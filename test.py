# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from docx import Document

# This module is imported so that we can  
# play the converted audio 
import os 
  
def getText(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

# The text that you want to convert to audio 
mytext = getText("teste.docx")
  
# Language in which you want to convert 
language = 'pt'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("afplay welcome.mp3") 

