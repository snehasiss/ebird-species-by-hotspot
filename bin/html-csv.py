#!python

import sys
import re

class convert:
	def __init__ (self, html):
		self.html = html
		self.text = "<div class='subitem'>"

	def extract (self):
		with open (self.html, 'r') as f:
			count=1
			for line in f:
				if self.text in line:
					line = line.strip()
					trim = re.compile ('<.*?>')
					line = re.sub (trim, '', line)
					print str(count) + "," + line + ","
					count = count + 1

if __name__ == '__main__':

	if len (sys.argv) > 1:
		html = sys.argv[1]
		try:
			c = convert (html)
			c.extract ()
		except:
			print 'Cannot handle: ' + html
