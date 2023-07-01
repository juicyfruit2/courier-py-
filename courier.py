# Creating a Program for a courier company to calculate the cost of sending a parcel 

# Asking the user to enter the price of an item 
Price = float(input("Enter the price of the item you would like to purchase:"))

# Asking the user to enter the distance of the deliverly 
Total_Distance = float(input("Enter the total distance of the delivery in:"))
print(Price)
print(Total_Distance)

# using if, else statements to determie what user wants multiplied by the the distance 
air_freight = input("Do you want air or freight.Enter air or freight:?")
if air_freight == "air":
    print(Total_Distance * 0.3) 
else:
     print(Total_Distance * 0.25)

# using if,else statements to calcute if user wants full or limted insurance multiplied by the price 
full_limited = input("Do you want full insurance or limited insurance.Enter full or limted :?")
if full_limited== "full insurance":
    print(Price * 50.00)
else:
    print(Price * 25.00)
# using if,else statements to calculate if user prefers gift or no gift multiplied by the price 
gift_no_gift = input ("Do you want gift or no gift.Enter gift or no gift:")
if gift_no_gift == "gift":
    print(Price * 15.0)
else:
    print(Price * 0.00)
 # using if,else statments to calculate if user wants priority or standard delivery    
priority_or_standard  = input("Do you want priority or standard delivery.Enter priority or standard:")
if priority_or_standard == "priority":
    print(Price * 100)
else:
    print(Price * 20.00)

# Adding up all the anwers to get the Total coast 
Total_Cost = Total_Distance * 0.3 + Total_Distance * 0.25 + Price * 50 + Price * 25 + Price * 15 + Price * 0.00 + Price * 100 + Price * 20.00
print(Total_Cost)