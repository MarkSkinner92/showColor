#!/usr/bin/python

import Tkinter as tk

root=tk.Tk()
root.attributes('-zoomed',True)
root.configure(bg='black')

LOOP = True
print("enter a color (eg. red green blue etc.)")
print("enter nothing to quit")
print("")
while LOOP:
	usrinput = raw_input("enter a color: ")
	if len(usrinput) > 0:
		try:
			root.configure(bg=usrinput)
		except tk.TclError as e:
			print("'{}' is not a supported color".format(usrinput))
	else:
		root.quit()
		exit()
		LOOP = False