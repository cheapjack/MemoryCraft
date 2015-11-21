#!/usr/bin/python

# import what we need to send messages to minecraft
from mcpi import minecraft
import server

mc = minecraft.Minecraft.create(server.address)

#####################################
#                                   #
#                                   #
#     Hack the message code!        #
#                                   #
#                                   #
#####################################

# This is our message to the Minecraft server
mc.postToChat("Hello world! Connecting to CloudMaker!")

#We are each playing on a minecraft cloudmaker account try hacking the code above to say your nname and the name of your player name!

# Just change the text within the quotes
