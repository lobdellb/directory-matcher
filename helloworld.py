#!/usr/bin/python

import hashlib
import os
import sys

print "Bryce is a pimp daddy.\n"


class File:
    # name
    # parent 
    # hash 
    
    def __init__(self,filename):
        self.name = filename

        fp = open( filename, 'r' )
        m = hashlib.new('md5')
        bs = m.block_size
        d = fp.read( bs );
        while len( d ) > 0:
            m.update( d )
            d = fp.read( bs )

        fp.close()
        self.hash = m.digest()


class Dir:
    # _name
    # _childrenFiles
    # _childrenDirs
    # _parent

    def __init__(self,dirname):
        self._name = dirname
        self._childrenFiles = []
        self._childrenDirs = []

        for childname in os.listdir(dirname):
            if os.path.isfile( dirname + childname ):
                self._childrenFiles.append( File( dirname + childname) )
            if os.path.isdir( dirname + childname ):
                self._childrenDirs.append( Dir( dirname + childname ) )



    def scoreFile(file):
        pass


    def scoreDir(dir):
        pass



#F = File('test')

#print F.name 
#print F.hash

if len( sys.argv ) != 2:
    print "wrong number of arguments"
else:
    D = Dir(sys.argv[1])

    print D._childrenDirs
    print D._childrenFiles

