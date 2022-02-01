length = int(input("Enter your length of the fish tank: "))
depth = int(input("Enter your depth of the fish tank: "))
height = int(input("Enter your height of the fish tank: "))

litres = depth*length*height/1000
print ("You'll need {} litres and {} gallons".format(litres,litres * 0.219969))
