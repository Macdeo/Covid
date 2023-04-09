#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 14:16:57 2022

@author: macdeo
"""

grid = []
# ash = '#'
# frontGrid = grid.insert(0,ash)
# backGrid = grid.append(ash)
# def first(playerNum):
#     playerNum = int(input("Please enter a number from 1 to 9:"))
#     return playerNum

def sudoku(playerNum):
    count = 0
    while count < 9:

        if (playerNum > 0)  and (playerNum < 10):
            playerNum = int(input("Please enter another number from 1 to 9:"))
            grid.insert(count,playerNum)
            print(grid)
        count = count + 1
    return playerNum

sudoku(4)

#playerNum = int(input("Please enter a number from 1 to 9:"))



    
    
# while (playerNum > 0)  and (playerNum < 10):
#     grid.insert(count,playerNum)
# count = count + 1
#print(grid)
