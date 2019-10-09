# Battleship Field Validator


## Instructions

Write a method that takes a field for well-known board game "Battleship" as an 
argument and returns true if it has a valid disposition of ships, false 
otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in 
the array are numbers, 0 if the cell is free and 1 if occupied by ship.


### Background

Battleship (also Battleships or Sea Battle) is a guessing game for two players. 
Each player has a 10x10 grid containing several "ships" and objective is to 
destroy enemy's forces by targetting individual cells on his field. The ship 
occupies one or more cells in the grid. Size and number of ships may differ 
from version to version. In this kata we will use Soviet/Russian version of the 
game.

![](http://i.imgur.com/IWxeRBV.png)


### Rules

Before the game begins, players set up the board and place the ships 
accordingly to the following rules:
- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 
destroyers (size 2) and 4 submarines (size 1). Any additional ships are not 
allowed, as well as missing ships.
- Each ship must be a straight line, except for submarines, which are just 
single cell.

    ![](http://i.imgur.com/FleBpT9.png)
- The ship cannot overlap or be in contact with any other ship, neither by edge 
nor by corner.

    ![](http://i.imgur.com/MuLvnug.png)