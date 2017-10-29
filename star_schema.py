#python program to implement star schema

class Address:
	def __init__(self):
		self.l_key = 0
		self.street = ""
		self.city = ""
		self.state = ""
		self.country = ""

	def get_details(self):
		self.l_key = input("enter location key :")
		self.street = raw_input("enter street name :")
		self.city = raw_input("enter city name :")
		self.state = raw_input("enter state name :")		
		self.country = raw_input("enter country name :")
		print '---------------------------------------'

	def show_details(self):
		print str(self.l_key)+" "+self.street+" "+self.city+" "+self.state

def main():
	n = input("enter number of adresses :")
	addresses = []
	for k in range(0,n):
		current_address = Address()
		current_address.get_details()
		addresses.append(current_address)

	print "entered table is :"
	for k in addresses:
		k.show_details()

	for k in range(0,n):
		for j in range(k+1,n):
			if addresses[k].city == addresses[j].city and addresses[k].state == addresses[j].state:
				print str(k)+" and "+str(j)+" are redundant"



if __name__ == '__main__':
	main()