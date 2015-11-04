#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Author: Albin Hübsch - albin.hubsch@gmail.com
# 

# Import
import os

res = []

# Fetch files in test resultat folder
for file in os.listdir("./Testresultat"):
	if file.endswith(".txt"):
		fileA = file.split('-')
		# print fileA
		name = fileA[0]
		dtype = fileA[1]

		# print dtype

		with open("./Testresultat/"+file) as f:
			content = f.readlines()

		cc = content[0].split(',')
		cc.pop()


		# shitstorm
		if dtype == 'hc' or dtype == 'lc':
			# pass
			print dtype
			# Parse data
			for l in cc:
				if '\n' in l:
					print 'blöööö'
				else:
					shape = l.split(':')[0]
					time = l.split(':')[1]

					print name+','+shape+','+time
					
		elif dtype == 'instructions':
			pass
			# print dtype
			# # Parse data
			# for l in cc:
			# 	if '\n' in l:
			# 		print 'blöööö'
			# 	else:
			# 		shape = l.split(':')[0]
			# 		time = l.split(':')[1]

			# 		print name+','+shape+','+time