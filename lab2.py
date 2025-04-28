print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_BMI(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    BMI=weight/(height*height)
    print("BMI is" + str(BMI))
    if BMI < 18.5:
        print("Underweight")
    if BMI > 18.5 and BMI < 25.0:
        print("normal")
    if BMI > 25.0:
        print("Fat")
    return

calculate_BMI(weight=80, height=1.75)


