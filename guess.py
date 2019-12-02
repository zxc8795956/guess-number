import random
start = input('請決定隨機變數開始值')
end = input('請決定隨機變數結束值')
start = int(start)
end = int(end)
count = 0 
r = random.randint(start,end)
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
