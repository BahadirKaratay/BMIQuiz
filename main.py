from tkinter import*

#window
window = Tk()
window.title("BMI QUİZ")
window.minsize(width=400, height=400)

#weight label
weight_label = Label(text="Enter Your Weight(kg)")
weight_label.config(padx=20, pady=20)
weight_label.pack()

#weight entry
weight_entry = Entry(width=10)
weight_entry.focus()
weight_entry.pack()

#height label
height_label = Label(text="Enter Your Height(cm)")
height_label.config(padx=20, pady=20)
height_label.pack()

#height entry
height_entry = Entry(width=10)
height_entry.pack()

#calculate button
def calc_process():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        label1.config(text="Enter both weight and height")

    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            results = result(bmi)
            label1.config(text=results)
        except:
            label1.config(text="Enter valid numbers!!!")

calc_button = Button(text="Calculate", width=10, command=calc_process)
calc_button.pack(pady=10)

def result(bmi):
    result_s = f"Your BMI is {bmi}... You are "
    if bmi > 10 and bmi <= 18.15:
        result_s += "underweight"
    elif bmi > 18.15 and bmi <= 24.9:
        result_s += "normal"
    elif bmi > 24.9 and bmi <= 29.9:
        result_s += "overweight"
    else:
        result_s += "obese"
    return result_s

#result label
label1 = Label()
label1.pack()
window.mainloop()