from tkinter import *
from tkinter import ttk, filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageGrab
from files.lng import *

brush_size = 12
canvas_width = 900
canvas_height = 600
color = "black"
name_of_color = text_0
x_color = 1200
y_color = 110
count_colors = 0
last_element = []
last_x1 = []
last_y1 = []
last_x2 = []
last_y2 = []
last_fill = []
last_outline = []
index = -1
lang = ""
bg_color = ""

with open("files/background.txt", "r") as file:
    bg_color = file.read()
    file.close()

win = Tk()
win.title("IrisPaint")
win.configure(bg=bg_color)
win.iconbitmap("files/irispaint_icon.ico")
win.option_add("*tearOff", FALSE)

def ru():
    global text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9
    global text_10, text_15, text_16, text_17, text_18, text_19, text_20, text_21, text_22
    global text_23, text_24, text_25, text_26, text_27, text_28, text_29, text_30, text_31
    global text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, text_40, text_41
    text_0 = "чёрный"
    text_1 = "красный"
    text_2 = "оранжевый"
    text_3 = "жёлтый"
    text_4 = "зелёный"
    text_5 = "белый"
    text_6 = "синий"
    text_7 = "фиолетовый"
    text_8 = "серый"
    text_9 = "коричневый"
    text_10 = "кастомный"
    text_15 = "Инструмент: Кисть"
    text_16 = "Количество цветов"
    text_17 = "Достигнут лимит цветов"
    text_18 = "Инструмент: Ластик"
    text_19 = "Без имени"
    text_20 = "Сохранение файла"
    text_21 = "Файл успешно сохранён"
    text_22 = "Новый"
    text_23 = "Открыть"
    text_24 = "Сохранить"
    text_25 = "Отменить"
    text_26 = "Вернуть"
    text_27 = "Файл"
    text_28 = "Изменить"
    text_29 = "Настройки"
    text_30 = "Язык"
    text_31 = "Ластик"
    text_32 = "Очистить всё"
    text_33 = "Кисть"
    text_34 = "Заполнить"
    text_35 = "Требуется перезапуск"
    text_36 = "Закройте программу и запустите её снова, чтобы язык изменился"
    text_37 = "Цвет заднего фона"
    text_38 = "Серый"
    text_39 = "Голубой"
    text_40 = "Светло-зелёный"
    text_41 = "Песчаный"

def en():
    global text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9
    global text_10, text_15, text_16, text_17, text_18, text_19, text_20, text_21, text_22
    global text_23, text_24, text_25, text_26, text_27, text_28, text_29, text_30, text_31
    global text_32, text_33, text_34, text_35, text_36, text_37, text_38, text_39, text_40, text_41
    text_0 = "black"
    text_1 = "red"
    text_2 = "orange"
    text_3 = "yellow"
    text_4 = "green"
    text_5 = "white"
    text_6 = "blue"
    text_7 = "purple"
    text_8 = "grey"
    text_9 = "brown"
    text_10 = "custom"
    text_15 = "Instrument: Brush"
    text_16 = "Color amount"
    text_17 = "Color limit reached"
    text_18 = "Instrument: Eraser"
    text_19 = "No name"
    text_20 = "Saving file"
    text_21 = "File saved successfully"
    text_22 = "New"
    text_23 = "Open"
    text_24 = "Save"
    text_25 = "Undo"
    text_26 = "Redo"
    text_27 = "File"
    text_28 = "Edit"
    text_29 = "Settings"
    text_30 = "Language"
    text_31 = "Eraser"
    text_32 = "Erase all"
    text_33 = "Brush"
    text_34 = "Fill"
    text_35 = "Need restart"
    text_36 = "Close program and open again to change language"
    text_37 = "Background color"
    text_38 = "Grey"
    text_39 = "Light blue"
    text_40 = "Light green"
    text_41 = "Sandy"


#лейблы     labels
bs_label = Label(win, text="", font="Arial 10 bold", bg=bg_color)
bs_label.place(x=1016, y=10)

color_label = Label(win, text="", font="Arial 10 bold", bg=bg_color)
color_label.place(x=1196, y=10)

ins_label = Label(win, text=text_15, font="Arial 10 bold", bg=bg_color)
ins_label.place(x=1016, y=185)

wc_label = Label(win, text="", font="Arial 10 bold", bg=bg_color)
wc_label.place(x=1016, y=440)

hc_label = Label(win, text="", font="Arial 10 bold", bg=bg_color)
hc_label.place(x=1016, y=515)

