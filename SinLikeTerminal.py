# -*- coding: UTF-8 -*
'''
Created on 2013-9-28

@author: RobinTang
@see: https://github.com/sintrb/SinLikeTerminal



Design doc.

message
?	# current function help
>?	# current function help
>a	# set current function with a

xx	# process message with current function
#?	# global help
#a.b.c	# process message with global function


'''




class PrefixDict(object):
	'''
	A Dictionary Adapter.
	It can be use as a Dictionary.
	It's implemented by a normal Dictionary witch can be share for many PrefixDict.
	Such as:
	-   rawdict = {}
	-   user1 = PrefixDict(rawdict=rawdict, prefix='u1')
	-   user2 = PrefixDict(rawdict=rawdict, prefix='u2')
	-   user3 = PrefixDict(rawdict=rawdict, prefix='u3')
	-   user1['name'] = 'User1'
	-   user2['name'] = 'User2'
	-   user3['name'] = 'User3'
	-   print user1['name']
	-   print user2['name']
	-   print user3['name']
	'''
	def __init__(self, rawdict={}, prefix=''):
		self.rawdict = rawdict
		self.prex = prefix
	def __trankey__(self, key):
		return '%s_%s'%(self.prex, key)
	
	# Implement Dictionary function
	def __getitem__(self, key):
		return self.rawdict.__getitem__(self.__trankey__(key))
	def __setitem__(self, key, value):
		return self.rawdict.__setitem__(self.__trankey__(key), value)
	def __delitem__(self, key):
		return self.rawdict.__delitem__(self.__trankey__(key))
	def __contains__(self, key):
		return self.rawdict.__contains__(self.__trankey__(key))
	def __str__(self):
		return self.rawdict.__str__()




def func1(uid, msg, sesn):
	return 'func1 %s'%msg

def func2(uid, msg, sesn):
	return 'func2 %s'%msg

def func3(uid, msg, sesn):
	return 'func3 %s'%msg

def func4(uid, msg, sesn):
	return 'func4 %s'%msg

class SinLikeTerminal():
	'''
	A chat robot Terminal
	'''
	__PREFIX_CURRENT__ = '>'
	__PREFIX_GLOBAL__ = '#'
	__PREFIX_HELP__ = '?'
	
	__ROUTE_SPLIT__ = '.'
	__USER_ROUTE__ = 'route'
	
	def __init__(self, sessinstore={}):
		self.session = sessinstore
		self.route = {
			'name':'R',
			'func':func1,
			'help':'help for R',
			'subfunc':{
					'r1':{
						'id':'r1',
						'name':'R1',
						'help':'help for R1',
						'func':func2,
						'subfunc':{
							'r2':{
								'id':'r4',
								'name':'R4',
								'help':'help for R4',
								'func':func4
							},
						}
					},
					'r2':{
						'id':'r2',
						'name':'R2',
						'help':'help for R2',
						'func':func3
					},
				}
		}
	
	def __get_current_routes__(self, usersession):
		return None if not SinLikeTerminal.__USER_ROUTE__ in usersession else usersession[SinLikeTerminal.__USER_ROUTE__]
	
	def __set_current_routes__(self, usersession, routes):
		usersession[SinLikeTerminal.__USER_ROUTE__] = routes
		
	def __get_route__(self, usersession, routes):
		if routes:
			rt = self.route
			for k in routes.split(SinLikeTerminal.__USER_ROUTE__):
				if 'subfunc' in rt and k in rt['subfunc']:
					rt = rt['k']
				else:
					break
			return rt
		else:
			return self.route
	
	def __get_current_route__(self, usersession):
		return self.__get_route__(usersession, self.__get_current_routes__(usersession))
		
	
	def __process_message_with_route(self, route, message, uid, usersession):
		return route(uid, message, usersession)
	
	def process_message(self, uid, message):
		usersession = {}
		if message[0] == SinLikeTerminal.__PREFIX_CURRENT__:
			# current message process
			route = self.__get_current_route__(usersession)
			if message[1]==SinLikeTerminal.__PREFIX_HELP__:
				return route['help']
			else:
				return self.__process_message_with_route(route['func'], message[1:], uid, usersession)
		elif message[0] == SinLikeTerminal.__PREFIX_GLOBAL__:
			if message[1]==SinLikeTerminal.__PREFIX_HELP__:
				# global help
				return self.route['help']
			
#		usersession = PrefixDict(rawdict=self.session, sessionid)
		


if __name__ == '__main__':
# 	rawdict = {}
# 	user1 = PrefixDict(rawdict=rawdict, prefix='u1')
# 	user2 = PrefixDict(rawdict=rawdict, prefix='u2')
# 	user3 = PrefixDict(rawdict=rawdict, prefix='u3')
# 	user1['name'] = 'User1'
# 	user2['name'] = 'User2'
# 	user3['name'] = 'User3'
# 	print user1['name']
# 	print user2['name']
# 	print user3['name']
	
	slt = SinLikeTerminal()
	sessionid = 'trb'
	print slt.process_message(sessionid, '>1')
	print slt.process_message(sessionid, '>?')
	
	
	
	
	
	
	
	
	