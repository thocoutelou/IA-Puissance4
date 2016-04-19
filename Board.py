#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import IAPuissance4

class Board():
	
	def __init__(n,p):
		self.gmap = []
		for i in range(p):
			self.gmap.append([0] * n)
