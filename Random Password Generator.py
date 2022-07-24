import random




capital_alpha = "ABCDEFGHJKLMNPQRSTUVWYZ"


small_alpha = "abcdefghjklmnopqrstuvwxyz"

num = "1234567890"

sympol = "_"

countainer = capital_alpha + small_alpha + num + sympol

length = int([7 , 10])

password = "".join(random.sample(countainer, length))

print(password)
