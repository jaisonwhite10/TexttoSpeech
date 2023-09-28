from tkinter import *
from pdf import PDF

window = Tk()
pd = PDF()
window.geometry('400x400')
window.title('Pdf-Audio App')

upload_button = Button(text='Upload PDF File',command=lambda:pd.upload(window),width=16)
upload_button.place(x=150,y=50)

save_button = Button(text='Save PDF as MP3',command=lambda:pd.save_mp3(window),width=16)
save_button.place(x=150,y=150)

window.mainloop()