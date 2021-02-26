import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from pytube import Playlist



root = tk.Tk()
root.title('YouTube Downloader')
canvas = tk.Canvas(root, width = 100, height = 200)
canvas.grid(column = 4, row = 6)

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=3 , row=1)

inputt = tk.StringVar()

instructions = tk.Label(root, text= "ENTER THE YOUTUBE PLAYLIST URL HERE", font = ('Raleway', 15, 'bold'))
instructions.grid(column = 3, row = 5)



def video_file():
    link = inputt.get()
    inputt.set("")
    p = Playlist(link)
    for vid in p.videos:
        vid.streams.first().download(r'E:\output\video')
    mb.showinfo("YAY!!!!", "Playlist Downloaded")

entry = tk.Entry(root, textvariable=inputt, font=('Raleway', 12, 'normal'), width = 30)
entry.grid(column=3, row=2)

video = tk.StringVar()
video_btn = tk.Button(root, textvariable=video ,command = lambda:video_file(), font = ('Raleway', 12, 'bold'), bg="#858585", fg = "white", height = 2, width = 15,relief = "groove")
video.set("DOWNLOAD")
video_btn.grid(row=6, column=3)


exit_button = tk.Button(root, text="EXIT", command=root.destroy, font = ('Raleway', 12, 'bold'), bg="#858585", fg ="white", height = 2, width = 8,relief = "groove")
exit_button.grid(column = 4, row =6)


root.mainloop()
