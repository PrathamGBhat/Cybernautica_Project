



from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\pgbha\Downloads\HACMAN\build\assets\frame0")


def Username():
    input
    username.itemconfig(text='')
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("540x670")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 540,
    width = 670,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1440.0,
    1024.0,
    fill="#878787",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=19.0,
    y=875.0,
    width=270.0,
    height=96.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=323.0,
    y=860.0,
    width=777.0,
    height=121.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1134.0,
    y=868.0,
    width=283.0,
    height=96.0
)

canvas.create_text(
    476.0,
    32.0,
    anchor="nw",
    text="Welcome Back,\n",
    fill="#000000",
    font=("Inter", 40 * -1)
)

canvas.create_rectangle(
    99.0,
    103.0,
    437.0,
    451.0,
    fill="#000000",
    outline="")

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=26.0,
    y=532.0,
    width=630.0,
    height=141.0
)

canvas.create_text(
    549.0,
    177.0,
    anchor="nw",
    text="Registered:",
    fill="#000000",
    font=("Inter", 40 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=55.0,
    y=693.0,
    width=467.0,
    height=103.0
)

canvas.create_text(
    604.0,
    263.0,
    anchor="nw",
    text="Contact Number: ",
    fill="#000000",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    673.0,
    361.0,
    anchor="nw",
    text="Education:",
    fill="#000000",
    font=("Inter", 40 * -1)
)

canvas.create_text(
    673.0,
    531.0,
    anchor="nw",
    text="Bio:",
    fill="#000000",
    font=("Inter", 40 * -1)
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=905.0,
    y=188.0,
    width=499.0,
    height=67.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1019.0,
    y=298.0,
    width=387.0,
    height=63.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=903.0,
    y=405.0,
    width=501.0,
    height=126.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=681.0,
    y=602.0,
    width=723.0,
    height=194.0
)

username=canvas.create_text(
    577.0,
    72.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Inter", 40 * -1)
)
window.resizable(False, False)
window.mainloop()

