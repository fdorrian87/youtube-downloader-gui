from yt_dlp import YoutubeDL #stable YT download library
import customtkinter as ctk #more modern-looking and easy to use than tkinter as it requires less customisation
from tkinter import messagebox #for feedback as ctk does not have this module built in

def yt_download():
    vid_link = entry1.get() #fetch value from entry field
    ydl_opts = { #download options
    'format': 'best',  # Get the best quality available
    'outtmpl': 'C:/Users/frank/Videos/YouTube Downloads/%(title)s.%(ext)s',  # Output template
}
    try: #error handling
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(vid_link, download=True)
            vid_title = info_dict.get('title', 'Unknown Title')
    except Exception as e:
        messagebox.showinfo(message=f"An error occurred: {e}")
    messagebox.showinfo(message="Video downloaded")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x350")
root.title("YouTube Downloader")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Enter the YouTube Video Link Below:", font=("Roboto", 18))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, width=300, placeholder_text="Vid link...")
entry1.pack(pady=12, padx=10)

button1 = ctk.CTkButton(master=frame, text="Download", command=yt_download)
button1.pack(pady=12, padx=10)

root.mainloop()