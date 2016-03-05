# 이 클래스는 Table의 처리 공간을 2D 직사각형으로 정의합니다.

from tkinter import *

class Table:
	###생성자
	def __init__(self, window, colour = "black", net_colour = "green", 
				width = 600, height = 400, vertical_net = False, horizontal_net = False):
	    self.width = width
	    self.height = height
	    self.colour = colour


	    # tkinter 공장으로부터 캔버스 주문
	    self.canvas = Canvas(window, bg = self.colour, height = self.height, width = self.width)
	    self.canvas.pack()


	    #tkinter 공장의 메서드를 사용하여 캔버스에 네트 추가
	    if(vertical_net):
	    	self.canvas.create_line(self.width/2, 0, self.width/2, self.height, width=2, fill=net_colour, dash=(15, 23))
	    if(horizontal_net):
        	self.canvas.create_line(0, self.height/2, self.width, self.height/2, width=2, fill=net_colour, dash=(15, 23))
	    