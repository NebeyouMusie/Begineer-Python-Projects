def convert(temp):
  f = float(temp)
  c = (f - 32) * 5/9
  return c

fahrenheit = int(input("Enter the temperature in fahrenheit: "))
print(convert(fahrenheit))