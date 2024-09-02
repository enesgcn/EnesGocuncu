num1 = input("Ange ett tal: ")  #Användaren matar in ett tal
num1 = int(num1)        #Talet omvandlas till int

if num1 %2 == 0:  #Om användarens tal kan delas med 2 då blir resultatet jämnt
    print("Talet du har angett är en jämnt tal", num1 %2)

elif num1 %2 != 0:   #Om användarens tal kan inte delas med 2 då blir resultatet udda.
    print("Talet du har angett är en udda tal" , num1 %2)
