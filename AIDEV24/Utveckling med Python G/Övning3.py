pris = int(0)
dricks = int(10)

a = input("tryck 1 för att se menyn: ") #Användaren kan se menyn
if a == "1":
    print("Dagens Meny är \n" , "biryani: 100kr \n" , "sushi: 50kr \n", "kebab: 150kr \n")

print()
print()

b = input("Vad vill du beställa: ") #Användaren kan skriva vad de vill beställa från menyn
if b == "biryani":
    biryani = int(100)
    total = pris + biryani
    print("Biryani kostar", biryani ,"kr")

elif b == "sushi":
    sushi = int(50)
    total = pris +sushi
    print("Sushi kostar", sushi ,"kr")

elif b == "kebab":
    kebab = int(150)
    total = pris + kebab
    print("Kebaben kostar", kebab ,"kr")

print()
print()

c = input("Vill du ge dricks: ") #Användaren kan välja om de vill ge dricks eller inte

if c == "Ja": #Om användaren väljer ge dricks så blir det maten + 10kr
    result = total + dricks
    print("Tack för du gav dricks :) \n Total summan är: ", result)

elif c == "Nej":
    result = total
    print("Total summan är : " , total)


