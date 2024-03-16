user_input = str(input("Enter a phrase: "))
text = user_input.split()

acronym = " "

for i in text:
  acronym += str(i[0]).upper()
  
print(acronym)