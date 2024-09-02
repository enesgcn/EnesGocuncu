num1 = int(input("Ange ett tal: "))
num2 = int(input("Ange ett tal: "))
x = input("vad vill du göra med dessa tal: ") #Användaren kan skriva jämförelseoperatorer ( > , < , == , != ) för att jämföra dessa tal 

if x == ">":  # Om användaren skriver ">" då kollar programmet om num1 större än num2
    result = num1 > num2
    print(num1 , "är större än", num2 , result)

elif x == "<": 
    result = num1 < num2
    print(result)

elif x == "==":
    result = num1 == num2
    print(result)

elif x == "!=":
    result = num1 != num2
    print(result)