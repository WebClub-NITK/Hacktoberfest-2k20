import PySimpleGUI as sg

sg.theme('LightBrown9')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('BMI CALCULATOR')],
            [sg.Text('Enter height in meters'), sg.InputText()],
            [sg.Text('Enter weight in kg'), sg.InputText()],
            [sg.Button('Calculate')] ]

# Create the Window
window = sg.Window('BMI', layout)
msg = ''
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:	# if user closes window or clicks cancel
        break
    #BMI calculation
    BMI = float(values[1])/(float(values[0])*float(values[0]))
    if BMI <18.5:
        msg = 'Underweight - BMI less than 18.5'
    elif BMI<25:
        msg = 'Normal healthy weight - BMI between 18.5 and 24.9'
    elif BMI<30:
        msg = 'Overweight - BMI between 25.0 and 29.9'
    elif BMI<40:
        msg = 'Obese - BMI between 30.0 and 39.9'
    elif BMI>=40:
        msg = 'Morbidly obese – BMI 40.0 and above'
    sg.popup('Your BMI is: ', BMI, "kg/m²\n",msg)


window.close()