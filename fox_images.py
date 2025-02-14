import requests
import tkinter as tk
from PIL import Image, ImageTk
import io
import random


def get_random_url():
    number = random.randint(1, 122)
    return f"https://randomfox.ca/images/{number}.jpg"


def get_photo():
    url = get_random_url()
    data = requests.get(url)
    image_data = Image.open(io.BytesIO(data.content))
    img = ImageTk.PhotoImage(image_data)
    label.config(image=img)
    label.image = img


window = tk.Tk()
window.title("Красивые лисички!")
window.geometry('900x800')
label = tk.Label(window)
label.pack()
button = tk.Button(window, text="Новое изображение", command=get_photo)
button.place(relx=0.5, rely=0.9, anchor="center")

get_photo()
window.mainloop()