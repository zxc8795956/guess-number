import random
count = 0 
r = random.randint(1,100)
while True:
	count = count + 1#count += 1
	number = input('請猜數字:')
	number = int(number)
	if number == r:
		print('這是你猜的第', count ,'次')
		print('你猜對了')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
	print('這是你猜的第', count ,'次')
