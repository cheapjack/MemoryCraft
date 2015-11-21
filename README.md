# Do Something Saturdays

## Workshop 5 The Minecraft Of Things Part 3

![datacraftsmall](https://cloud.githubusercontent.com/assets/128456/11318314/69cdaf12-9044-11e5-8ff5-a6b169b36fcc.png)


Today we are going to play with some prototype [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things) products made by CloudMaker, **RF-Craft** and some [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft) Kits

###Background

**Lesions in the Landscape** by *Shona Illingworth* refers to the islands of **St Kilda** as a a landscape haunted by traces of cultural memory; the community of people who lived there altho
ugh small inhabited the islands for over 2000 years. She also hints at its more contemporary id
entity as a strategic point in the infrastructure of mapping and tracking technology often for semi-military applications. In her video installation she seems to link this to the forcible relocation of inhabitants in the 1930s; hinting at contemporary technology's control and tracking of cultural *externalised* memory. 

Soon almost everything will be connected to the internet, you can turn your heating off as soon as your phone leaves your street or alert people that you need help or make sure your gran can keep in touch with her family and friends.

The basic principles of the internet of things can be learned in Minecraft: you as a player are a `client` on a minecraft `server` that sends you information; where are you, what you are looking at, and then your client (the game on your computer) interprets that data to let you play the game.

###Workshop

 * Explore exhibition again
 * Explore the server again
 * Look at the St Kilda Map
 * Look at some Internet Of Things Examples
 * Do an Internet of Things `HelloWorld.py` example
 * Make some sensors
 * Send live data to Minecraft with [ShrimpCraft](https://github.com/cheapjack/ShrimpCraft)
 * Draw graphs by the **RF-Craft** castle
 * Make a secret door game to transport us to **memory islands**
 * Use `MemoryCloud.py` to make clouds
 * Use `/js back(1).blocktype("My Memory\nMy Name", "35:2")` to write memory clouds

###Activity

First off we are going to open the `MemoryCraft-Master` folder on your computer desktop and open some `Python` files. Python files are opened with IDLE an IDE (Integrated Development Environment) for Python

Try opening `HelloWorld.py` in the MemoryCraft Folder 

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

Anything beginning with a hash `#` is a 'comment'; ie its our notes to remind us what each bit of code does... Happy Coding!

### More soon...  

