from tkinter import *

ventana=Tk()
ventana.title("Conversor de colores")
ventana.geometry("520x200")
ventana.configure(bg="#ffbdbd")

def rgb_hsv():
    val_red = val_red / 255.0
    val_green = val_green / 255.0
    val_blue = val_blue / 255.0

    minimo = min (val_red, val_green, val_blue)
    maximo = max (val_red, val_green, val_blue)
    diff = maximo - minimo

    if minimo == maximo:
        val_hue = 0
    elif maximo == val_red:
        val_hue = (60 * ((val_green - val_blue)/diff)+360)%360
    elif maximo == val_green:
        val_hue = (60 * ((val_green - val_blue)/diff)+120)%360
    elif maximo == val_blue:
        val_hue = (60 * ((val_green - val_blue)/diff)+240)%360

    if maximo == 0:
        val_saturation = 0
    else:
        val_saturation = (diff / maximo) * 100

    val_value = maximo * 100

    return val_hue, val_saturation, val_value

ventana.mainloop()