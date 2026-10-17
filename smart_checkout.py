cart_total = 180.0            
user_status = "vip"           
has_promo_code = False        
loyalty_points = 520          
delivery_city = "თბილისი"
is_account_active = True

if not is_account_active:
    print("ანგარიში დაბლოკილია. შეკვეთა ვერ დამუშავდა!")
    exit()
if cart_total < 0:
    print("შეცდომა: კალათის ღირებულება არ შეიძლება იყოს უარყოფითი!")
    exit()
elif cart_total == 0:
    print("შეცდომა: კალათა ცარიელია!")
    exit()
print("შეკვეთა მზადდება!")

discount_percent = 0
 
if user_status == "vip":
    discount_percent = 20
    if loyalty_points >= 500:
        discount_percent += 5      # 25%
elif user_status == "regular":
    if has_promo_code or cart_total >= 150:
        discount_percent = 10
    else:
        discount_percent = 0
elif user_status == "admin":
    discount_percent = 50
 
discounted_total = cart_total * (1 - discount_percent / 100)   

if delivery_city in ["თბილისი", "ქუთაისი", "ბათუმი"]:
    if discounted_total >= 100:
        delivery_fee = 0
    else:
        delivery_fee = 5
else:
    delivery_fee = 15
 
final_total = discounted_total + delivery_fee

print("-" * 36)
print("ინვოისი")
print("-" * 36)
print(f"მომხმარებლის სტატუსი: {user_status}")
print(f"მიტანის ქალაქი: {delivery_city}")
print("-" * 36)
print(f"კალათის საწყისი ფასი: {cart_total} ლარი")
print(f"ფასდაკლება: {discount_percent}%")
print(f"ფასდაკლებული თანხა: {discounted_total} ლარი")
print(f"მიტანის საფასური: {delivery_fee} ლარი")
print("-" * 36)
print(f"საბოლოო გადასახდელი თანხა: {final_total} ლარი")