Restaurant_name = str(input ("What is the restaurant name? "))
Location = str(input ("What is the location? "))
Dish_1 = str(input ("What is dish 1? "))
Dish_1_rating = float(input ("What is the rating of dish 1? "))
Dish_2 = str(input ("What is dish 2? "))
Dish_2_rating = float(input ("What is the rating of dish 2? "))

if Dish_1_rating + Dish_2_rating >= 12:
    wouldireturn = "yes"
else:
    wouldireturn = "no"


print ("Restaurant Name:" + Restaurant_name)
print ("Location:" + Location)
print ("Dish 1:" + Dish_1)
print ("Dish 1 rating:" + str(Dish_1_rating))
print ("Dish 2:" + Dish_2)
print ("Dish 2 rating:" + str(Dish_2_rating))
print ("Would I return? " + wouldireturn)
