name = input("შეიყვანეთ თქვენი სახელი")
surname = input("შეიყვანეთ თქვენი გვარი:")
platform = input("აირჩიეთ პლატფორმა (მაგალითად: gmail.com, itstep.ge, yahoo.com): ")

name = name.strip().lower()
surname = surname.strip().lower()

name_part = name[:2] 

#(f-string)
email = f"{name.lower()}.{surname.lower()}@{platform}"
print(email)
print()
print()
print("თქვენი ელფოსტა წარმატებით შეიქმნა!")