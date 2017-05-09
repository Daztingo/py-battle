"""
This module handles players stats
Minus hp and mp, stats are based from 1 to 20.
The more you get, the more you're good
"""

class stat():
	#Define stat : Name as to be normed. Maxstat is equal to current stat by default
	def __init__(self, name, currentStat, maxStat):
		self.name = name
		self.currentStat = currentStat
		self.maxStat = maxStat
		
	def showStat(self):
		#print self.name + ' : ' + self.currentStat + '/' + self.maxStat
		print 'showStat';
		
	def challengeStat(self, modificator, critical):
		#Generate random number
		
		#Add modificator to tested stat
		
		#Compare if number <= Stat
		
		#Critical proc if number >= Stat - critical
		print 'challengeStat'
