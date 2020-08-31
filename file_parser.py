import sys
import os


class FileParser():

    def __init__(self, filelocation):
      self.filelocation = filelocation
      input_data = self.read_file()
      print("File contents: {}".format(input_data))

    def read_file(self):
      file_contents = ""
      with open(self.filelocation, "r") as f:
         file_contents="".join(each_line.rstrip() for each_line in f)
      return file_contents


if __name__ == '__main__':
   current_location = os.getcwd()
   print ("Current working dir : %s" % current_location)
   file_location = current_location+'/phrases.txt'
   FileParser(file_location)