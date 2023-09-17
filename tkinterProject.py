from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.config(padx= 30, pady=30)


def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        result_label.config(text="enter both weight and height")

    else:
        try: #dene
            bmi = float(weight)/ (float(height) /100) **2
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except: # olmazsa yapılacak işlem
            result_label.config(text="Enter a valid number")

#ui
weight_input_label =  Label(text="Enter Your Weight (kg)")
weight_input_label.pack()

weight_input = Entry(width=10)
weight_input.pack()

height_input_label =Label(text="Enter Your Height (cm)")
height_input_label.pack()

height_input= Entry(width=10)
height_input.pack()


calculate_button = Button(text="Calculate" , command=calculate_bmi)
calculate_button.pack()

result_label= Label()
result_label.pack()



def write_result(bmi):
    result_string =  f"Your BMİ is : {round(bmi,2)} You are "
    if bmi <= 16:
        result_string+= "Several thin !"
    elif 16 < bmi <= 17:
        result_string += "Moderate Thinness"
    elif 17 < bmi <= 18.5:
        result_string += "Mild Thinness"
    elif 18.5 < bmi <= 25:
        result_string+="Normal"
    elif 25 < bmi <= 30:
        result_string += "Overweight"
    elif 30 < bmi <= 35:
        result_string += "Obese Class 1"
    elif 35 > bmi >= 40:
        result_string+= "Obese Class"
    elif bmi >40:
        result_string+= "Obese Class"
    return result_string



window.mainloop()