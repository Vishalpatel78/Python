import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
# mint = int(time.strftime('%M'))
# print(mint)
# sec = int(time.strftime('%S'))
# print(sec)

if( hour>0 and hour <12 ):
    print("Good Morning sir")

elif(hour > 12 and hour < 17):
    print("Good after noon sir")

else:
    print("Good evening sir")

