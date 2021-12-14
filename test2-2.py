# Yongdong Xi
initial_velocity = input("What is initial velocity of the car in meters-per-second? ")
final_velocity = input("What is final velocity of the car in meters-per-second? ")
time = input('How many seconds the car used? ')

Average_acceleration = (int(final_velocity) - int(initial_velocity)) / int(time)
print('the average acceleration of this car is {0}'. format(Average_acceleration))
