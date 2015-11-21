#!/usr/bin/python

#Install the modules we need
#from pyfirmata import Arduino, util, INPUT
from mcpi import minecraft
from mcpi import minecraftstuff
from time import sleep
import server
import serial

# Set up a connection to the Arduino/Shrimp if we need it
#PORT = "/dev/tty.SLAB_USBtoUART"
#ser = serial.Serial(PORT, 9600)

# Connect to the server: we use the imported server.py to make it work with CloudMaker
mc = minecraft.Minecraft.create(server.address)
#Post a message to the minecraft chat window 
mc.postToChat("Ready to read Memory!")

# Use the command /getpos or F3 in Minecraft client to find out where you are then use those
# x, y, z coordinates to build things
# translate CloudMaker coords for mcpi ones
# add this to x
mcx = 177
# - this from y
mcy = 64
# - this from z
mcz = 135

# Text Bubble 1
def MemoryCloud1(startx,starty,startz, chartwidth, chartheight, chartdepth, blocktype, blockid):
	# Main Bubble
	mc.setBlocks((startx + mcx), (starty-mcy), (startz-mcz), (startx + mcx) + chartwidth, (starty-mcy) + chartheight, (startz - mcz) + chartdepth, blocktype, blockid)
	# inset bottom
	mc.setBlocks((startx + mcx) + 1, (starty-mcy) - 1, (startz-mcz), (startx + mcx) + (chartwidth-1), (starty-mcy) -1, (startz - mcz) + chartdepth, blocktype, blockid)
	#inset top
	mc.setBlocks((startx + mcx) + 1, (starty-mcy) + (chartheight + 1), (startz-mcz), (startx + mcx) + (chartwidth-1), (starty-mcy) + (chartheight + 1), (startz - mcz) + chartdepth, blocktype, blockid)


# If you want to add a bubble diagram, insert your coordinates
# Then use /js blocktype("My Message", blockid) while facing the block where you want to write

#MemoryCloud1(-343, 75, -15, 44, 14, 2, 35, 0)
#MemoryCloud1(-343, 110, -15, 44, 14, 2, 35, 0)
#MemoryCloud1(-343, 75, -15, 44, 14, 2, 0)
#MemoryCloud1(-343, 100, -15, 44, 14, 2, 0)

# the memory cloud funtction is (myposx, myposy, myposz, width, thickness,
# blocktype, blockidoption)

MemoryCloud1(154, 120, -287, 44, 14, 2, 35, 0)


#
