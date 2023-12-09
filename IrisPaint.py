from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk, ImageGrab
from lng import *

brush_size = 8
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
lang = ""

text_11 = f"Ширина холста: {canvas_width}"
text_12 = f"Длина холста: {canvas_height}"
text_13 = f"Размер: {brush_size}"
text_14 = f"Цвет: {name_of_color}"

def ru():
    global text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9
    global text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19
    global text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29
    global text_30, text_31, text_32, text_33, text_34, text_35, text_36
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

def en():
    global text_0, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9
    global text_10, text_11, text_12, text_13, text_14, text_15, text_16, text_17, text_18, text_19
    global text_20, text_21, text_22, text_23, text_24, text_25, text_26, text_27, text_28, text_29
    global text_30, text_31, text_32, text_33, text_34, text_35, text_36
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

def change_language_ru():
    global text_11, text_12, text_13, text_14
    ru()
    text_11 = f"Ширина холста: {canvas_width}"
    text_12 = f"Длина холста: {canvas_height}"
    text_13 = f"Размер: {brush_size}"
    text_14 = f"Цвет: {name_of_color}"
    with open("lang.txt", "w") as file:
        file.write("ru")
        file.close()

def change_language_en():
    global text_11, text_12, text_13, text_14
    en()
    text_11 = f"Canvas width: {canvas_width}"
    text_12 = f"Canvas height: {canvas_height}"
    text_13 = f"Size: {brush_size}"
    text_14 = f"Color: {name_of_color}"
    with open("lang.txt", "w") as file:
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

win = Tk()
win.title("IrisPaint")
win.configure(bg="#BFBFBF")
win.option_add("*tearOff", FALSE)

with open("lang.txt", "r") as file:
    lang = file.read()
    file.close()

match lang:
    case "ru": change_language_ru()
    case "en": change_language_en()
    case _:
        messagebox.showerror(title="Language error", message="Language not found")
        quit()

def paint(event):
    global brush_size, color
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

def increase_canvas_width():
    global canvas_width
    canvas_width += 25
    canvas.configure(width=canvas_width)
    wc_label["text"] = text_11
    win.update()
    if canvas_width == 950: in_wc_btn["state"] = "disabled"
    elif canvas_width > 300: dec_wc_btn["state"] = "normal"

def decrease_canvas_width():
    global canvas_width
    canvas_width -= 25
    canvas.configure(width=canvas_width)
    wc_label["text"] = text_11
    win.update()
    if canvas_width == 300: dec_wc_btn["state"] = "disabled"
    elif canvas_width < 950: in_wc_btn["state"] = "normal"

def increase_canvas_height():
    global canvas_height
    canvas_height += 25
    canvas.configure(height=canvas_height)
    hc_label["text"] = text_12
    win.update()
    if canvas_height == 650: in_hc_btn["state"] = "disabled"
    elif canvas_height > 300: dec_hc_btn["state"] = "normal"

def decrease_canvas_height():
    global canvas_height
    canvas_height -= 25
    canvas.configure(height=canvas_height)
    hc_label["text"] = text_12
    win.update()
    if canvas_height == 300: dec_hc_btn["state"] = "disabled"
    elif canvas_height < 650: in_hc_btn["state"] = "normal"

def increase_brush_size():
    global brush_size
    brush_size += 1
    bs_label["text"] = text_13
    if brush_size == 25: in_bs_btn["state"] = "disable"
    elif brush_size > 1: dec_bs_btn["state"] = "normal"

def decrease_brush_size():
    global brush_size
    brush_size -= 1
    bs_label["text"] = text_13
    if brush_size == 1: dec_bs_btn["state"] = "disable"
    elif brush_size < 25: in_bs_btn["state"] = "normal"

def change_color(new_color, new_name_of_color):
    global color, name_of_color
    color = new_color
    name_of_color = new_name_of_color
    color_label["text"] = text_14
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
    canvas.delete(last_element[-1])
    last_element.pop(-1)

def redo():
    global color
    oval = canvas.create_oval(last_x1[-1], last_y1[-1], last_x2[-1], last_y2[-1],
        fill=last_fill[-1], outline=last_outline[-1]
        )
    last_element.append(oval)
    last_x1.pop(-1)
    last_y1.pop(-1)
    last_x2.pop(-1)
    last_y2.pop(-1)
    last_fill.pop(-1)
    last_outline.pop(-1)


#меню
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

settings_menu = Menu()
settings_menu.add_cascade(label=text_30, menu=language_menu)

main_menu = Menu()
main_menu.add_cascade(label=text_27, menu=file_menu)
main_menu.add_cascade(label=text_28, menu=edit_menu)
main_menu.add_cascade(label=text_29, menu=settings_menu)

win.configure(menu=main_menu)


#холст
canvas = Canvas(win, width=canvas_width, height=canvas_height, bg="white")
canvas.bind("<B1-Motion>", paint)
canvas.place(x=5,y=5)


#лейблы
bs_label = Label(win, text=text_13, font="Arial 10 bold", bg="#BFBFBF")
bs_label.place(x=1016, y=10)

color_label = Label(win, text=text_14, font="Arial 10 bold", bg="#BFBFBF")
color_label.place(x=1196, y=10)

ins_label = Label(win, text=text_15, font="Arial 10 bold", bg="#BFBFBF")
ins_label.place(x=1016, y=185)

wc_label = Label(win, text=text_11, font="Arial 10 bold", bg="#BFBFBF")
wc_label.place(x=1016, y=440)

hc_label = Label(win, text=text_12, font="Arial 10 bold", bg="#BFBFBF")
hc_label.place(x=1016, y=515)


#кнопки регулирования размера кисти
in_bs_btn = Button(win, width=3, height=1, text="+", font="Arial 15 bold", bg="#E8DD78",
       command=increase_brush_size, relief=GROOVE
       )
in_bs_btn.place(x=1020, y=35)

dec_bs_btn = Button(win, width=3, height=1, text="-", font="Arial 15 bold", bg="#E8DD78",
       command=decrease_brush_size, relief=GROOVE
       )
dec_bs_btn.place(x=1074, y=35)


#кнопки регулирования ширины холста
in_wc_btn = Button(win, width=3, height=1, text="+", font="Arial 15 bold", bg="#E8DD78",
       command=increase_canvas_width, relief=GROOVE
       )
in_wc_btn.place(x=1020, y=465)

dec_wc_btn = Button(win, width=3, height=1, text="-", font="Arial 15 bold", bg="#E8DD78",
       command=decrease_canvas_width, relief=GROOVE
       )
dec_wc_btn.place(x=1074, y=465)


#кнопки регулирования длины холста
in_hc_btn = Button(win, width=3, height=1, text="+", font="Arial 15 bold", bg="#E8DD78",
       command=increase_canvas_height, relief=GROOVE
       )
in_hc_btn.place(x=1020, y=540)

dec_hc_btn = Button(win, width=3, height=1, text="-", font="Arial 15 bold", bg="#E8DD78",
       command=decrease_canvas_height, relief=GROOVE
       )
dec_hc_btn.place(x=1074, y=540)


#кнопки инструментов
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


#кнопки цветов
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
                      font="Arial 9 bold", command=new_color,
                      relief=GROOVE, bd=3
                      )
cstm_clr_btn.place(x=1320, y=145)

win.mainloop()