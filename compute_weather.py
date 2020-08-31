import os


class ComputeWeather():

	def __init__(self, file_location):
		self.file_location = file_location
		self.get_avg_temp()

	def get_avg_temp(self):
		avg_temps = open(self.file_location,'a+')

		avg_temps.write("Rio de Janeiro, Brazil, 30.0,18.0\n")
		avg_temps.seek(0)
		heading = avg_temps.readline()
		headings = heading.split(',')
		city_temp = avg_temps.readline()
		city_list = city_temp.split(',')
		while city_temp:
		    print(headings[0].capitalize(), 'of', city_list[0], headings[2], 'is', city_list[2], 'Celsius')
		    city_temp = avg_temps.readline()
		    city_list = city_temp.split(',')

		avg_temps.close()


if __name__ == '__main__':
	current_location = os.getcwd()
	print ("Current working dir : %s" % current_location)
	ComputeWeather(current_location+'/avg_temp.txt')