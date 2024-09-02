num1 = int(input("Mata in priset på första varan: "))
num2 = int(input("Mata in priset på andra varan: "))
num3 = int(input("Mata in priset på tredje varan: "))

total = num1 + num2 + num3
moms = total * 1.25
rabatt = total * 0.1

print()
if total > 500:
    result = moms - rabatt
    print("För att du har handlat mer än 500SEK så erbjuder vi dig en rabatt på 10%.\n Din total summa är: " , result , "SEK")

elif total < 500:
    result = moms
    print("För att du har handlat mindre än 500SEK så kan vi tyvärr inte erbjuda någon rabatt!\n Din total summa är: ", result , "SEK")

else:
    print("Ett problem har uppstod försök igen senare.")
