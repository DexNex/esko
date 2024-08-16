# Esko is a simple program that helps humans.
# Created on August 17, 2022.
import datetime
print ("乇丂匚ㄖ".center(20,"="))
print ("\n A Tool to Help You")
print("\n")
print("Created on August 17, 2022")
name = input("What is your name: ")
print ("Welcome:", name)
print ("Menu:")
print ("\n 1.Area Calculator \n 2.Calculator \n 3.Text Spam \n 4.Temperature Conversion \n 5.Convert Number to Binary, Hex, Octal Format \n 6.Count Characters \n 7.Repeat Sentence \n 8.Convert All to Uppercase or Lowercase \n 9.Check Character \n 10.Check Day in Date, Month, Year".upper())

choice = int(input("Enter your choice: "))
if choice == 1:
  print("\n 1.Rectangle Area \n 2.Square Area \n 3.Triangle \n 4.Circle")
  # submenu
  area_choice = int(input("\n Enter your choice:"))
  if area_choice == 1:
     length = int(input("Length:"))
     width = int(input ("Width: "))
     result = length * width
     print("The result is:", result)
  elif area_choice == 2:
     side = int(input("Side:"))
     result = side * side
     print ("The result is:", result)
  elif area_choice == 3:
     base = int(input("Base:"))
     height = int(input("Height:"))
     result = 0.5 * base * height
     print ("The result is:", result)
  elif area_choice == 4:
     radius = int(input("Radius:"))
     result = 3.14 * radius * radius
     print ("The result is:", result)
  else:
      print("Invalid input")
      
elif choice == 2:
  print("\n 1.Standard Calculator \n 2.Magic Calculator\n")
  calculator_choice = int(input("Enter your choice:"))
  if calculator_choice == 1:
      print ("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n")
      operation = int(input("Enter your choice:"))
      if operation == 1:
          a = int(input("Enter value A: "))
          b = int(input("Enter value B: "))
          print (f"Result: {a+b:,}")
      elif operation == 2:
          a = int(input("Enter value A: "))
          b = int(input("Enter value B: "))
          print (f"Result: {a-b:,}")
      elif operation == 3:
          a = int(input("Enter value A: "))
          b = int(input("Enter value B: "))
          print (f"Result: {a*b:,}")
      elif operation == 4:
          a = int(input("Enter value A: "))
          b = int(input("Enter value B: "))
          print (int(f"Result: {a/b:,}"))
      else:
          print("Invalid input")
      
elif choice == 3: 
      text = input("Enter text: ")
      start_value = int(input("Enter the start value (no commas): "))
      end_value = int(input("Enter the end value (no commas): "))
      while start_value <= end_value:
          print (text, start_value)
          start_value += 1
          
elif choice == 4:
      print ("\nTEMPERATURE CONVERSION\n")
      print ("1.Celsius \n2.Reaumur \n3.Fahrenheit \n4.Kelvin\n")
      temperature_choice = int(input("Enter your choice:"))
      if temperature_choice == 1:
          temperature = float(input("Enter temperature in Celsius: "))
          reaumur = (4/5) * temperature
          fahrenheit = ((9/5) * temperature) + 32
          kelvin = temperature + 273
          print ("\nTemperature in Celsius:", temperature)
          print("\nTemperature in Reaumur:", reaumur)
          print("Temperature in Fahrenheit:", fahrenheit)
          print("Temperature in Kelvin:", kelvin)
          
      elif temperature_choice == 2:
          temperature_r = float(input("Enter temperature in Reaumur: "))
          celsius = 5/4 * temperature_r
          fahrenheit = ((9/4) * temperature_r) + 32
          kelvin = ((5/4) * temperature_r) + 273
          print ("\nTemperature in Reaumur:", temperature_r)
          print("\nTemperature in Celsius:", celsius)
          print("Temperature in Fahrenheit:", fahrenheit)
          print("Temperature in Kelvin:", kelvin)
          
      elif temperature_choice == 3:
          temperature_f = float(input("Enter temperature in Fahrenheit: "))
          celsius = 5/9 * (temperature_f - 32)
          reaumur = 4/5 * (temperature_f - 32)
          kelvin = ((temperature_f - 32) * 5/9) + 273.15
          print ("\nTemperature in Fahrenheit:", temperature_f)
          print("\nTemperature in Celsius:", celsius)
          print("Temperature in Reaumur:", reaumur)
          print("Temperature in Kelvin:", kelvin)
          
      elif temperature_choice == 4:
          temperature_k = float(input("Enter temperature in Kelvin: "))
          celsius = (temperature_k - 273)
          reaumur = 4/5 * (temperature_k - 275)
          fahrenheit = (((temperature_k - 32) * 5/9) + 273.15)
          print ("\nTemperature in Kelvin:", temperature_k)
          print("\nTemperature in Celsius:", celsius)
          print("Temperature in Reaumur:", reaumur)
          print("Temperature in Fahrenheit:", fahrenheit)
      
      else:
          print("Invalid input")
          
elif choice == 5:
    number = int(input("Enter a number: "))        
    print("In Binary:", format(number, "08b"))
    print(f"In Hexadecimal: {hex(number)}")   
    print(f"In Octal: {oct(number)}")
                             
elif choice == 6:
    input_text = input("Enter text: ")
    print("Total characters + spaces:", len(input_text))                     
elif choice == 7:
    input_text = input("Enter text: ")
    repeat_count = int(input("Enter the number of repetitions: "))
    result = input_text * repeat_count
    print(result)

elif choice == 8:
    print("""
    1.Uppercase
    2.Lowercase
    """)
    conversion_choice = int(input("Enter your choice: "))
    if conversion_choice == 1:
        sentence = input("Enter text: ")
        uppercase = sentence.upper()
        print(uppercase)
        
    elif conversion_choice == 2:
        sentence = input("Enter text: ")
        lowercase = sentence.lower()
        print(lowercase)
    else:
        print("Invalid choice")
        
elif choice == 9:
    text = input("Enter a sentence: ")
    word_to_check = input("Enter the word you want to check for: ")
    exists = word_to_check in text
    if exists:
        print("Exists")   
    else:
        print("Does not exist")
         
elif choice == 10:
    day = int(input("Day: "))
    month = int(input("Month: "))  
    year = int(input("Year: "))  
    date = datetime.date(year, month, day)
    day_of_week = f"{date:%A}"
    is_sunday = day_of_week == "Sunday"
    is_monday = day_of_week == "Monday"
    is_tuesday = day_of_week == "Tuesday"
    is_wednesday = day_of_week == "Wednesday"
    is_thursday = day_of_week == "Thursday"
    is_friday = day_of_week == "Friday"
    is_saturday = day_of_week == "Saturday"
    today = datetime.date.today()
    days_elapsed = today - date
    years_elapsed = days_elapsed // 365
    months_elapsed = years_elapsed * 12
    if is_sunday:
        print(f"On: {date} It was a Sunday")
    elif is_monday:
        print(f"On: {date} It was a Monday")
    elif is_tuesday:
        print(f"On: {date} It was a Tuesday")
    elif is_wednesday:
        print(f"On: {date} It was a Wednesday")
    elif is_thursday:
        print(f"On: {date} It was a Thursday")
    elif is_friday:
        print(f"On: {date} It was a Friday")
    elif is_saturday:
        print(f"On: {date} It was a Saturday")
    print("It has been", days_elapsed.days, "days")
    print("It has been", months_elapsed.days, "months")
    print ("It has been", years_elapsed.days, "years")
else:
    print("Invalid input")
