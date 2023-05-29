from tkinter import *
from tkinter import ttk


def conv(var1, var2):
    if var1 == 'cm':
        return var2 / 2.54
    elif var1 == 'ich':
        return var2 * 2.54
    elif var1 == 'm':
        return var2 / 0.3048
    elif var1 == 'ft':
        return var2 * 0.3048
    elif var1 == 'km':
        return var2 * 0.621371192
    elif var1 == 'mi':
        return var2 / 0.621371192
    elif var1 == 'kg':
        return var2 / 0.45359237
    elif var1 == 'lbs':
        return var2 * 0.45359237
    elif var1 == 'dlr':
        return var2 * 0.93
    elif var1 == 'eur':
        return var2 / 0.93
    elif var1 == 'zl':
        return var2 * 0.22
    elif var1 == 'eur1':
        return var2 / 0.22
    elif var1 == 'mm':
        return var2 / 1000
    elif var1 == 'mm2':
        return var2 * 1000
    elif var1 == 'cm':
        return var2 / 100
    elif var1 == 'cm2':
        return var2 * 100
    elif var1 == 'dm':
        return var2 / 10
    elif var1 == 'dm2':
        return var2 * 10
    elif var1 == 'decam':
        return var2 * 10
    elif var1 == 'decam2':
        return var2 / 10
    elif var1 == 'hm':
        return var2 * 100
    elif var1 == 'hm2':
        return var2 / 100
    elif var1 == 'km':
        return var2 * 1000
    elif var1 == 'km2':
        return var2 / 1000


def func1(var1):
    if var1 == 'Cm to Inches':
        cm1 = 'cm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(cm1, float(input_box_1.get())))
        return
    elif var1 == 'Inches to Cm':
        ich1 = 'ich'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(ich1, float(input_box_1.get())))
        return
    elif var1 == 'M to Ft':
        m1 = 'm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(m1, float(input_box_1.get())))
        return
    elif var1 == 'Ft to M':
        ft1 = 'ft'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(ft1, float(input_box_1.get())))
        return
    elif var1 == 'Km to Mi':
        km1 = 'km'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(km1, float(input_box_1.get())))
        return
    elif var1 == 'Mi to Km':
        mi1 = 'mi'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(mi1, float(input_box_1.get())))
        return
    elif var1 == 'Kg to Lbs':
        kg1 = 'kg'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(kg1, float(input_box_1.get())))
        return
    elif var1 == 'Lbs to Kg':
        lbs1 = 'lbs'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(lbs1, float(input_box_1.get())))
        return
    elif var1 == 'American $ to €':
        dlr1 = 'dlr'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(dlr1, float(input_box_1.get())))
        return
    elif var1 == '€ to American $':
        eur1 = 'eur'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(eur1, float(input_box_1.get())))
        return
    elif var1 == 'Zl to €':
        zl1 = 'zl'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(zl1, float(input_box_1.get())))
        return
    elif var1 == '€ to Zl':
        eur2 = 'eur1'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(eur2, float(input_box_1.get())))
        return
    elif var1 == 'Mm to M':
        mm1 = 'mm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(mm1, float(input_box_1.get())))
        return
    elif var1 == 'M to Mm':
        mm2 = 'mm2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(mm2, float(input_box_1.get())))
        return
    elif var1 == 'Cm to M':
        cm1 = 'cm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(cm1, float(input_box_1.get())))
        return
    elif var1 == 'M to Cm':
        cm2 = 'cm2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(cm2, float(input_box_1.get())))
        return
    elif var1 == 'Dm to M':
        dm1 = 'dm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(dm1, float(input_box_1.get())))
        return
    elif var1 == 'M to Dm':
        dm2 = 'dm2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(dm2, float(input_box_1.get())))
        return
    elif var1 == 'Decam to M':
        decam1 = 'decam'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(decam1, float(input_box_1.get())))
        return
    elif var1 == 'M to Decam':
        decam2 = 'decam2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(decam2, float(input_box_1.get())))
        return
    elif var1 == 'Hm to M':
        hm1 = 'hm'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(hm1, float(input_box_1.get())))
        return
    elif var1 == 'M to Hm':
        hm2 = 'hm2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(hm2, float(input_box_1.get())))
        return
    elif var1 == 'Km to M':
        km1 = 'km'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(km1, float(input_box_1.get())))
        return
    elif var1 == 'M to Km':
        km2 = 'km2'
        outpt1.delete(0, END)
        outpt1.insert(0, conv(km2, float(input_box_1.get())))
        return
    return


window = Tk()
window.title('Converter')
window.geometry('435x150')
window.resizable(False, False)
window.iconbitmap('logo.ico')

frame1 = Frame(window, height=200, width=200)
frame2 = Frame(window, height=150, width=150)

lbl1 = Label(window, text='Created by falopr', bg='#b0b0b0', fg='#fdfdfd')
lbl2 = Label(frame1, text='Input')
lbl3 = Label(frame1, text='From ? to ?')
lbl4 = Label(frame2, text='Output')
input_box_1 = Entry(frame1, font=('Arial', 10))

lb1 = ['Cm to Inches', 'Inches to Cm', 'M to Ft', 'Ft to M', 'Km to Mi', 'Mi to Km', 'Kg to Lbs', 'Lbs to Kg', 'American $ to €', '€ to American $', 'Zl to €', '€ to Zl', 'Mm to M', 'M to Mm', 'Cm to M', 'M to Cm', 'Dm to M', 'M to Dm', 'Decam to M', 'M to Decam', 'Hm to M', 'M to Hm', 'Km to M', 'M to Km']

cb1 = ttk.Combobox(frame1, values=lb1)
btn1 = Button(frame2, text='Submit', command=lambda: func1(cb1.get()))
outpt1 = Entry(frame2)
lbl1.pack()
frame1.pack(side=LEFT)
frame2.pack(side=RIGHT)
lbl2.pack()
input_box_1.pack(padx=20)
lbl3.pack()
cb1.pack()
btn1.pack(padx=100)
lbl4.pack()
outpt1.pack()

window.mainloop()
