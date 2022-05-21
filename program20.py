string_text = '''Write a Python program to print a long text, convert the string to 
a list and print all the words and their frequencies.'''
word_list = string_text.split()

word_freq = [word_list.count(n) for n in word_list]

print("String:\n {} \n".format(string_text))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))