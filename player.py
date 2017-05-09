"""
This module handles every vars and behaviour related to player

TODO : Stock players into DB/file
Serialize players infos
static value for list of stats
"""

import stats
import job
import conf

class player():	 
	#Create player
	def __init__(self, name, job):
		self.name = name;
		self.status = 1; #1 if alive, 0 if dead
		self.stats = {};
		self.initalize(job);
		
	#Initalize stats for player
	def initalize(self, job) :
		print '===Creating stats for new player ' #print name
		#Go through stats dicctionarry
		self.stats['life'] = stats.stat('life', 10, 10); #find how to give optional value
		self.stats['life'].showStat();
		
	#Check current stats of player
	def checkStats(self):
		print 'checkStats';
		
	#Save player infos and xp to DB/file
	def savePLayer(self):
		print 'savePlayer';
		
	#List combat actions availables 
	#And allow player to make a choice
	def makeCombatActions(self):
		#combat actions
		print 'makeActions';
		
	#Activate actions choiced by player	
	def dispatchActions(self, actionNumber):
		print 'dispatchActions';
	#How to store all actions ? Tab in conf.py ? 
	#Associative array ?
	
	#Allow player to strike an opponent
	def attack(self):
		print 'attack';
		#Target opponent
		#Choose weapon
		#Strike
		
	#Observe an ennemy to get infos on him	
	def observe(self):
		print 'observe';
		#Target opponent
		#Gain infos from him
		
