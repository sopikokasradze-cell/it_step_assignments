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