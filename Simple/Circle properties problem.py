diameter = int(input("Enter the diameter of your circle: "))
arc = int(input("Enter the arc of your circle: "))
radius = diameter/2
circumference = 3.14*diameter
print ("Radius: {}".format(radius))
print ("Area: {}".format(3.14*(radius**2)))
print ("Circumference: {}".format(circumference))
print ("Arc: {}".format((circumference*arc)/360))
