#车辆数量定义
cars = 100
#车载乘客数量定义
space_in_a_car = 4.0
#司机数量定义
drivers = 30
#乘客数量定义
passengers = 90
#未驾驶的车辆数定义
cars_not_driven = cars - drivers
#驾驶的车辆数定义
cars_driven = drivers
#还可承载乘客的数量定义
carpool_capacity = cars_driven * space_in_a_car
#平均承载乘客数定义
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.") 
print ("There are only", drivers, "drivers available.") 
print ("There will be", cars_not_driven, "empty cars today.") 
print ("We can transport", carpool_capacity, "people today.") 
print ("We have", passengers, "to carpool today.") 
print ("We need to put about", average_passengers_per_car, "in each car.")


#Traceback (most recent call last):
#File "ex4.py", line 8, in <module>
#average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
#行8的"car_pool_capacity"变量未定义

#1.使用4.0和4的区别，就是代入运算时，4.0是浮点类型float，而4是int类型
