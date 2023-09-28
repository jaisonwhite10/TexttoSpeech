from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import PyPDF2

class PDF:
    def __init__(self):
        self.file_directory = None
        self.mp3_name = None

    def upload(self,window):

        self.file_directory = filedialog.askopenfilename(title='Upload PDF File')
        file_directory_split = self.file_directory.split('/')
        filename = file_directory_split[4]
        if self.file_directory:
            upload_success = Label(window, text=f'{filename} successfully uploaded!')
            if upload_success:
                upload_success.config(text=f'{filename} successfully uploaded!')
            upload_success.place(x=75, y=100)
        return self.file_directory

    def save_mp3(self,window):

        file_directory_split = self.file_directory.split('/')
        filename_pdf = file_directory_split[4]
        pdf_split = filename_pdf.split('.')
        filename = pdf_split[0]

        # # path of the PDF file
        path = open(self.file_directory, 'rb')
        pdfReader = PyPDF2.PdfReader(path)

        combined_text = ''

        for page in pdfReader.pages:
            text = page.extract_text()
            combined_text += text + "\n\n"

        myobj = gTTS(text=combined_text, lang='en', slow=False)
        myobj.save(f"{filename}.mp3")

        save_success = Label(window, text=f'{filename}.mp3 successfully uploaded!')
        if save_success:
            save_success.config(text=f'{filename}.mp3 successfully uploaded!')

        save_success.place(x=75, y=200)