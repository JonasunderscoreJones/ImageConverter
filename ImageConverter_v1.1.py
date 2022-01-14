from PIL import Image, ImageTk
import sys, os
import tkinter as tk
from tkinter import filedialog

options = [".bmp", ".dds", ".dib", ".eps", ".gif", ".icns", ".ico", ".im", ".jpeg", ".jpg", ".msp", ".pcx", ".png", ".ppm", ".sgi", ".spider", ".tga", ".tiff", ".webp", ".xbm", ".palm", ".pdf", ".xv"]

root = tk.Tk()

def getimg(button1):
    global img_path, img
    img_path = filedialog.askopenfilename()
    print("ImagePath: " + img_path)
    if img_path != "":
        img = Image.open(img_path)
        maxwidth = 215
        maxheight = 215
        width, height = img.size
        print(width, height)
        if width > height:
            scalingfactor = maxwidth/width
            width = maxwidth
            height = int(height*scalingfactor)
        else:
            scalingfactor = maxheight/height
            height = maxheight
            width = int(width*scalingfactor)

        img = img.resize((width,height), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        width, height = img.size
        print(width, height)
        button1['image'] = photo
        
        global filename, file_extension, selection
        filename, file_extension = os.path.splitext(img_path)
        selection = selections.get()
        label3["text"] = "Convert '" + file_extension + "' to '" + selection + "'?"
        selection = options.get()
    print(img_path)

def convertimage():
    print("ConvertImage")
    img.save(filename + selections.get())
    print("Image saved as: '" + filename + selections.get() + "'")
    tk.messagebox.showinfo(title="Success", message="Your image has successfully been converted!")

root.title("Converter")
root.resizable(False, False)
root.geometry("219x320")
label0 = tk.Label(root, text="Image Converter").grid(row=0, column=1)
label1 = tk.Label(root, text="Select file:").grid(column=0, row=2)
button1 = tk.Button(root, text="\n\n\n\n\n\n\nClick to open File\n\n\n\n\n\n", command=(lambda: getimg(button1)))
button1.grid(row=3, column=0, rowspan=3, columnspan=3, sticky=tk.NSEW)

selections = tk.StringVar(root)
selections.set(".ico")

list1 = tk.OptionMenu(root, selections, *options)
list1.grid(column=2, row=2)
label2 = tk.Label(root, text="Convert to:").grid(column=2, row=1)
button2 = tk.Button(root, text="Convert", command=(lambda: convertimage())).grid(column=2, row=6, sticky=tk.E)
label3 = tk.Label(root)
label3.grid(row=6, column=0, columnspan=2)
root.mainloop()

sys.argv.pop(0)
if len(sys.argv) > 1:
    if sys.argv[0] == "-p":
        sys.argv.pop(0)
        img_path = sys.argv[0]
        correct_syntax = True
    else:
        print("[ERROR ] enter '-p [image path]' behind the filename when executing the script")
        correct_syntax = False
else:
    print("[ERROR ] enter '-p [image path]' behind the filename when executing the script")
    correct_syntax = False
if correct_syntax:
    img = Image.open(img_path)
    img.save(img_path + '.ico')
else:
    print("[Thread] Exiting Program")