def change_language_ru():
    ru()
    wc_label["text"] = f"Ширина холста: {canvas_width}"
    hc_label["text"] = f"Длина холста: {canvas_height}"
    bs_label["text"] = f"Размер: {brush_size}"
    color_label["text"] = f"Цвет: {name_of_color}"
    with open("files/lang.txt", "w") as file:
        file.write("ru")
        file.close()

def change_language_en():
    en()
    wc_label["text"] = f"Canvas width: {canvas_width}"
    hc_label["text"] = f"Canvas height: {canvas_height}"
    bs_label["text"] = f"Size: {brush_size}"
    color_label["text"] = f"Color: {name_of_color}"
    with open("files/lang.txt", "w") as file:
        file.write("en")
        file.close()

def chng_ru():
    if lang == "ru": pass
    else:
        change_language_ru()
        messagebox.showinfo(title=text_35, message=text_36)

def chng_en():
    if lang == "en": pass
    else:
        change_language_en()
        messagebox.showinfo(title=text_35, message=text_36)

with open("files/lang.txt", "r") as file:
    lang = file.read()
    file.close()

match lang:
    case "ru":
        change_language_ru()
        name_of_color = text_0
        color_label["text"] = f"Цвет: {name_of_color}"
        ins_label["text"] = "Инструмент: Кисть"
    case "en":
        change_language_en()
        name_of_color = text_0
        color_label["text"] = f"Color: {name_of_color}"
        ins_label["text"] = "Instrument: Brush"
    case _:
        messagebox.showerror(title="Language error", message="Language not found")
        quit()

def paint(event):
    global brush_size, color, index
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    oval = canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    last_element.append(oval)
    last_x1.append(x1)
    last_y1.append(y1)
    last_x2.append(x2)
    last_y2.append(y2)
    last_fill.append(color)
    last_outline.append(color)
    index += 1

def change_brush_size(new_size):
    global brush_size 
    brush_size = round(float(new_size))
    if lang == "en": bs_label["text"] = f"Size: {brush_size}"
    elif lang == "ru": bs_label["text"] = f"Размер: {brush_size}"

def change_canvas_width(new_size):
    global canvas_width
    canvas_width = round(float(new_size))
    canvas.configure(width=canvas_width)
    if lang == "en": wc_label["text"] = f"Canvas width: {canvas_width}"
    elif lang == "ru": wc_label["text"] = f"Ширина холста: {canvas_width}"
    win.update()

def change_canvas_height(new_size):
    global canvas_height
    canvas_height = round(float(new_size))
    canvas.configure(height=canvas_height)
    if lang == "en": hc_label["text"] = f"Canvas height: {canvas_height}"
    elif lang == "ru": hc_label["text"] = f"Длина холста: {canvas_height}"
    win.update()

def change_color(new_color, new_name_of_color):
    global color, name_of_color
    color = new_color
    name_of_color = new_name_of_color
    if lang == "en": color_label["text"] = f"Color: {name_of_color}"
    elif lang == "ru": color_label["text"] = f"Цвет: {name_of_color}"
    ins_label["text"] = text_15

def create_color_button(btn_clr, name_clr):
    return Button(win, width=2, height=1, bg=btn_clr, command=lambda: change_color(btn_clr, name_clr))

def new_color():
    global count_colors, x_color, y_color
    if count_colors == 9: messagebox.showinfo(title=text_16, message=text_17)
    else:
        new_color = colorchooser.askcolor()
        create_color_button(new_color[1], text_10).place(x=x_color, y=y_color)
        x_color += 30
        count_colors += 1
        if count_colors == 5:
            y_color += 35
            x_color = 1200

def eraser():
    global color
    color = "white"
    ins_label["text"] = text_18

def erase_all():
    canvas.delete("all")
    last_element.clear()
    canvas.configure(bg="white")

def brush(): ins_label["text"] = text_15

def open_file():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path).resize([canvas.winfo_width()+5, canvas.winfo_height()+5])
    image = ImageTk.PhotoImage(img)
    canvas.image = image
    canvas.delete("all")
    canvas.create_image(0, 0, anchor=NW, image=image)

def save_file():
    file_path = filedialog.asksaveasfilename(initialfile=text_19, filetypes=[(".png", "")])
    lpx = canvas.winfo_rootx() + 2
    lpy = canvas.winfo_rooty() + 2
    rpx = lpx + canvas.winfo_width() - 4
    rpy = lpy + canvas.winfo_height() - 4
    img = ImageGrab.grab([lpx, lpy, rpx, rpy]).save(f"{file_path}.png")
    messagebox.showinfo(title=text_20, message=text_21)

def undo():
    global index
    canvas.delete(last_element[-1])
    last_element.pop(-1)
    index -= 1

