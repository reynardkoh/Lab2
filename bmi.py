def calculate_bmi(height,weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))

    BMI = weight / (height*height)
    print("BMI =" , BMI)

    return BMI

weightinp = float(input("What is your weight?"))
heightinp = float(input("What is your height?"))
bmi=calculate_bmi(heightinp,weightinp)

def weight_class(bmi):
    if bmi<18.5 :
        print("Under Weight")
        return -1
    elif bmi>=18.5 and bmi<=25.0:
        print("Normal Weight")
        return 0
    else:
       print("Over Weight")  
       return 1  

weight_class(bmi)


