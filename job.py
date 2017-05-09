"""
This module handles players jobs

Each job got infos from file/database (still has to determine it)

"""

class job():
	def __init__(self, name, level):
		self.setStatsForJob(self, name)
	
	def setStatsForJob(self, name):
		print 'setStatsForJob' 
