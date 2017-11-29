#!python

import sys

class pending:
	dbase = {}

	def __init__ (self, opts):
		self.lifer = opts.get ('lifer')
		self.area  = opts.get ('area')

	def _load (self, opts):
		score = 1
		fname = self.area

		if opts:
			score = 0
			fname = self.lifer

		with open (fname, 'r') as f:
			for line in f:
				line = line.strip()
				species = (line.split (','))[1]
				self.dbase.update ( {species : score} )

	def write (self):
		self._load (False)
		self._load (True)

		for key in self.dbase.keys():
			if self.dbase.get (key):
				if "sp." in key:
					continue
				if "/" in key:
					continue
				print key

if __name__ == '__main__':
	lifer = 'data/ebird_world_life_list.csv'
	area  = 'L1933806-mysore-indraprastha.csv'

	if len (sys.argv) > 1:
		lifer = sys.argv[2] 
		area  = sys.argv[1]
		try:
			p = pending ({'lifer': lifer, 'area': area})
			p.write()
		except:
			print "Error: cannot handle " + lifer + " or " + area

	else:
		print "Usage: " + sys.argv[0] + " <lifer_csv> <area_csv>"
		print "       lifer_csv: " + lifer
		print "       area_csv:  " + area
