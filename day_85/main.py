from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

OVERLAY_WIDTH = 50
POSITION = 0
background_path = ""
overlay_path = ""

#Buttons
def select_image()->str:
    return filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")])

def action():
    global background_path
    background_path = select_image()
    print(f"Do something: {background_path}")

def action_select_logo():
    global overlay_path
    overlay_path = select_image()
    print(f"Do something : {overlay_path}")

def add_watermark():
    global POSITION, OVERLAY_WIDTH
    position = (0,0)

    print("adding watermark")

    if background_path == "":
        print("No Image Found")
        return
    
    if overlay_path == "":
        print("No Image Found")
        return
    
    bg_img = Image.open(background_path).convert("RGBA")
    ov_img = Image.open(overlay_path).convert("RGBA")


    b_width, b_height = bg_img.size
    o_width, o_height = ov_img.size

    ratio = o_height / o_width
    new_height = int(OVERLAY_WIDTH * ratio)

    ov_img = ov_img.resize((OVERLAY_WIDTH, new_height))

    if POSITION == 1:
        position = (0,0)
    elif POSITION == 2:
        position = (b_width - OVERLAY_WIDTH, 0)
    elif POSITION == 3:
        position = (0, b_height - new_height)
    elif POSITION == 4:
        position = (b_width - OVERLAY_WIDTH, b_height - new_height)

    print(position)
    bg_img.paste(ov_img, position, ov_img)

    bg_img.save("output.png")
    bg_img.show()    
    pass

#calls action() when pressed
btn_select_img = Button(text="Select Image", command=action)
btn_select_img.pack()

btn_select_logo = Button(text="Select Watermark", command=action_select_logo)
btn_select_logo.pack()

def radio_used():
    global POSITION
    print(radio_state.get())
    
    POSITION = radio_state.get()

#Variable to hold on to which radio button value is checked.
label = Label(text="Water-Mark Location")
label.pack()
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Top Left", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Top Right", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Bottom Left", value=3, variable=radio_state, command=radio_used)
radiobutton4 = Radiobutton(text="Bottom Right", value=4, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton4.pack()

btn_select_img = Button(text="Add Water-Mark", command=add_watermark)
btn_select_img.pack()

image_label = Label(window)
image_label.pack()

window.mainloop()