#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import IAPuissance4

# Game implements the rules of the game.

class Game():
	
	def __init__(player1, player2, board):
		self.player1 = player1
		self.player2 = player2
		self.board = board
