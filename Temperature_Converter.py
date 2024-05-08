print('''
 ______                                                  __                          
/\__  _\                                                /\ \__                       
\/_/\ \/    __    ___ ___   _____      __    _ __    __ \ \ ,_\ __  __  _ __    __   
   \ \ \  /'__`\/' __` __`\/\ '__`\  /'__`\ /\`'__\/'__`\\ \ \//\ \/\ \/\`'__\/'__`\ 
    \ \ \/\  __//\ \/\ \/\ \ \ \L\ \/\ \L\.\\ \ \//\ \L\.\\ \ \\ \ \_\ \ \ \//\  __/ 
     \ \_\ \____\ \_\ \_\ \_\ \ ,__/\ \__/.\_\ \_\\ \__/.\_\ \__\ \____/\ \_\\ \____\
 ____ \/_/\/____/\/_/\/_/\/_/\ \ \/  \/__/\/_/\/_/ \/__/\/_/\/__/\/___/  \/_/ \/____/
/\  _`\                       \ \_\           /\ \__                                 
\ \ \/\_\    ___     ___   __  \/_/  __   _ __\ \ ,_\    __   _ __                   
 \ \ \/_/_  / __`\ /' _ `\/\ \/\ \ /'__`\/\`'__\ \ \/  /'__`\/\`'__\                 
  \ \ \L\ \/\ \L\ \/\ \/\ \ \ \_/ /\  __/\ \ \/ \ \ \_/\  __/\ \ \/                  
   \ \____/\ \____/\ \_\ \_\ \___/\ \____\\ \_\  \ \__\ \____\\ \_\                  
    \/___/  \/___/  \/_/\/_/\/__/  \/____/ \/_/   \/__/\/____/ \/_/                  
                                                                                     
                                                                                     
''')


def temperature_converter():
    choice = input("Enter 'F' to convert from Fahrenheit to Celsius or 'C' to convert from Celsius to Fahrenheit: ")

    if choice.upper() == 'F':
        fahrenheit = float(input("Enter the Fahrenheit value you want to convert: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif choice.upper() == 'C':
        celsius = float(input("Enter the Celsius value you want to convert: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    else:
        print("You made an invalid selection.")

temperature_converter()
