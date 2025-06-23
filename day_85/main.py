from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

OVERLAY_WIDTH = 60
POSITION = 0
background_path = ""
overlay_path = ""
WIDTH_SIZE = 500
HEIGHT_SIZE = 500
current_output_img = None
image_label = None

window = Tk()
window.title("I-Mark")
window.minsize(width=WIDTH_SIZE, height=HEIGHT_SIZE)


def select_image()->str:
    return filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")])

def action():
    global background_path
    background_path = select_image()

    if background_path:
        bg_img = Image.open(background_path).convert("RGBA")
        display_image(bg_img)

    print(f"Do something: {background_path}")

def action_select_logo():
    global overlay_path
    overlay_path = select_image()
    print(f"Do something : {overlay_path}")

def add_watermark():
    global POSITION, OVERLAY_WIDTH, WIDTH_SIZE, current_output_img, image_label
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
    b_ratio = b_height / b_width
    b_new_height = int(WIDTH_SIZE * b_ratio)

    o_width, o_height = ov_img.size
    o_ratio = o_height / o_width
    o_new_height = int(OVERLAY_WIDTH * o_ratio)

    ov_img = ov_img.resize((OVERLAY_WIDTH, o_new_height))

    if POSITION == 1:
        position = (0,0)
    elif POSITION == 2:
        position = (b_width - OVERLAY_WIDTH, 0)
    elif POSITION == 3:
        position = (0, b_height - o_new_height)
    elif POSITION == 4:
        position = (b_width - OVERLAY_WIDTH, b_height - o_new_height)

    bg_img.paste(ov_img, position, ov_img)

    current_output_img = bg_img

    new_bg_img = bg_img.resize((WIDTH_SIZE, b_new_height))
    display_image(new_bg_img)

    
def display_image(image:Image):
    global WIDTH_SIZE, image_label

    b_width, b_height = image.size
    b_ratio = b_height / b_width
    b_new_height = int(WIDTH_SIZE * b_ratio)

    new_bg_img = image.resize((WIDTH_SIZE, b_new_height))

    img_tk = ImageTk.PhotoImage(new_bg_img)

    image_label.destroy()
    image_label = Label(window, background='black', image=img_tk)
    image_label.grid(column=0, row=8, columnspan=4, padx=20, pady=20)
    image_label.image = img_tk 
     
def save_image():
    global current_output_img

    if current_output_img:
        current_output_img.save("output.png")
        current_output_img.show()
    

label = Label(text="Image-Marker", font=('Courier', 35, "bold"))
label.grid(column=0, row=0, columnspan=4, pady=5)

btn_select_img = Button(text="Select Image", command=action, width=20)
btn_select_img.grid(column=1, row=1, padx=5)

btn_select_logo = Button(text="Select Watermark", command=action_select_logo, width=20)
btn_select_logo.grid(column=2, row=1, padx=5)

def radio_used():
    global POSITION
    print(radio_state.get())
    
    POSITION = radio_state.get()

#Variable to hold on to which radio button value is checked.
label = Label(text="Water-Mark Location", font=('Courier', 10, "bold"))
label.grid(column=0, row=2, columnspan=4, pady=5)
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Top Left", value=1, variable=radio_state, command=radio_used, width=10)
radiobutton2 = Radiobutton(text="Top Right", value=2, variable=radio_state, command=radio_used, width=10 )
radiobutton3 = Radiobutton(text="Bottom Left", value=3, variable=radio_state, command=radio_used, width=10)
radiobutton4 = Radiobutton(text="Bottom Right", value=4, variable=radio_state, command=radio_used, width=10)
radiobutton1.grid(column=0, row=3)
radiobutton2.grid(column=1, row=3)
radiobutton3.grid(column=2, row=3)
radiobutton4.grid(column=3, row=3)

btn_select_img = Button(text="Add Water-Mark", command=add_watermark, width=20)
btn_select_img.grid(column=0, row=7, columnspan=4, pady=5)

image_label = Label(window, width=60, height=20, background='black')
image_label.grid(column=0, row=8, columnspan=4, padx=5, pady=5)

btn_save_img = Button(text="Save Image", command=save_image, width=20)
btn_save_img.grid(column=0, row=9, columnspan=4, pady=15)

window.mainloop()