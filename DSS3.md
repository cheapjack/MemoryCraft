# Do Something Saturdays

## Workshop 4 The Minecraft Of Things Part 2

![Things](http://36.media.tumblr.com/ab3d03e2a3ee6432030c4bbe6e943658/tumblr_n3vrhu2RYX1tytl75o1_500.jpg)

Today we are going to learn about the [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_Things).

Soon almost everything will be connected to the internet, you can turn your heating off as soon as your phone leaves your street or alert people that you need help or make sure your gran can keep in touch with her family and friends.

The basic principles of the internet of things can be learned in Minecraft: you as a player are a `client` on a minecraft `server` that sends you information; where are you, what you are looking at, and then your client (the game on your computer) interprets that data to let you play the game.

Today we are going to play with some physical switches that trigger building events in the game

Then we are going to make our own thing on the internet: an accurate map of St Kilda based on Google Map data and a map made by fellow Minecrafter [GemmaMayLatham](https://twitter.com/gemmamaylatham) using [WorldPaint](http://worldpainter.net/)

## Using the mcpi API with CloudSwitch.py

We can make things happen in minecraft with the `mcpi` **API**
 
 * Open a terminal window
 * Type `cd ~/MoTDSS2/mcpi/`  
 * Type `vim CloudSwitch.py` and use the cursor keys to move around; see the vim instructions below but if you look through the code you can change the `beacon()` function to build beacons in the game based on minecraft coordinates.
 * When you've hacked the `beacon` function you can make your switch build or unbuild beacons in the game. You save any changes by typing `:wq` and press return
 * You run your python programme by typing in the terminal `python CloudSwitch.py` and press return


####Vim

[Vim](http://vim.rtorr.com/) (a version of Vi) is a text editor that lives pretty much on every server on the internet 

 * First make a new window in terminal and type `cd MoT-master`
 * type `ls` to see all the files

 * type `vim CloudSwitch.py` to edit that file


Basically you move with the cursor keys and if you want to type something press `i` and you can type and delete as normal. When you're finished hit escape `esc` and if you want to `write` your changes type `:wq`  

 * `i` - insert text
 * `cursor keys` - move in the text
 * `esc` - stop inserting text
 * `:w` - write your changes
 * `:wq` - write your changes and quit vim

When you are happy with your changes typ `:wq` to save them then try running the CloudSwitch Programme
 
 * Make another window and type `cd MoT-master`
 * Type `python CloudSwitch.py` as you type you can press `Tab` the arrow pointin right next to the `q` key and this will **auto-complete** the file name

**Then see if it works!**

## Mapping in Minecraft

Our main task today is to complete a model of St Kilda 

