print("Välkommen till \"Spring ifrån Enes\"")
print()

start = input("Välj för att starta spelet (Ja/Nej): ") #Användaren kan starta spelet 

print()
if start == "Ja": #Användaren har startat spelet och nu kommer ne scenario.
    print("Du åker med din bil på en landsväg. \n Längre fram ser du en älg som står på vägen \n")
    
print()
val_1 = input("Vad gör du (\"Kör höger\"/ \"Kör på älgen\"): ") #Användaren har 2 alternativt att välja
print()
if val_1 == "Kör höger": #Om användaren väljer detta alternativt så kommer en ny scenario
    print("Du svängde höger och nu är du i skogen \n")
    print("Du fortsätter köra i mörkret.\n Helt plötsigt ser du någon som och gråter vid ett stort trä.\n") 

elif val_1 == "Kör på älgen": #Om användaren väljer detta alternativt så förlorar han.
    print("Du trodde det var en älg fast det var en sten så du är DÖD! \n GAME OVER!")

tree = input("Du närmar dig till personen och ser att det står E på hans panna.\n\n  Han ser jätteläskigt ut och stirrar rakt in i dig\n\n Du säger:\n - hej vad heter du?\n och han säger:\n -YAG HETA !!ENES!! YAG MUKKE HONGRIG!!\n \n Han försöker ställa sig upp vad gör du (Spring/Hjälpa)? ")
 
if tree == "Spring": #Om användaren väljer denna alternativt så vinner hen spelet
    print()
    print("GRATTIS!! Du lyckades fly ifrån Enes!!!")

elif tree == "Hjälpa": #Om användaren väljer denna alternativt så förlorar de.
    print()
    print("Enes var jätte hungrig så han åt upp dig istället!! \n GAME OVER!!!")