def redo():
    global index
    oval = canvas.create_oval(last_x1[index], last_y1[index], last_x2[index], last_y2[index],
        fill=last_fill[index], outline=last_outline[index]
        )
    last_element.append(oval)
    index += 1


def change_bg(bg_clr):
    global bg_color
    bg_color = bg_clr
    win.configure(bg=bg_clr)
    bs_label["bg"] = bg_clr
    color_label["bg"] = bg_clr
    ins_label["bg"] = bg_clr
    wc_label["bg"] = bg_clr
    hc_label["bg"] = bg_clr
    win.update()
    with open("files/background.txt", "w") as file:
        file.write(bg_clr)
        file.close


#меню     menu
file_menu = Menu()
file_menu.add_command(label=text_22, command=erase_all)
file_menu.add_command(label=text_23, command=open_file)
file_menu.add_command(label=text_24, command=save_file)

edit_menu = Menu()
edit_menu.add_command(label=text_25, command=undo)
edit_menu.add_command(label=text_26, command=redo)

language_menu = Menu()
language_menu.add_command(label="English", command=chng_en)
language_menu.add_command(label="Русский", command=chng_ru)

bg_menu = Menu()
bg_menu.add_command(label=text_38, command=lambda: change_bg("#BFBFBF"))
bg_menu.add_command(label=text_39, command=lambda: change_bg("#91E6FF"))
bg_menu.add_command(label=text_40, command=lambda: change_bg("#67E559"))
bg_menu.add_command(label=text_41, command=lambda: change_bg("#FDFFA1"))

settings_menu = Menu()
settings_menu.add_cascade(label=text_30, menu=language_menu)
settings_menu.add_cascade(label=text_37, menu=bg_menu)

main_menu = Menu()
main_menu.add_cascade(label=text_27, menu=file_menu)
main_menu.add_cascade(label=text_28, menu=edit_menu)
main_menu.add_cascade(label=text_29, menu=settings_menu)

win.configure(menu=main_menu)


#холст     canvas
canvas = Canvas(win, width=canvas_width, height=canvas_height, bg="white")
canvas.bind("<B1-Motion>", paint)
canvas.place(x=5,y=5)


#регулировка размера кисти     brush size control
bs_scale = ttk.Scale(win, orient=HORIZONTAL, length=130, from_=1.0, to=30.0, 
                     value=brush_size, command=change_brush_size
                     )
bs_scale.place(x=1020, y=35)


#регулировка ширины холста     canvas width control
wc_scale = ttk.Scale(win, orient=HORIZONTAL, length=200, from_=300.0, to=950.0, 
                     value=canvas_width, command=change_canvas_width
                     )
wc_scale.place(x=1020, y=465)


#регулировка длины холста     canvas height control    
hc_scale = ttk.Scale(win, orient=HORIZONTAL, length=200, from_=300.0, to=650.0, 
                     value=canvas_height, command=change_canvas_height
                     )
hc_scale.place(x=1020, y=540)


#кнопки инструментов     instruments buttons
Button(win, text=text_31, font="Arial 10 bold", width=8, height=2,
       command=eraser, bg="#D5936D", relief=GROOVE, bd=4
       ).place(x=1020, y=215)

Button(win, text=text_32, font="Arial 10 bold", width=12, height=2,
       command=erase_all, bg="#948D8D", relief=GROOVE, bd=4
       ).place(x=1120, y=215)

Button(win, text=text_33, font="Arial 10 bold", width=8, height=2,
       command=brush, bg="#FF4343", relief=GROOVE, bd=4
       ).place(x=1020, y=285)

Button(win, text=text_34, font="Arial 10 bold", width=12, height=2,
       command=lambda: canvas.configure(bg=color),
       bg="#68FF51", relief=GROOVE, bd=4
       ).place(x=1120, y=285)


#кнопки цветов     colors buttons
create_color_button("black", text_0).place(x=1200, y=40)
create_color_button("red", text_1).place(x=1230, y=40)
create_color_button("orange", text_2).place(x=1260, y=40)
create_color_button("yellow", text_3).place(x=1290, y=40)
create_color_button("green", text_4).place(x=1320, y=40)
create_color_button("white", text_5).place(x=1200, y=75)
create_color_button("blue", text_6).place(x=1230, y=75)
create_color_button("purple", text_7).place(x=1260, y=75)
create_color_button("grey", text_8).place(x=1290, y=75)
create_color_button("brown", text_9).place(x=1320, y=75)

cstm_clr_btn = Button(win, width=2, height=1, bg="grey", text="+",
                      font="Arial 9 bold", command=new_color, bd=3
                      )
cstm_clr_btn.place(x=1320, y=145)

win.mainloop()
