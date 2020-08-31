from file_parser import FileParser
import os

class FilterSequence():

    def __init__(self, filelocation, filter_letter):
      self.filelocation = filelocation
      file_contents = FileParser(filelocation).read_file()
      print("File contents: {}".format(file_contents))
      filtered = self.first_letter_filter(filter_letter, file_contents)
      print(filtered)

    def first_letter_filter(self, letter, phrase):
      """Returns the words in [phrase] with starting letter after [letter]"""
      result, word = "", ""
      for letter in phrase:     
        if letter.isalpha():         
          word += letter     
        elif word.lower() > "h":         
          result += word.upper() + " "
          word = ""     
        else:         
          word = ""
      if word.lower() > "h":     
        result += word.upper()
      return result


if __name__ == '__main__':
  current_location = os.getcwd()
  print ("Current working dir : %s" % current_location)
  filelocation = current_location+'/phrases.txt'
  filter_letter = 'G'
  FilterSequence(filelocation, filter_letter)
