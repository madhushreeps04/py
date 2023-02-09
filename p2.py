import random
def display(room):
    print(room)

m = int(input("Enter number of floors "))
n = int(input("Enter number of rooms "))
room = [[random.choice([0,1]) for x in range(n)] for y in range(m)]
print("Before cleaning in the room I detected")
display(room)
z=0
for x in range(m):
    for y in range(n):
        if room[x][y] == 1:
            room[x][y]=0
    print("Room is cleaned",x,y)
z+=1
pro = (100-((z/16)*100))
print("Room is clean now")
display(room)
print("Performance :",pro,"%")
