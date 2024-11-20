import os
from tkinter import Tk, Label, Entry, Button, messagebox

def convert_to_webp():
    current_dir = os.getcwd()
    save_dir = os.path.join(current_dir, "compressed_images")
    os.makedirs(save_dir, exist_ok=True)

    quality = quality_entry.get()
    if not quality.isdigit() or not (0 <= int(quality) <= 100):
        messagebox.showerror("Error", "Set quality from 0 to 100")
        return

    image_extensions = (".jpg", ".jpeg", ".png")
    images = [file for file in os.listdir(current_dir) if file.lower().endswith(image_extensions)]

    if not images:
        messagebox.showinfo("Information", "There are no images in the folder to process")
        return

    for image in images:
        input_file = os.path.join(current_dir, image)
        output_file = os.path.join(save_dir, f"{os.path.splitext(image)[0]}.webp")
        command = f'cwebp -q {quality} "{input_file}" -o "{output_file}"'
        os.system(command)

    messagebox.showinfo("Done", f"Conversion completed! Files saved in folder: {save_dir}")

root = Tk()
root.title("WebP Converter")

Label(root, text="Set quality (0-100):").pack()
quality_entry = Entry(root)
quality_entry.insert(0, "80")
quality_entry.pack()

Button(root, text="Start conversion", command=convert_to_webp).pack()
root.mainloop()

