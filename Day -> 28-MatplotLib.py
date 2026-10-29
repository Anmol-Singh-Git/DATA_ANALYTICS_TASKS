#1
pip install matplotlib
import matplotlib.pyplot as plt
x =[1,2,3,4,5]
y = [100,150,200,250,300]


plt.title("Line Chart")
plt.plot(x,y, color = "Red")

plt.ylabel("Money")
plt.xlabel("Number")
plt.show()

#2
x = [1,2,3,4,5]
y=["monday", "tuesday", "Wedneshday", "Thursday","Friday"]

#3
plt.bar(x,y, color="red")
plt.title("Sales day wise")
plt.show()

#4
plt.barh(x,y, color="red")
plt.title("Sales day wise")
plt.show()

#5
plt.title("Scatter Chart")
plt.scatter(x,y)
plt.show()

#6
plt.barh(x,y, color="red")
plt.title("Pie Chart")
plt.pie(a)
plt.show()

#7
a=[10,12,1,4,14,15,16,17,18,22,25,28, 100,150,300]
plt.hist(a, bins=8)
plt.show()

#8
# Boxplot 
a=[10,12,1,4,14,15,16,17,18,22,25,28,100,150]

plt.boxplot(a)
plt.show()

#9
# HOME WORK -> Draw a house structure by line chart

front_wall_x = [2,2,8,8,2]
front_wall_y = [5,0,0,5,5]
plt.plot(front_wall_x,front_wall_y)

back_wall_x = [8,8,17,17,8]
back_wall_y = [5,0,0,5,5]
plt.plot(back_wall_x,back_wall_y)

front_roof_x = [2,5,8]
front_roof_y = [5,8,5]
plt.plot(front_roof_x,front_roof_y)

back_roof_x = [8,17,14,5]
back_roof_y = [5,5,8,8]
plt.plot(back_roof_x,back_roof_y)

door_x = [4,4,6,6]
door_y = [0,3,3,0]
plt.plot(door_x,door_y)

windowL_x = [2.5,2.5,3.5,3.5,2.5]
windowL_y = [3,4,4,3,3]
plt.plot(windowL_x,windowL_y)

windowR_x = [6.5,7.5,7.5,6.5,6.5]
windowR_y = [3,3,4,4,3]
plt.plot(windowR_x,windowR_y)


back_window_x = [10.5,14.5,14.5,10.5,10.5]
back_window_y = [1.25,1.25,3.75,4,1]
plt.plot(back_window_x,back_window_y)

plt.title("House")


plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")
plt.show()
