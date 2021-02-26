import tkinter as tk
import pytube
from tkinter import messagebox as mb
from PIL import Image, ImageTk

root = tk.Tk()
root.title('YouTube Downloader')
canvas = tk.Canvas(root, width = 0, height = 200)
canvas.grid(column = 5, row = 6)

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=3 , row=1)

inputt = tk.StringVar()

instructions = tk.Label(root, text= "ENTER THE YOUTUBE URL HERE", font = ('Raleway', 15, 'bold'))
instructions.grid(column = 3, row = 5)

def song_file():
    link = inputt.get()
    inputt.set("")
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(r'E:\output\song')
    mb.showinfo("YAY!!!!", "Audio downloaded")


def video_file():
    link = inputt.get()
    inputt.set("")
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    stream.download(r'E:\output\video')
    mb.showinfo("YAY!!!!", "Video downloaded")

entry = tk.Entry(root, textvariable=inputt, font=('Raleway', 12, 'normal'), width = 30)
entry.grid(column=3, row=2)

video = tk.StringVar()
video_btn = tk.Button(root, textvariable=video ,command = lambda:video_file(), font = ('Raleway', 12, 'bold'), bg="#858585", fg = "white", height = 2, width = 8,relief = "groove")
video.set("VIDEO")
video_btn.grid(row=6, column=2)

song = tk.StringVar()
audio_btn = tk.Button(root, textvariable=song ,command = lambda:song_file(), font = ('Raleway', 12, 'bold'), bg="#858585", fg = "white" , height = 2, width = 8,relief = "groove")
song.set("AUDIO")
audio_btn.grid(row=6, column=3)

exit_button = tk.Button(root, text="EXIT", command=root.destroy, font = ('Raleway', 12, 'bold'), bg="#858585", fg ="white", height = 2, width = 8,relief = "groove")
exit_button.grid(column = 4, row =6)


root.mainloop()
