from tkinter import *
import tkinter as tk
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=san+francisco&appid=6b114fcfb69a1bb0c2b6c39fd3bfdad2'
result = requests.get(url)
json = result.json()
sf_temp = json['main']['temp']

# from tkinter import font as tkfont
window=Tk()
window.title('Weather Forecast')
window.geometry("635x600+10+10")
window.configure(bg='MintCream')

#frames
titleframe = tk.Frame()
titleframe.pack()
todayframe = tk.Frame()
todayframe.pack()

#Label
lbl=tk.Label(titleframe, text="Weather Py-cast", font=("Courier", 30, 'bold'), foreground='black', background='PapayaWhip')
lbl.pack()

#Button
btn1=tk.Button(titleframe, text="Today's Weather", fg='SlateBlue', bg='pink', command=lambda:show_todayframe())
btn1.pack()

#Today's Weather
def show_todayframe():
    titleframe.destroy()
    # todayframe = tk.Frame()
    # todayframe.pack()
    lbl2=tk.Label(todayframe, text="San Francisco, CA", font=("Courier", 20, 'bold'), foreground='black', background='AliceBlue')
    lbl2.pack()


#temperature: F = 9/5(K - 273) + 32
    F = 9/5*(sf_temp - 273) + 32
    F = round(F, 2)
    lbl3 = tk.Label(todayframe, text = 'Temp (F): ' + str(F),bg='MintCream', font=("Courier", 20, 'bold'))
    lbl3.pack()
  
    C = (F - 32) / 1.8
    C = round(C)
    lbl4 = tk.Label(todayframe, text = ' Temp (C): ' + str(C), bg='MintCream', font=("Courier", 20, 'bold'))
    lbl4.pack()

    btnback=tk.Button(todayframe, text="Click to view the hidden note!", fg='SlateBlue', bg='LightPink',command=lambda:show_titleframe())
    btnback.pack()

#Thank you Note
def show_titleframe():
    todayframe.destroy()
    titleframe = tk.Frame()
    titleframe.pack()
    lbl=tk.Label(titleframe, text="Thank you for viewing our project!\nHave a good day!", font=("Courier", 13, 'bold'), foreground='RosyBrown', bg="MintCream")
    lbl.pack()

window.mainloop()

#Thank you Note（word）
import time
sentence = "Thank you"
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-30, 30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\n'.join(allChar))
   time.sleep(1)

window.mainloop()

