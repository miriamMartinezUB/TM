import tkinter as tk

from PIL import Image, ImageTk


def play_images(image_paths, fps):
    root = tk.Tk()
    root.title("Video")

    delay = int(1000 / fps)  # Convertir fps a milisegundos

    def update_image():
        nonlocal image_label, current_image_index
        image_path = image_paths[current_image_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo
        current_image_index = (current_image_index + 1) % len(image_paths)
        root.after(delay, update_image)

    current_image_index = 0
    image_label = tk.Label(root)
    image_label.pack()

    update_image()

    root.mainloop()