Height = float(input("Enter your height in centimeters: "))
Weight = float(input("Enter your Weight in kg: "))
Height = Height / 100
BMI = Weight/(Height * Height)
print("your Body Mass Index is: ", BMI)
if(BMI > 0):
  if (BMI <= 16):
    print("you are severley underweight")
  elif(BMI <= 18.5):
    print("you are underweight")
  elif(BMI <= 25):
    print("You are healthy")
  elif(BMI <= 30):
    print("you are overweight")
  else: 
    print("You are severley overweight")
else:
  print("Please enter valid details")