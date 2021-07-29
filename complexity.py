#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ~ Copyright (c) 2021 Humberto Ramos Costa
import sys
from math import inf

def max( iterable ):
    
    m=-inf
    for n in iterable:
        if n>m:
            m=n
    return( m )

def main():
    print( max( [5, 7, 13, 8 , 3, 7, 1] ) )

    
    sys.exit( 0 )


if __name__ == "__main__":
    

    main()

