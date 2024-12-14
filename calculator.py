import tkinter

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2



def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)




def add():
    num1, num2 = get_values()
    result = num1 + num2
    insert_values(result)



def sub():
    num1, num2 = get_values()
    result = num1 - num2
    insert_values(result)



def div():
    num1, num2 = get_values()
    result = num1 / num2
    insert_values(result)



def mul():
    num1, num2 = get_values()
    result = num1 * num2
    insert_values(result)




window = tkinter.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)
button_add = tkinter.Button(window, text = '+', width = 2, height = 2, command  = add)
button_add.place(x = 100, y = 200)
button_sub = tkinter.Button(window, text = '-', width = 2, height = 2, command  = sub)
button_sub.place(x = 150, y = 200)
button_mul = tkinter.Button(window, text = '*', width = 2, height = 2, command  = mul)
button_mul.place(x = 200, y = 200)
button_div = tkinter.Button(window, text = '/', width = 2, height = 2, command  = div)
button_div.place(x = 250, y = 200)
number1_entry = tkinter.Entry(window, width = 28)
number1_entry.place(x = 100, y = 75)
number2_entry = tkinter.Entry(window, width = 28)
number2_entry.place(x = 100, y = 150)
answer_entry = tkinter.Entry(window, width = 28)
answer_entry.place(x = 100, y = 300)
number1 = tkinter.Label(window, text = 'Введите первое число:')
number1.place(x = 100, y = 50)
number2 = tkinter.Label(window, text = 'Введите второе число:')
number2.place(x = 100, y = 125)
answer= tkinter.Label(window, text = 'Ответ:')
answer.place(x = 100, y = 275)
window.mainloop()
