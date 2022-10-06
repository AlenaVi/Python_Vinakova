name = input("Введите имя: ") #Введем имя
surname = input("Введите фамилию: ") #Введем фамилию
date = int(input("Введите год рождения: ")) #Введем год рождения
print (name, surname, date, sep="_" )
name, surname = surname, name
date = date+60
print (name, surname, date)



             
             
            
