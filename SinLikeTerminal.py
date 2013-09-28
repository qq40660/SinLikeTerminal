# -*- coding: UTF-8 -*
'''
Created on 2013-9-28

@author: RobinTang
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

if __name__ == '__main__':
    rawdict = {}
    user1 = PrefixDict(rawdict=rawdict, prefix='u1')
    user2 = PrefixDict(rawdict=rawdict, prefix='u2')
    user3 = PrefixDict(rawdict=rawdict, prefix='u3')
    user1['name'] = 'User1'
    user2['name'] = 'User2'
    user3['name'] = 'User3'
    print user1['name']
    print user2['name']
    print user3['name']
    
    
    
    
    
    
    
    
    