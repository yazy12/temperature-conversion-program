while True:
    what_type = input("type a for fahrenheit to celsius - type b for celsius to fahrenheit: ")
    if what_type.lower() == 'a':
        temp = int(input("enter temperature in Fahrenheit: "))
        temp_celi = (temp -32) * 5/9
        print("the temperature in celsius is " + str(temp_celi))
        break 
    elif what_type.lower() == 'b':
        temp = int(input("enter temperature in celsius: "))
        temp_fahr = (temp * 1.8) + 32
        print("the temperature in fahrenheit is " + str(temp_fahr))
        break 
    else:
        print("enter correct value")
        continue 
    

                
