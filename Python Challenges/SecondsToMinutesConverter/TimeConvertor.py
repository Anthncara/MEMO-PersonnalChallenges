def cevir(i, j):
    global sonuc, z
    a = z // i
    b = z % i
    if a == 0:
        sonuc += ""
        z = b
    else:
        sonuc += str(a) + j
        z -= a*i
print('###  This program converts milliseconds into hours, minutes, and seconds ###\n(To exit the program, please type "exit")')

while True:
    giris = input("Please enter the milliseconds (should be greater than zero) : ")
    if giris.lower() == "exit":
        print('"Exiting the program... Good Bye"')
        break

    sonuc = ""
    sayi = {3600000 : " hour/s ", 60000 : " minute/s ", 1000 : " second/s "}    
    if not giris.isdigit() or int(giris) < 1:
        print("Not Valid Input!!!")
    elif int(giris) < 1000:
        sonuc = "just " + giris + " millisecond/s "    
    else:
        z = int(giris)
        for i in sayi:
            cevir(i, sayi[i])
    print(sonuc)