from tkinter import *
from colorsys import hsv_to_rgb

ventana=Tk()
ventana.title("Conversor")
ventana.geometry("250x610")
ventana.resizable(1,1)
ventana.configure(bg="#65B2FF")

#Funciones
def rgb_hsv(v):
    rgb_r = rgb_r_entry.get() / 255.0
    rgb_g = rgb_g_entry.get() / 255.0
    rgb_b = rgb_b_entry.get() / 255.0

    minimo = min (rgb_r, rgb_g, rgb_b)
    maximo = max (rgb_r, rgb_g, rgb_b)
    diff = maximo - minimo

    if minimo == maximo:
        val_hue = 0
    elif maximo == rgb_r_entry:
        val_hue = (60 * ((rgb_g - rgb_b)/diff)+360)%360
    elif maximo == rgb_g_entry:
        val_hue = (60 * ((rgb_g - rgb_b)/diff)+120)%360
    elif maximo == rgb_b_entry:
        val_hue = (60 * ((rgb_g - rgb_b)/diff)+240)%360

    if maximo == 0:
        val_saturation = 0
    else:
        val_saturation = (diff / maximo) * 100

    val_value = maximo * 100

    return val_hue, val_saturation, val_value

def cambia_color_desde_hex(event):
    color_nuevo = "#" + hex_entry.get()
    vista_previa_canvas.configure(bg=color_nuevo)

def cambia_color_desde_rgb(v):
    color_c = "#%02x%02x%02x" % (rgb_r_entry.get(), rgb_g_entry.get(), rgb_b_entry.get())
    vista_previa_canvas.configure(bg=color_c)


def cambia_color_desde_hsv(v):
    hsv_hue = hsv_h_entry.get() / 360
    hsv_saturation = hsv_s_entry.get()/100
    hsv_value = hsv_v_entry.get()/100
    
    r,g,b = hsv_to_rgb(hsv_hue, hsv_saturation, hsv_value)
    r,g,b = int(r*255), int(g*255), int(b*255)
    color_d = "#%02x%02x%02x" % (r,g,b)
    vista_previa_canvas.configure(bg=color_d)

#HEX
cuadro_hex = LabelFrame(ventana,
                             text="COLORES HEX",
                             font=("helvetica", 14),
                             bg="#65B2FF")
cuadro_hex.pack()

hex_label = Label(cuadro_hex,
                  text = "HEX:",
                  bg="#65B2FF")
hex_label.pack()

hex_entry = Entry(cuadro_hex,
                bg="#65B2FF",
                justify=CENTER,
                font=("Courier", 12, "bold"))
hex_entry.bind("<Key>", cambia_color_desde_hex)
hex_entry.pack()

#RGB
cuadro_rgb = LabelFrame(ventana,
                             text="COLORES RGB",
                             font=("helvetica", 14),
                             bg="#65B2FF")
cuadro_rgb.pack()

rgb_r_entry = Scale(cuadro_rgb,
                    from_=0, to=255,
                    bg="red",
                    orient=HORIZONTAL,
                    command=cambia_color_desde_rgb,
                    font=("Courier", 12, "bold"))
rgb_r_entry.pack()

rgb_g_entry = Scale(cuadro_rgb,
                    from_=0, to=255,
                    bg="green",
                    orient=HORIZONTAL,
                    command=cambia_color_desde_rgb,
                    font=("Courier", 12, "bold"))
rgb_g_entry.pack()

rgb_b_entry = Scale(cuadro_rgb,
                    from_=0, to=255,
                    bg="blue",
                    orient=HORIZONTAL,
                    command=cambia_color_desde_rgb,
                    font=("Courier", 12, "bold"))
rgb_b_entry.pack()

#HSV
cuadro_hsv = LabelFrame(ventana,
                             text="COLORES HSV",
                             font=("helvetica", 14),
                             bg="#65B2FF")
cuadro_hsv.pack()

hsv_h_entry = Scale(cuadro_hsv,
                    bg="#65B2FF",
                    orient=HORIZONTAL,
                    from_=0, to=360,
                    command=cambia_color_desde_hsv,
                    font=("Courier", 12, "bold"))
hsv_h_entry.pack()

hsv_s_entry = Scale(cuadro_hsv,
                    bg="#65B2FF",
                    from_=0, to=100,
                    orient=HORIZONTAL,
                    command=cambia_color_desde_hsv,
                    font=("Courier", 12, "bold"))
hsv_s_entry.pack()

hsv_v_entry = Scale(cuadro_hsv,
                    bg="#65B2FF",
                    orient=HORIZONTAL,
                    from_=0, to=100,
                    command=cambia_color_desde_hsv,
                    font=("Courier", 12, "bold"))
hsv_v_entry.pack()

#Vista Previa
cuadro_vista_previa = LabelFrame(ventana,
                             text="Vista Previa del color",
                             font=("helvetica", 14, "bold"),
                             bg="#65B2FF")
cuadro_vista_previa.pack()

vista_previa_canvas = Canvas(cuadro_vista_previa,
                             width=120, height=80,
                             bg="#FFFFFF")
vista_previa_canvas.pack()


ventana.mainloop()