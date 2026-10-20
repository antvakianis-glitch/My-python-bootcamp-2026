import os
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageDraw, ImageFont


selected_path = ""


def add_watermark(image, text):
    img_width, img_height = image.size

    draw = ImageDraw.Draw(image)

    font_size = max(20, int(img_height * 0.05))

    font = ImageFont.truetype("arial.ttf", font_size)
    stroke = max(1, int(font_size * 0.05))

    text_bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    margin = int(img_width * 0.03)

    x = img_width - text_width - margin - text_bbox[0]
    y = img_height - text_height - margin - text_bbox[1]

    draw.text((x, y), text, font=font, fill="white",
              stroke_width=stroke, stroke_fill="black")

    return image


def choose_image():
    global selected_path
    filename = filedialog.askopenfilename(filetypes = [("Images", "*.png *.jpg *.jpeg")])
    if filename:
        selected_path = filename
        cut_path = os.path.basename(selected_path)
        path_label.config(text=f"Image: {cut_path}")


def apply_watermark():
    if not selected_path:
        messagebox.showwarning("Warning", "Please select an image")
        return

    text = entry.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter a text")
        return

    img = Image.open(selected_path)
    result = add_watermark(img, text)

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")]
    )
    if not save_path:
        return

    if save_path.lower().endswith((".jpg", ".jpeg")) and result.mode == "RGBA":
        result = result.convert("RGB")

    result.save(save_path)
    messagebox.showinfo("Success", "Image saved successfully and watermark has been applied")

window = tk.Tk()
window.title("Watermark Desktop")
window.geometry("300x300")


tk.Label(window, text="Watermark text:").pack()
entry = tk.Entry(window)
entry.pack()

path_label = tk.Label(window, text="Watermark image:")
path_label.pack()


tk.Button(window, text="Choose Image", command=choose_image).pack()
tk.Button(window, text="Apply Watermark", command=apply_watermark).pack()


window.mainloop()