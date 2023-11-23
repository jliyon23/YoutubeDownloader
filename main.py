import tkinter
import customtkinter
from pytube import YouTube

def start_download():
    try:
        ytLink = url_var.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title , text_color="white")
        video.download()
        finish_download.configure(text="Downloaded!",text_color="green")
    except:
        finish_download.configure(text="Invalid YouTube Link!",text_color="red")

def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progressBar
    progress_bar.set(float(percentage_of_completion / 100))



#System settings.
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app settings
app = customtkinter.CTk()
app.title("YouTube Video Downloader by Liyon")
app.geometry("720x480")

#Adding UI Elements.
title = customtkinter.CTkLabel(app, text="Insert Youtube Link")
title.pack(padx=10,pady=10)

#Link input.
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#progress bar
pPercentage = customtkinter.CTkLabel(app,text="0 %")
pPercentage.pack(padx=10,pady=10)

progress_bar = customtkinter.CTkProgressBar(app,width=400)
progress_bar.set(0)
progress_bar.pack(padx=15,pady=15)

#finished download.
finish_download = customtkinter.CTkLabel(app,text="")
finish_download.pack()

#Button Download.
download = customtkinter.CTkButton(app,text="Download",command=start_download)
download.pack(padx=20,pady=20)

#app run
app.mainloop()