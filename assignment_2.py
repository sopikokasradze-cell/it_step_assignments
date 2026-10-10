first_name = "sopiko"
last_name = "kasradze"
favourite_language = "python"
birth_year = 2001
upper_first_name = first_name.upper()
upper_last_name = last_name.upper()
upper_language = favourite_language.upper()
current_year = 2026
age = current_year - birth_year
is_adult = age >= 18
print(upper_first_name, "|", upper_last_name,"|", age,"|",upper_language,"|",is_adult)


name = input("შეიყვანეთ თქვენი სახელი")
surname = input("შეიყვანეთ თქვენი გვარი")
birth_year = int(input("შეიყვანეთ დაბადების წელი"))
language = input("შეიყვანეთ საყვარელი პროგრამირების ენა")

name = name.upper()
surname = surname.upper()
language = language.upper()

age = 2026 - birth_year
is_adult = age >= 18
print(name, "|", surname, "|", age, "|", language, "|", is_adult)

score = int(input("შეიყვანეთ მოსწავლის მიღებული ქულა (მაქსიმუმ 20)"))

grade = score // 2
print("მოსწავლის ქულაა 10 ბალიან სისტემაში:", grade)