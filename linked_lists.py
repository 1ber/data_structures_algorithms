#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
# https://www.youtube.com/watch?v=XDO6I8jxHtA
import sys

class Node( ):
    def __init__( self, value=None ):
        self.value=value
        self.next=None
        
    def __str__( self ):
        return( str( self.value ) )
        
class LinkedList( ):
    def __init__( self ):
        self.root=None
        
    def add( self, value=None ):

        if self.root is None:
            self.root=Node( value=value )
        else:
            n=self.root
            while n.next is not None:
                n=n.next
            n.next=Node( value=value )

    def reverse( self ):
        

        prev=None
        head=self.root
        
        while( head ):
            
            temp = head
            # ~ print( '---' )
            # ~ print( '>prev:%s,head:%s,temp:%s,temp.next:%s' % (prev, head, temp, temp.next ) )
            head=head.next
            # ~ print( '>prev:%s,head:%s,temp:%s,temp.next:%s' % (prev, head, temp, temp.next ) )
            temp.next=prev
            # ~ print( '>prev:%s,head:%s,temp:%s,temp.next:%s' % (prev, head, temp, temp.next ) )
            prev=temp
            # ~ print( '>prev:%s,head:%s,temp:%s,temp.next:%s' % (prev, head, temp, temp.next ) )
            
        self.root=prev
        
            
            
            

    def get( self, position=0 ):
        p=0
        n=self.root
        # ~ print( '>>', n )
        while p<position:
            
            n=n.next
            
            p=p+1
        return (n)
        

def main():
    
    ll=LinkedList()
    ll.add( 1 )
    ll.add( 2 )
    ll.add( 3 )
    
    print( ll.get( 0 ) )
    print( ll.get( 1 ) )
    print( ll.get( 2 ) )
    
    ll.reverse()
    print( ll.get( 0 ) )
    print( ll.get( 1 ) )
    print( ll.get( 2 ) )

    
    sys.exit( 0 )


if __name__ == "__main__":
    

    main()

