
 print("dollars to euros convertion:")#title
while True:#keeps asking untill a yes or no is givin
    Convert = input("would you like to convert")#askes if you want to convert
    if Convert == "yes": #if yes then it converts
        Dollars = float(input("how many dollars do you want to convert?:"))#amount you want to convert
        Euros = Dollars * .94540 #multiplies to convert
        print("Euros " + str(Euros)) #prints conversion
    elif Convert == "no": #if no it breaks
        break