#python script to represent snowflake schema
class City:
	def __init__(self,city_key):
		self.city_key = city_key
		self.city_name = ""
		self.city_state = ""
		self.city_country = ""

	def get_data(self):
		self.city_name = raw_input("enter city name :")
		self.city_state = raw_input("enter state name :")
		self.city_country = raw_input("enter country name :")
		print "--------------------------------------------"

	def show_details(self):
		print str(self.city_key)+" "+self.city_name+" "+self.city_state+" "+self.city_country


class Address:
	def __init__(self):
		self.l_key = 0
		self.street = ""
		self.city_key = 0
		self.city = None

	def get_data(self):
		self.l_key = input("enter location key :")
		self.street = raw_input("enter the street name :")
		self.city_key = input("enter city key :")
		self.city = City(self.city_key)
		self.city.get_data()
		print "--------------------------------------------"

	def show_details(self):
		print str(self.l_key)+" "+self.street+" "+str(self.city_key)

def main():
	n = input("enter the number of addresses :")
	addrs = []
	for k in range(0,n):
		addr = Address()
		addr.get_data()
		addrs.append(addr)

	print "address details are:"
	for k in addrs:
		k.show_details()

	print "city details are:"
	for k in addrs:
		k.city.show_details()

	for k in range(0,n):
		for j in range(k+1,n):
			if addrs[k].city.city_state == addrs[j].city.city_state and addrs[k].city.city_country == addrs[j].city.city_country:
				print "redundancy between "+str(k)+" and "+str(j)
			else:
				print "no redundancy between "+str(k)+" and "+str(j)

if __name__ == '__main__':
	main()