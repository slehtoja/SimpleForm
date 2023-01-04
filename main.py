from tkinter import *  # Impordime graafilise liidese

from Circle import Circle


def is_float(string):  # Kui on number siis arvuta kui teks näita error
    try:
        float(string)
        return True
    except ValueError:
        return False


def calculate(event):  # kuvab texti ja arvutused text_fieldile
    # print('Button clicked')  # Test!
    radius = user_input.get()
    # print(radius)  # Test!
    if is_float(radius):
        user_input.delete(0, END)  # tühjendab texti välja peale entry ja nupu vajutust
        radius = float(radius)  # now is radius float
        circle = Circle(radius)
        txt_field['state'] = 'normal'  # can change field
        txt_field.delete('1.0', END)  # Clear text_field in 1 to end
        txt_field.insert(END, 'Radius: ' + str(circle.radius) + '\n')
        txt_field.insert(END, 'Diameter: ' + str(circle.get_diameter()) + '\n')
        txt_field.insert(END, 'Area: ' + str(circle.get_area()) + '\n')
        txt_field.insert(END, 'Perimeter: ' + str(circle.get_perimeter()) + '\n')
        txt_field['state'] = 'disabled'  # user can´t change field

    # print('Number')  # Test!
    # else:  # Test!
    # print('Error')  # Test!


# Main window properties
window = Tk()  # Loob graafilise akna
window.title('Geometry')  # Titel text
# window.geometry('400x500')  # # Akna suurus laius/w=400, kõrgus/h=500
window.resizable(False, False)  # True width, False height(laiust saab muuta kõrgust ei saa muuta)

# Frames
frame_top = Frame(window, bg='#89CFF0', height=50)  # Loome ülemise frame. bg = frame värv. Heiht= frame kõrgus pixlites
frame_top.pack(fill='both')  # paneb frame põhi aknale. fill= tähendab kuidas ta täidab(laiuse täidab täielikult)

frame_bottom = Frame(window, bg='#90EE90', height=50)  # Loome alumise Frame
frame_bottom.pack(fill=BOTH)  # paneb frame põhi aknale. fill= tähendab kuidas ta täidab(laiuse täidab täielikult)


# First Line in frame top
lbl = Label(frame_top, text='Circle radius', bg='#89CFF0')  # Loome lable ülemisele frameile ja paneme texti ja värvi
lbl.pack(side='left')  # kleebime labeli framei külge ja ütleme kus ta asub

user_input = Entry(frame_top)  # Loome Entry kasti ülemisele frameile kuhu kirjutada
user_input.pack(side='left')
user_input.focus()   # lisab textikursori entry kasti

btn_calc = Button(frame_top, text='Calculate', command=lambda: calculate(0))  # lisame calculate nupu ülemisele Frameli
btn_calc.pack(side=LEFT, padx=2, pady=2)  # nupu asukoht ja padx= ja pady= pixlite arv servast, et näha värvi nupu ümber

# second Line, one big textfield

txt_field = Text(frame_bottom, state=DISABLED)   # lisame teksti välja alumisele frameile, state= disabled(ei luba jama kirjutada)
txt_field.pack(side=LEFT, padx=2, pady=2)

# Bind Entry key
window.bind('<Return>', lambda event: calculate(event))  # lubab kasutada Entrit et ei peaks kasutama hiirt

# No mvc last line
window.mainloop()  # Et aken jääks lahti mitte ei läheks kinni ( sisse on ehitatud for loop)
