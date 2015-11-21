# Do Something Saturdays

## Workshop 5 The Minecraft Of Things Part 3

![Things](http://36.media.tumblr.com/ab3d03e2a3ee6432030c4bbe6e943658/tumblr_n3vrhu2RYX1tytl75o1_500.jpg)

Today we are going to play with some prototype [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things) products made by CloudMaker, **RF-Craft** and some [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft) Kits

###Background

**Lesions in the Landscape** by *Shona Illingworth* refers to the islands of **St Kilda** as a a landscape haunted by traces of cultural memory; the community of people who lived there altho
ugh small inhabited the islands for over 2000 years. She also hints at its more contemporary id
entity as a strategic point in the infrastructure of mapping and tracking technology often for semi-military applications. In her video installation she seems to link this to the forcible relocation of inhabitants in the 1930s; hinting at contemporary technology's control and tracking of cultural *externalised* memory. 

Soon almost everything will be connected to the internet, you can turn your heating off as soon as your phone leaves your street or alert people that you need help or make sure your gran can keep in touch with her family and friends.

The basic principles of the internet of things can be learned in Minecraft: you as a player are a `client` on a minecraft `server` that sends you information; where are you, what you are looking at, and then your client (the game on your computer) interprets that data to let you play the game.

###Workshop

First off we are going to open the `DSSFinal` folder on your computer and open some `Python` files. Python files are opened with IDLE an IDE (Integrated Development Environment) for Python

Try opening `HelloWorld.py` 

You will see this text
```
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
```

Anything beginning with a hash `#` is a 'comment'; ie its our notes to remind us what each bit of code does  

