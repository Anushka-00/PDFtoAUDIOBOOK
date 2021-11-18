import sys
import subprocess
from pathlib import Path
import fitz
from gtts import gTTS
import PySimpleGUI as sg



def reader(file_loc):
    """
        This method is to extract text from the pdf and return the extracted text in the form of string.
    """
    pages = ""
    
    with fitz.open(file_loc) as doc:
        for i in range(len(doc)):
            pages+= doc[i].get_text()
    return pages


def save_file(file_loc,final_directory,download_filename):
    """
        This method generates an audio file and saves it.
    """  
    pages = reader(file_loc)
    audio = gTTS(pages, lang="en", slow=False)
    audio.save(Path.joinpath(final_directory,download_filename))

def play_file(final_directory,download_filename):
    """
        This method plays the saved audio file.
    """
    subprocess.call(['xdg-open', Path.joinpath(final_directory,download_filename)])

def main():
    """
        main method which implements the GUI converter
    """
    sg.theme('BlueMono')

    file_types = [("PDF (*.pdf)", "*.pdf")]
    layout1 = [ [sg.T("")],
                [sg.Text("Choose a pdf file: ",font=('Lucida',13)), sg.Input(),sg.FileBrowse(key="-IN-",file_types=file_types,size=(10,1)),sg.Button("Submit",size=(10,1))]            
            ]

    window = sg.Window('My File Browser', layout1, size=(800,150))
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        elif event == "Submit":
            file_loc = values["-IN-"]
            file_name = file_loc.split('/')[-1]
            download_filename = "{}.mp3".format(file_name.split(".")[0])
            layout2 = [[sg.Text(file_name,font=('Lucida',13),key = "first_text"),sg.Text("Saved as {}".format(download_filename),font=('Lucida',13),key = "second_text",visible = False),sg.Button("Play the file",size=(15,1), visible=False),sg.Button("Save as Mp3",size=(10,1))]]
            window.Element("-IN-").hide_row()
            window  = sg.Window('My File Browser', layout2, size=(800,150))

            while True:
                if event == sg.WIN_CLOSED or event=="Exit":
                    break
                event, values = window.read()            
                if event == "Save as Mp3":                
                    print("Saving your file...May take a few seconds")
                    window.Element("first_text").Update(visible = False)
                    window.Element("second_text").Update(visible = True)
                    window.Element("Play the file").Update(visible = True)
                    
                    current_directory = Path("/".join(file_loc.split("/")[0:-1]))
                    final_directory = Path.joinpath(current_directory,"audio")

                    # Creating a directory to save the audio file
                    if not Path(final_directory).exists():
                        Path.mkdir(current_directory/"audio")
                    save_file(file_loc,final_directory,download_filename)
                    
                    window.Element("Save as Mp3").Update(visible = False)
                    print("Saved as {}".format(download_filename))
                    
                    
                if event  == "Play the file":
                    play_file(final_directory,download_filename)
                    sys.exit()



if __name__=="__main__":
    main()