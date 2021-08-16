print("Welcome to Dhruv's Biology Calculator")
bio=str(input('Enter the calculation(no capital letters(single word)): '))

if(bio=='ph'):
    concentration=float(input('Enter the hydrogen concentration:'))
    ph=-log(concentration)
    print('%0.3f is the pH.' %(ph))
if(bio=='BMI'):
    Height=float(input("Enter your height in inches: "))
    Weight=float(input("Enter your Weight in lbs: "))
    BMI=(Weight/(Height*Height))*703
    print("your Body Mass Index is: ",BMI)
if(bio=='BMI2'):
    Height=float(input("Enter your height in centimeters: "))
    Weight=float(input("Enter your Weight in Kg: "))
    Height = Height/100
    BMI=Weight/(Height*Height)