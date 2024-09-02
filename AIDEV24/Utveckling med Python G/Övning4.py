print("Skriv in dina tal som du ska beräkna och sätt ett mellanslag mellan varje tal")
listVärden = [float(x) for x in input().split()]
listSummma = sum (listVärden)
listLängd = len (listVärden)
listMedelvärde = listSummma /listLängd 
    
print("Ditt medelvärde är: " + str(listMedelvärde))