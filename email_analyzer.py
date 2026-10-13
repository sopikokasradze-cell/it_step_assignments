import re
text = "ჩვენი გუნდის წევრები არიან: mari.tavadze@itstep.com, მეგობარი ლიზი dima123@gmail.com და კიდევ ერთი ტესტური მისამართი test_user@yahoo.com"
pattern = r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, text)
print(emails)

result = "+".join(emails) #ლისთის გადაქცევა ერთ სტრინგად ელემენტები გაერთიანებული "+" -ით
print(result)