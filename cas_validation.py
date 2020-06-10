#!/usr/bin/python

import sys
def cas_validation(cas):
	"""Validates if a provided CAS number could exist"""

	try:
		cas_match = cas.split('-') # Takes into account the standard CAS formatting e.g. 7732-18-5
		if len(cas_match[2]) != 1:
			return False
		cas_string = cas_match[0] + cas_match[1] + cas_match[2]

		increment = 0
		sum_cas = 0

		# Slices the reversed number string
		for number in reversed(cas_string):
			if increment == 0:
				validate = int(number)
				increment = increment + 1
			else:
				sum_cas = sum_cas + (int(number) * increment)
				increment = increment + 1

		# Does the math
		if validate == sum_cas % 10:
			print('True') # Can be removed if not used on Terminal
			return True
		else: 
			print('False') # Can be removed if not used on Terminal
			return False
	except:
		print('Something went wrong') # Choose the action for errors you like

def main():
  if len(sys.argv) != 2:
    print('usage: python cas_validation.py CAS')
    sys.exit(1)
  cas = sys.argv[1]
  cas_validation(cas)
  
if __name__ == "__main__":
  main()
