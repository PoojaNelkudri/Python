
w1 = float(input('Enter the width of wall : '))
h1 = float(input('Enter the height of a wall: '))

w2 = float(input('Enter the width of wall2 : '))
h2 = float(input('Enter the height of a wall2: '))

Area1 = w1 * h1
print("Area of a wall 1 is: %.2f" %Area1)      
cost1= Area1 * 120
print(" Painting cost of wall 1 with width",w1,"and height ",h1, "and the area of",Area1,"cost of wall1 is :" ,cost1,"per/sq mt")
Area2 = w2 * h2
print("Area of a wall 2 is: %.2f" %Area2)      
cost2= Area2 * 120
print("Painting cost of wall 2 with width",w2,"and height ",h2, "and the area of",Area2,"cost of wall2 is :" ,cost2,"per/sq mt")

total= cost1+cost2
print ("Total cost of both wall is ",total)
