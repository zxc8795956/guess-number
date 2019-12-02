import random 
r = random.randint.(1,100)
while True:
	number = input('請猜數字:')
	number = int(number)
	if number == r:
		print('你猜對了')
		break
	elif number > r:
		print('比答案大')
	elif number < r:
		print('比答案小')
