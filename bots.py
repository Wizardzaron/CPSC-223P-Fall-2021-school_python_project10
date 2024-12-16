import threading
import json
import time
def bot_clerk(item_list):
	cart_list = []
	lock = threading.Lock()
	list_1 = []
	list_2 = []
	list_3 = []
	for i, item in enumerate(item_list):
		if i % 3 == 0:
			list_1.append(item)
		elif i % 3 == 1:
			list_2.append(item)
		else:
			list_3.append(item)

	t = threading.Thread(target=bot_fetcher, args=(list_1,cart_list,lock))
	t2 = threading.Thread(target=bot_fetcher, args=(list_2,cart_list,lock))
	t3 = threading.Thread(target=bot_fetcher, args=(list_3,cart_list,lock))
	#cart_list.append(t)
	t.start()
	t2.start()
	t3.start()
	t.join()
	t2.join()
	t3.join()

	return cart_list

def bot_fetcher(item_list, cart_list,lock):
	dict = []
	try:
                with open("inventory.dat", 'r') as a:
                        dict = json.load(a)
	except FileNotFoundError:
		print ("File not found")

	for n in (item_list):
		time.sleep(dict[n][1])
		lock.acquire()
		list = []
		list.append(n)
		list.append(dict[n][0])
		cart_list.append(list)
		lock.release()

