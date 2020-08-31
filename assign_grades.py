import os

class AssignGrades():
    """ User is given a grade and test report for items correct and incorrect."""

    def __init__(self, file_location, subject):
        self.file_location = file_location
        if subject == 'chem':
            self.chem_assign_grades()

    def get_names(self):
        e_temp = []
        print("Please enter 5 elements from the first 20 in the periodic table")
        while len(e_temp) < 5:
            elem = (input("Please enter element: ")).lower()
            if elem in e_temp:
                print ("Duplicate entered")
            elif len(elem) == 0:
                print("No value entered")
            else:
                e_temp.append(elem)
        return e_temp

    def compute_grades(self, element_file):
        tmp_element_list = []
        element_list = element_file.readline()

        while element_list:
            tmp_element_list.append(element_list.strip().lower())
            element_list = element_file.readline()
        e_list = self.get_names()
        correct_list = []
        mistake_list = []
        for temp in range(5):
            if e_list[temp] in tmp_element_list:
                correct_list.append(e_list[temp])
            else:
                mistake_list.append(e_list[temp])
            
        correctpercent = (int(len(correct_list)))*20

        print ("Score: ", correctpercent, "%")
        print ("Found: ",correct_list)
        print("Not Found:", mistake_list)

    def chem_assign_grades(self):
        element_file = open(self.file_location,'r')
        self.compute_grades(element_file)


if __name__ == '__main__':
    current_location = os.getcwd()
    print ("Current working dir : %s" % current_location)
    AssignGrades(current_location+'/elements1_20.txt', 'chem')
            
            
            
            
            

