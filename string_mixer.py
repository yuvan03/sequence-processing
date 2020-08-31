

class StringMixer():
    """ Takes string input and then prints out a mixed order version of the string"""
    
    def __init__(self, word_list):
        self.word_list = word_list
        self.mix_sentence()

    def mix_word(self, word_list):
        word_list.sort()
        new_words = []
        while len(word_list) > 5:
            new_words.append(word_list[-5])
            word_list.pop(-5)
            new_words.append(word_list[0])
            word_list.pop(0)
            new_words.append(word_list[-1])
            word_list.pop(-1)
        return new_words

    def mix_sentence(self):
        word_list = self.word_list
        word_length = len(word_list)
        for index in range(word_length):
            if len(word_list[index]) <= 3:
                word_list[index] = word_list[index].lower()
            elif len(word_list[index]) >=7:
                word_list[index] = word_list[index].upper()
                
        mixed = self.mix_word(word_list)

        for each_word in mixed:
            print(each_word, end=" ")
        print()

if __name__ == '__main__':
    word = input ("Please enter poem/saying: ")
    word_list = word.split()    
    StringMixer(word_list)