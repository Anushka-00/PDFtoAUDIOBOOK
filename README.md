# PDF TO AUDIO CONVERTER

### This project implements a simple pdf to audiobook converter.<br> 
Here, the software extracts the text from the pdf as a string using PyMuPDF library and converts it to audio using the gTTs library.
<br>

### The workflow is:

        Upload the pdf -> Scan and extract text -> Convert and Save the audio file -> Play the file
<br>

###  PreRequirements:
The libraries which are to be used can be installed by running the following command:
        
        pip3 install -r requirements.txt
<br>

<small><strong>Note:</strong> However, this software cannot be used to read out complicated pdfs having scientific equations or symbols as this project only extracts the texual portion of the pdf.</small>