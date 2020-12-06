# Is the Word Singular or Plural?
def is_plural(word):
	return word.endswith('s')

s = input("Enter the world:")
if is_plural(s):
    print("This word is Plural.")
else:
    print("This world is Singular.")    
