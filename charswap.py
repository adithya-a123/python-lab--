def swap_characters(string):
 	first=string[0]
 	last=string[-1]
 	mod_string=last+string[1:-1]+first
 	print(mod_string)
string=input("Enter a string:")
swap_characters(string)
