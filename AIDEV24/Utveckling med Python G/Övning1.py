num1 = int(input("Ange ett tal: "))  #Omvandlar str till int så programmet fattar att vi skriver ett tal.
num2 = int(input("Ange ett tal: "))
x = input("Skriv vad du vill göra: ") # Användaren kan skriva "+","-","*" och "/" för att göra en beräkning.



if x == "+":           # om användaren skriver "+" då resultatet blir num1 + num2 sedan printar vi resultatet
    result = num1 + num2
    print(result)

elif x == "-":
    result = num1 - num2
    print(result)

elif x == "*":
    result = num1 * num2
    print(result)

elif x == "/":
    result = num1 / num2
    print(result)

else:       #Om användaren skriver någonting annat då printas Hejdå!

    print ("Hejdå!")