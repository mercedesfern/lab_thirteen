

class Delivery_Personal:
	"""docstring for Delivery_Personal"""
	def __init__(self, years_of_service, company, is_drone, zip_codes_covered, name = None):
		self.years_of_service  = years_of_service
		self.company 		   = company
		self.is_drone 		   = is_drone
		self.zip_codes_covered = zip_codes_covered
		self.name 			   = name

##GETTERS
	def get_years_of_service(self):
		return(self.years_of_service)

	def get_company(self):
		return(self.company)

	def get_zip_codes_covered(self):
		return(self.zip_codes_covered)

##SETTERS
	def set_years_of_service(self, d):
		self.years_of_service = d

	def set_company(self, d):
		self.company = d

	def set_zip_codes_covered(self, d):
		self.zip_codes_covered = d

##RECURSIVE MOTHOD FOR DELIVER
	def deliver(self, n, h):
		if(len(n)==1):
			print('delivering to'+ str(n))
		else:

			mid = len(n)//2
			n   = n[mid::]
			h   = n[0:mid]
			# print(n_list[0:mid])
			Delivery_Personal(n)
			Delivery_Personal(h)

			return(Delivery_Personal(n))



def main():
	delivery_house_1 = Delivery_Personal(years_of_service = 2, company = 'Amazon', is_drone = False, zip_codes_covered = 90723) 

	delivery_house_2 = Delivery_Personal(years_of_service = 4, company = 'USPS', is_drone = False, zip_codes_covered = 20016) 
	
	delivery_house_3 = Delivery_Personal(years_of_service = 5, company = 'Amazon', is_drone = True, zip_codes_covered = 95129)
	 
	delivery_house_4 = Delivery_Personal(years_of_service = 1, company = 'Federal Express', is_drone = False, zip_codes_covered = 90240)

	print(deliver(delivery_house_4))




if __name__ == '__main__':
	main()

