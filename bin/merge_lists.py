#!/usr/bin/python

import sys

class unique:
	db = {}

	def read (self, csv):
		with open (csv, 'r') as f:
			for line in f:
				line = line.strip()
				species = (line.split(','))[1]
				self.db.update ( {species : 1} )

	def write (self):
		i=1
		for key in sorted (self.db.keys()):
			if 'sp.' not in key:
				print str(i) + "," + key + ","
				i=i+1

if __name__ == '__main__':
	u = unique()
	for arg in sys.argv[1:]:
		print '  adding ' + arg
		u.read ( arg )

	print 'writing output:'
	u.write ()
