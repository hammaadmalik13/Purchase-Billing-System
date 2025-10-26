print("Bill for Purchasing Items")
print("Discount Rules:")
print("5000 above = 20% discount")
print("3000 above = 15% discount")
print("1000 above = 10% discount")
print("Below 1000 = No discount")

total_original = 0
total_discount = 0
total_final = 0

print("\n" + "=" * 20)
print("Shoes:")
print("=" * 20)

print("Shoes")
price1 = float(input("Enter Price: $"))
if price1 >=5000:
    discount1 = price1 *0.20
elif price1 >=3000:
    discount1 = price1 *0.15
elif price1 >=1000:
    discount1 = price1 *0.10
else:
    discount1 = 0
    
final1 = price1 - discount1
total_original += price1
total_discount += discount1
total_final += final1

print("\n" + "=" * 20)
print("Jeans:")
print("=" * 20)

print("Jeans")
price2 = float(input("Enter price: $"))
if price2 >= 5000:
    discount2 = price2 *0.20
elif price2 >=3000:
    discount2 = price2 *0.15
elif price2 >=1000:
    discount2 = price2 *0.10
else:
    discount2 = 0
final2 = price2 - discount2
total_original += price2
total_discount += discount2
total_final += final2

print("\n" + "=" * 20)
print("T-Shirt:")
print("=" * 20)

print("T-Shirt")
price3 = float(input("Enter price: $"))
if price3 >=5000:
    discount3 = price3 *0.20
elif price3 >=3000:
    discount3 = price3 *0.15
elif price3 >=1000:
    discount3 = price3 *0.10
else:
    discount3 = 0
final3 = price3 - discount3
total_original += price3
total_discount += discount3
total_final += final3

print("\n" + "=" * 30)
print("INDIVIDUAL BILLS:")
print("=" * 30)

print("shoes")
print("Original Price: $", (price1))
print("Discount: $", (discount1))
print("Final Price: $", (final1))

print("Jeans")
print("Original Price: $", (price2))
print("Discount: $", (discount2))
print("Final Price: $", (final2))

print("T-shirt")
print("Original Price: $", (price3))
print("Discount: $", (discount3))
print("Final Price: $", (final3))

print("\n" + "=" * 30)
print("FINAL BILL SUMMARY:")
print("=" * 30)
print("Final Bill")
print("Total Original Price: $", (total_original))
print("Total Discount: $", (total_discount))
print("Final Amount: $", (total_final))