
"""Write a program to calculate BMI of a person after inputting the weight in kgs and height in meters and
then print the nutritional status as per the given table

BMI Nutritional Status
< 18.5 Underweight
18.5-24.9 Normal
25-29.9 Overweight
>= 30 Obese"""


"""----------------------------------------------------------------------1"""
#sol:

weight_in_kg=float(input('Enter weight in kg:'))
height_in_mt=float(input('Enter height in mt:'))
#The formula is BMI = kg/m2
BMI_of_person= weight_in_kg/(height_in_mt * height_in_mt)
print('BMI is:',BMI_of_person)
if (BMI_of_person < 18.5):
        print('UnderWeight')
elif (BMI_of_person >=18.5 or BMI_of_person<=24.9):
        print('Normal')

if(BMI_of_person>=25 or  BMI_of_person<= 29.9):
        print('Overweight')
elif BMI_of_person >=30:
         print('Obess')
    

                   
