#Kevin Shi
#Kevin's Maplestory Paint.py

#This is a paint program with a Maplestory theme. This paint program has many of the basic functions of paint program (such as pencil, brush, eraser,
#shapes, stamps, spray can, eyedropper, and a colour palette). There is nice background music that loops. The program can also save and load images in the
#'save files' folder. Unofrtunately, it can only save and load pngs. If you want to load an image, you have to drag the image into the 'save files' folder
# before you can load it. The icons will have a blue outline when they are hovered over and a red one if they are selected. The stamps have a description of
#the characters that they are based off of. The code is pretty long, but most of it is loading images, icons, and text.

from random import *
from pygame import *
from math import *
from glob import *
from getname import *

screen = display.set_mode((1100,700))
#-------------SONGS-------------------------------------
init()
song1 = mixer.music.load("songs/maplestory theme 1.mp3")
mixer.music.play(-1)
#------------Font-----------------------------------
font.init()
font = font.SysFont("Comic Sans MS",13)
#------------Background and Titles-------------------
background = image.load("background/background.jpg")
paint = image.load("background/paint.jpg")
screen.blit(background,(0,0))
screen.blit(paint,(0,75))
#----------------------------------------------------------------------
canvas = Rect(230,50,720,500)#drawing surface
draw.rect(screen,(255,255,255),canvas)
draw.rect(screen,(0,0,0),(229,49,722,502),1)#line outlining the canvas, which is outside of the actual so that it can't be erased
#--------------Music Pause/Play------------------------------------
playRect = Rect(125,500,75,75)                                                      #For the next hundred lines or so, its just drawing and
pauseRect = Rect(125,600,75,75)                                                     #bliting the boxes for the icons.
play = image.load("icons/play.png")
pause = image.load("icons/pause.png")
screen.blit(play,(125,500))
screen.blit(pause,(125,600))
#--------------Drawing Buttons-------------------------------------------------
colourRect = Rect(1000,50,50,500)           #colour palette (primary and secondary colours)
colours = image.load("icons/colours.jpg")
screen.blit(colours,(1000,50))
draw.rect(screen,(0,0,0),colourRect,2)

colour2Rect = Rect(1000,575,50,100)         #Second colour (black, grey, and white)
colours2 = image.load("icons/colours2.jpg")
screen.blit(colours2,(1000,575))
draw.rect(screen,(0,0,0),colour2Rect,2)
#-----First Extra Column (Clear and Bucket)-----
clearRect = Rect(30,180,50,50)
clear = image.load("icons/clear.jpg")
screen.blit(clear,(30,180))

bucketRect = Rect(30,240,50,50)
bucket = image.load("icons/bucket.jpg")
screen.blit(bucket,(30,240))
#-----Second Extra Column (Undo and Redo)------
undoRect = Rect(90,180,50,50)
undo = image.load("icons/undo.png")
screen.blit(undo,(90,180))

redoRect = Rect(90,240,50,50)
redo = image.load("icons/redo.png")
screen.blit(redo,(90,240))
#------Third Extra Column (Save and Load)------
saveRect = Rect(150,180,50,50)
save = image.load("icons/save.png")
screen.blit(save,(150,180))

loadRect = Rect(150,240,50,50)
load = image.load("icons/load.png")
screen.blit(load,(150,240))
#-------First Row of Tools (Stamps)---------
luminousRect = Rect(230,630,50,50)
luminous = image.load("icons/luminous.png")
screen.blit(luminous,(230,630))

aranRect = Rect(290,630,50,50)
aran = image.load("icons/aran.png")
screen.blit(aran,(290,630))

evanRect = Rect(350,630,50,50)
evan = image.load("icons/evan.png")
screen.blit(evan,(350,630))

mercedesRect = Rect(410,630,50,50)
mercedes = image.load("icons/mercedes.png")
screen.blit(mercedes,(410,630))

phantomRect = Rect(470,630,50,50)
phantom = image.load("icons/phantom.png")
screen.blit(phantom,(470,630))

demonslayerRect = Rect(530,630,50,50)
demonslayer = image.load("icons/demonslayer.png")
screen.blit(demonslayer,(530,630))

mageRect = Rect(590,630,50,50)
mage = image.load("icons/mage.png")
screen.blit(mage,(590,630))

pirateRect = Rect(650,630,50,50)
pirate = image.load("icons/pirate.png")
screen.blit(pirate,(650,630))

thiefRect = Rect(710,630,50,50)
thief = image.load("icons/thief.png")
screen.blit(thief,(710,630))

warriorRect = Rect(770,630,50,50)
warrior = image.load("icons/warrior.png")
screen.blit(warrior,(770,630))

bowmanRect = Rect(830,630,50,50)
bowman = image.load("icons/bowman.png")
screen.blit(bowman,(830,630))

blackmageRect = Rect(890,630,50,50)
blackmage = image.load("icons/blackmage.jpg")
screen.blit(blackmage,(890,630))
#--Second Row of Tools (Shapes and Drawing Tools)----
pencilRect = Rect(230,570,50,50)
pencil = image.load("icons/pencil.jpg")
screen.blit(pencil,(230,570))

brushRect = Rect(290,570,50,50)
brush = image.load("icons/brush.jpg")
screen.blit(brush,(290,570))

eraserRect = Rect(350,570,50,50)
eraser = image.load("icons/eraser.jpg")
screen.blit(eraser,(350,570))

sprayRect = Rect(410,570,50,50)
spray = image.load("icons/spray.jpg")
screen.blit(spray,(410,570))

eyedropperRect = Rect(470,570,50,50)
eyedropper = image.load("icons/eyedropper.jpg")
screen.blit(eyedropper,(470,570))

rectangleRect = Rect(530,570,50,50)
rectangle = image.load("icons/rectangle.jpg")
screen.blit(rectangle,(530,570))

ellipseRect = Rect(590,570,50,50)
ellipse = image.load("icons/ellipse.jpg")
screen.blit(ellipse,(590,570))

polygonRect = Rect(650,570,50,50) 
polygon = image.load("icons/polygon.png")
screen.blit(polygon,(650,570))

fillrectangleRect = Rect(710,570,50,50)
fillrectangle = image.load("icons/fillrectangle.jpg")
screen.blit(fillrectangle,(710,570))

fillellipseRect = Rect(770,570,50,50)
fillellipse = image.load("icons/fillcircle.png")
screen.blit(fillellipse,(770,570))

fillpolygonRect = Rect(830,570,50,50) 
fillpolygon = image.load("icons/fillpolygon.jpg")
screen.blit(fillpolygon,(830,570))

lineRect = Rect(890,570,50,50)
line = image.load("icons/line.png")
screen.blit(line,(890,570))
#--------------STAMPS LOAD-------------------------------
luminousstamp = image.load("stamps/luminousstamp.png")
aranstamp = image.load("stamps/aranstamp.png")
evanstamp = image.load("stamps/evanstamp.png")
mercedesstamp = image.load("stamps/mercedesstamp.png")
phantomstamp = image.load("stamps/phantomstamp.png")
demonslayerstamp = image.load("stamps/demonslayerstamp.png")
magestamp = image.load("stamps/magestamp.png")
piratestamp = image.load("stamps/piratestamp.png")
thiefstamp = image.load("stamps/thiefstamp.png")
warriorstamp = image.load("stamps/warriorstamp.png")
bowmanstamp = image.load("stamps/bowmanstamp.png")
blackmagestamp = image.load("stamps/blackmagestamp.png")

#LISTS OF BOXES, FUNCTIONS, and DESCRIPTIONS
musicboxes = [playRect,pauseRect]                       #boxes and functions have to be properly aligned so that the correct toll will be used when the
musicfunction = ["play","pause"]                        #boxes are clicked on.

toolboxes = [pencilRect,brushRect,eraserRect,sprayRect,eyedropperRect]
toolfunction = ["pencil","brush","eraser","spray","eyedropper"]

tooldescription = ["Tool - Pencil",                                             #The descriptions are put into multiple lists because the small description
                   "Tool - Brush",                                              #box can't fit all of the information that needs to be put into the descrip-
                   "Tool - Eraser",                                             #tions. Each list contains the lines of each description as they go along.
                   "Tool - Spray",                                              #for example, tooldescription contains the first line of text for each tool, 
                   "Tool - Eyedropper"]                                         #and tooldescription2 contains the second line. These lists will then go
                                                                                #through a loop that will cause them to appear on the screen. The descripti-
tooldescription2 = ["Use the left mouse button to",     #pencil blurb           #ons are labelled on the side so that you can read them line by line.
                    "Thicker version of the Pencil",    #brush blurb            ##Needless to say that I couldn't think of a better way to do this...
                    "Use the eraser to erase any",      #eraser blurb
                    "Now you can also be a graffiti",   #spray paint blurb
                    "Use the eyedropper to select"]     #eyedropper blurb

tooldescription3 = ["draw on the canvas. Does not",     #pencil blurb
                    "tool. The thickness of the brush", #brush blurb
                    "mistakes you've made. Comes",      #eraser blurb
                    "artist. Spray areas scale with",   #spray paint blurb
                    "a colour on the canvas. Doesn't"]  #eyedropper blurb

tooldescription4 = ["change size.",                     #pencil blurb
                    "scales with change size.",         #brush blurb
                    "in different sizes.",              #eraser blurb
                    "size.",                            #spray paint blurb
                    "scale with size."]                 #eyedropper blurb

shapeboxes = [rectangleRect,ellipseRect,polygonRect,fillrectangleRect,fillellipseRect,fillpolygonRect,lineRect]
shapefunction = ["rectangle","ellipse","polygon","fillrectangle","fillellipse","fillpolygon","line"]

shapedescription = ["Tool - Rectangle",                 
                    "Tool - Ellipse",                   
                    "Tool - Polygon",                   
                    "Tool - Filled Rectangle",          
                    "Tool - Filled Ellipse",            
                    "Tool - Filled Polygon",            
                    "Tool - Line"]                      

shapedescription2 = ["Use this tool to draw unfilled",  #Rectangle blurb
                     "Use this tool to draw unfilled",  #Ellipse blurb
                     "Use this tool to draw unfilled",  #Polygon blurb
                     "Use this tool to draw filled" ,   #Fill rectangle blurb
                     "Use this tool to draw filled",    #Fill ellipse blurb                     
                     "Use this tool to draw filled",    #Fill polygon blurb
                     "Use this tool to draw straigt"]   #Line blurb

shapedescription3 = ["rectangles. Thickness scales",    #Rectangle blurb
                     "ellipses. Thickness scales with", #Ellipse blurb
                     "polygons. Set points on the",     #Polygon blurb
                     "rectangles. Doesn't scale with",  #Fill rectangle blurb
                     "ellipses. Doesn't scale with",    #Fill ellipse blurb               
                     "polygons. Set points with right", #Fill polygon blurb
                     "lines. Thickness scales with"]    #Line blurb
                     
shapedescription4 = ["with size.",                      #Rectangle blurb
                     "size.",                           #Ellipse blurb
                    "canvas with right click and",      #Polygon blurb
                     "size.",                           #Fill rectangle blurb
                     "size.",                           #Fill ellipse blurb
                     "click and draw the with left.",   #Fill polygon blurb
                     "size."]                           #Line blurb

shapedescription5 = ["",                                #Rectangle blurb
                     "",                                #Ellipse blurb
                     "draw with left click. Thickness", #Polygon blurb
                     "",                                #Fill rectangle blurb
                     "",                                #Fill ellipse blurb                     
                     "Doesn't scale with size",         #Fill polygon blurb
                     ""]                                #Line blurb

shapedescription6 = ["",                                #Rectangle blurb
                     "",                                #Ellipse blurb
                     "scales with size.",               #Polygon blurb
                     "",                                #Fill rectangle blurb
                     "",                                #Fill ellipse blurb
                     "",                                #Fill polygon blurb
                     ""]                                #Line blurb
    
sclickboxes = [clearRect,bucketRect,undoRect,redoRect,saveRect,loadRect]
sclickfunction = ["clear","bucket","undo","redo","save","load"]

sclickdescription = ["Tool - Clear",
                     "Tool - Bucket",
                     "Tool - Undo",
                     "Tool - Redo",
                     "Tool - Save",
                     "Tool - Load"]
sclickdescription2 = ["Upset at everything you've",             #Clear blurb
                      "Is a white background too",              #Bucket blurb
                      "Go back into the past and undo",         #Undo blurb
                      "Go back into the future and",            #Redo blurb
                      "Save your work into the'save",           #Save blurb
                      "Load a picture from the 'save"]          #Load blurb

sclickdescription3 = ["done so far? Wipe it all away",          #Clear blurb
                      "mainstream for you? Fill the",           #Bucket blurb
                      "something that you did. Clean",          #Undo blurb
                      "redo something that you undid.",         #Redo blurb
                      "files' folder.",                         #Save blurb
                      "files' folder."]                         #Load blurb

sclickdescription4 = ["& cleanse your sins.",                   #Clear blurb
                      "screen with a COLOUR!",                  #Bucket blurb
                      "up your mistakes.",                      #Undo blurb
                      "",                                       #Redo blurb
                      "",                                       #Save blurb
                      ""]                                       #Load blurb

stampboxes = [luminousRect,aranRect,evanRect,mercedesRect,phantomRect,demonslayerRect,mageRect,pirateRect,thiefRect,warriorRect,bowmanRect,blackmageRect]
stampfunction = ["luminous","aran","evan","mercedes","phantom","demonslayer","mage","pirate","thief","warrior","bowman","blackmage"]
stamps = [luminousstamp,aranstamp,evanstamp,mercedesstamp,phantomstamp,demonslayerstamp,magestamp,piratestamp,thiefstamp,warriorstamp,bowmanstamp,blackmagestamp]

stampdescription = ["Stamp - Luminous",
                    "Stamp - Aran",
                    "Stamp - Evan",
                    "Stamp - Mercedes",
                    "Stamp - Phantom",
                    "Stamp - Demonslayer",
                    "Stamp - Blaze Wizard",
                    "Stamp - Pirate",
                    "Stamp - Nightwalker",
                    "Stamp - Warrior",
                    "Stamp - Wind Archer",
                    "Stamp - The Black Mage"]

stampdescription2 = ["Luminous is one of the five he-",     #Luminous Description
                     "Aran is one of the five heros",       #Aran Description
                     "Evan is one of the five heros",       #Evan Description
                     "Mercedes is one of the five",         #Mercedes Description
                     "Phantom is one of the five her-",     #Phantom Description
                     "Demon was a servant of the",          #Demonslayer Description
                     "Blaze Wizards pray to Ignis,",        #Blaze Wizard Description
                     "Pirates are the scourge of the",      #Pirate Description
                     "Nightwalkers worship Umbra,",         #Nightwalker Description
                     "Warriors are some of the tou-",       #Warrior Description
                     "The Wind Archers are elite",          #Wind Archer Description
                     "The Black is the Trancendence"]       #The Black Mage Description

stampdescription3 = ["ros who defeated the Black",          #Luminous Description
                     "who defeated the Black Mage.",        #Aran Description
                     "who defeated the Black Mage.",        #Evan Description
                     "heros who defeated the Black",        #Mercedes Description
                     "os who defeated the Black",           #Phantom Description
                     "Black Mage, but he fought back",      #Demonslayer Description
                     "the spirit of fire to cast power-",   #Blaze Wizard Description
                     "sea. They are expert shots as",       #Pirate Description
                     "the spirit of darkness. They",        #Nightwalker Description
                     "ghest people in Maple World.",        #Warrior Description
                     "band of marksmen, or markswo-",       #Wind Archer Description
                     "of light, but he became consum-"]     #The Black Mage Description

stampdescription4 = ["Mage. He was the one who fin-",       #Luminous Description
                     "she specializes in ice attacks.",     #Aran Description
                     "Evan was a simple farm boy un-",      #Evan Description
                     "Mage and also the Queen of",          #Mercedes Description
                     "Mage and a notorious thief.",         #Phantom Description
                     "after the destruction of his vil-",   #Demonslayer Description
                     "ful fire magic. They are a part",     #Blaze Wizard Description
                     "well as fearsome melee fighte-",      #Pirate Description
                     "are some of the most skillful,",      #Nightwalker Description
                     "They specialize in a multitude",      #Warrior Description
                     "men. They are said to be able",       #Wind Archer Description
                     "ed by darkness. In the final b-"]     #The Black Mage Description
                     
stampdescription5 = ["ished the Black Mage, but he",        #Luminous Description
                     "In the battle against the Black",     #Aran Description
                     "til he found a onyx-dragon egg.",     #Evan Description
                     "the Elves. During the confict",       #Mercedes Description
                     "When the Black Mage killed his",      #Phantom Description
                     "liage. In an attempt to slay the",    #Demonslayer Description
                     "of the Cygnus Knights, an order",     #Blaze Wizard Description
                     "rs.",                                 #Pirate Description
                     "cunning and secretive people in",     #Nightwalker Description
                     "of weapons and come from a",          #Warrior Description
                     "to control the wind. They are a",     #Wind Archer Description
                     "attle, He was sealed away by "]       #The Black Mage Description
                     
stampdescription6 = ["became tainted by the Black",         #Luminous Description
                     "Mage, she was cursed and sea-",       #Aran Description
                     "During the battle with the Bla-",     #Evan Description
                     "with the Black Mage, she and",        #Mercedes Description
                     "beloved, Aria, he joined the",        #Phantom Description
                     "Black Mage, he was sealed aw-",       #Demonslayer Description
                     "devoted to protecting the wor-",      #Blaze Wizard Description
                     "",                                    #Pirate Description
                     "Maple World. Nightwalkers are",       #Nightwalker Description
                     "variety of backgrounds: from",        #Warrior Description
                     "branch of the Cygnus Knights,",       #Wind Archer Description
                     "Luminous. Before he vanished,"]       #The Black Mage Description
                     
stampdescription7 = ["Mage's dark magic. He constan-",      #Luminous Description
                     "led away in a cave until she",        #Aran Description
                     "ck Mage, Evan was slain, but",        #Evan Description
                     "her people were frozen. She",         #Mercedes Description
                     "heros. He disappeared during",        #Phantom Description
                     "ay. 100 years later, he revived",     #Demonslayer Description
                     "ld against the Dark Mage and",        #Blaze Wizard Description
                     "",                                    #Pirate Description
                     "a branch of the Cygnus Knights,",     #Nightwalker Description
                     "Paladins, to Dark Knights, to",       #Warrior Description
                     "an order devoted to protecting",      #Wind Archer Description
                     "he cursed all five heros. He is"]     #The Black Mage Description
                     
stampdescription8 = ["tly struggles against the dark.",     #Luminous Description
                     "was revived a century later.",        #Aran Description
                     "his legacy lives on.",                #Evan Description
                     "was revived a century later.",        #Mercedes Description
                     "the fight with the Black Mage.",      #Phantom Description
                     "and became the Demonslayer.",         #Demonslayer Description
                     "all other evils.",                    #Blaze Wizard Description
                     "",                                    #Pirate Description
                     "who serve justice and peace.",        #Nightwalker Description
                     "Heros.",                              #Warrior Description
                     "peace and justice.",                  #Wind Archer Description
                     "now trying to revive himself."]       #The Black Mage Description

colourboxes = [colourRect,colour2Rect]
colourfunction = ["colour","colour2"]

points = []

tool = "pencil"     #this variable is used for all the Drawing Tools                        #Only the 'tool' variable actually does any drawing. The rest of
colour = ""         #This variable controls which colour palette is being used              #These variables are used so that it doesn't disturb the smooth-
sclick = ""         #this variable controls Single click icons                              #ness of the program. This way, they don't interfere with the
music = "play"      #this variable controls music                                           #actual drawing and everything is more user friendly.

c = ((0,0,0))                   #colour value in RGB
start = 0,0
size = 1                        #the size of most of the tools

oldscreen = screen.subsurface(canvas).copy()
undo = [oldscreen]
redo = [oldscreen]

y = 20
message = ""

labelmusic = "Play/Pause"            #these variables are used in the text display after
labelsize = "Size:      (scroll to change size)" 
labelcolour = "Colour:"
labelpixel = "Pixels:          ,"
#------------------------GRAPHICS--------------------------------------------------------------------------------------------------------------

running = True
while running:
    click = False
    lift = False
    lftclick = False
    for evnt in event.get():
        if evnt.type == QUIT:
            running=False
        if evnt.type == MOUSEBUTTONDOWN:
            if evnt.button == 1:
                click = True
                if canvas.collidepoint(mx,my): 
                    start = evnt.pos        #the starting points for drawing lines, rectangles, ellipses etc.
            if evnt.button == 3:
                lftclick = True
            if evnt.button == 4:
               size += 1
            if evnt.button == 5:
               size -= 1
               if size < 1: #ensures the size will never be 0 or less
                   size = 1
        if evnt.type == MOUSEBUTTONUP:
            if evnt.button == 1:
                if canvas.collidepoint(mx,my) or clearRect.collidepoint(mx,my) or bucketRect.collidepoint(mx,my):                    
                    oldscreen = screen.subsurface(canvas).copy()
                    undo.append(oldscreen)
                lift = True                                              

    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    
    if mb[0] == 1:              #this statement is to ensure that the redo list resets everytime something new happens
        if canvas.collidepoint(mx,my) or clearRect.collidepoint(mx,my) or bucketRect.collidepoint(mx,my):
            redo = []

#---COLOUR INDICATORS-------------------------
    draw.circle(screen,(c),(979,630),15)        #Slime's Eye
    draw.circle(screen,(0,0,0),(979,630),15,1)
    
    draw.circle(screen,(c),(1088,660),13)       #Slime's Tail Bulb Thingie
    draw.circle(screen,(0,0,0),(1088,660),13,1)
#---Drawing Boxes------------------------------
    for i in range(len(musicboxes)):
        draw.rect(screen,(0,0,0),musicboxes[i],2)
    for i in range(len(toolboxes)):
        draw.rect(screen,(0,0,0),toolboxes[i],2)
    for i in range(len(stampboxes)):
        draw.rect(screen,(0,0,0),stampboxes[i],2)
    for i in range(len(shapeboxes)):
        draw.rect(screen,(0,0,0),shapeboxes[i],2)
    for i in range(len(sclickboxes)):
        draw.rect(screen,(0,0,0),sclickboxes[i],2)

#---Colliding with and Clicking on Boxes to Get Tools, single click, music, and colour changes
    for i in range(len(musicboxes)):
        if musicboxes[i].collidepoint(mx,my) and click:
                music = musicfunction[i]
                
    for i in range(len(toolboxes)):
        if toolboxes[i].collidepoint(mx,my) and click:
                tool = toolfunction[i]
                
    for i in range(len(stampboxes)):
        if stampboxes[i].collidepoint(mx,my) and click:
                tool = stampfunction[i]
                
    for i in range(len(shapeboxes)):
        if shapeboxes[i].collidepoint(mx,my) and click:
                tool = shapefunction[i]
                
    for i in range(len(sclickboxes)):
        if sclickboxes[i].collidepoint(mx,my) and click:
                sclick = sclickfunction[i]
                
    for i in range(len(colourboxes)):
        if colourboxes[i].collidepoint(mx,my) and click:
                colour = colourfunction[i]
#---------------------Music -------------------------------------------
    if music == "pause":
        mixer.music.pause()
                 
    if music == "play":
        mixer.music.unpause()
#----------------------------------------------------------------------
    screen.set_clip(canvas)
#---------------------TOOLS--------------------------------------------    
    if tool == "pencil":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            draw.line(screen,c,(omx,omy),(mx,my),1)
        omx,omy = mx,my    #omx is the old "mx" point and is set after the drawing to ensure that these "omx,omy" points are actually the previous points
        
    if tool == "brush":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            draw.circle(screen,c,(mx,my),size)
            dist = int(((mx-omx)**2+(my-omy)**2)**0.5)
            for i in range(dist):
                sx = omx+(i*(mx-omx))//dist     #these 2 points are all the points between omx,omy and mx,my. Then a circle is drawn with these
                sy = omy+(i*(my-omy))//dist     #points at the centre to form a brush tool with no gaps inbetween.
                draw.circle (screen,c,(sx,sy),size)
        omx,omy = mx,my
        
    if tool == "eraser":                        #same concept as the brush
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            draw.circle(screen,(255,255,255),(mx,my),size)
            dist=int(((mx-omx)**2+(my-omy)**2)**0.5)
            for i in range(dist):
                sx = omx+(i*(mx-omx))//dist 
                sy = omy+(i*(my-omy))//dist
                draw.circle (screen,(255,255,255),(sx,sy),size)
        omx,omy = mx,my
        
    if tool == "spray":
        for i in range(size+20):
            if mb[0] == 1 and canvas.collidepoint(mx,my):
                rx = randint(-size-20,size+20)
                ry = randint(-size-20,size+20)
                if ((rx)**2+(ry)**2)**0.5 < size+20:
                    draw.circle(screen,c,(mx+rx,my+ry),0)   #these dots would draw randomly in a circulare area
    
    if tool == "eyedropper":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            c = screen.get_at((mx,my))
#---------------------SHAPES---------------------------------------
    
    if tool == "rectangle":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            screen.blit(oldscreen,(230,50))                     #blit oldscreen so that when the rectangle is dragged around, the previous ones dont stay 
            draw.rect(screen,c,(min(mx,omx),min(my,omy),abs(mx-omx),abs(my-omy)),size)
        omx,omy = start
            
            
    if tool == "ellipse":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            screen.blit(oldscreen,(230,50))
            if abs(omx-mx)/2 >size and abs(omy-my)/2 >size:   #ensures that the thickness is never greater than the radius
                draw.ellipse(screen,c,(min(omx,mx),min(omy,my),abs(omx-mx),abs(omy-my)),size) 
        omx,omy = start                                     #omx,omy = start is done so that abs can be used

    if tool == "fillrectangle":                             
        if mb[0] == 1 and canvas.collidepoint(mx,my):       
            screen.blit(oldscreen,(230,50))                 
            draw.rect(screen,c,(min(mx,omx),min(my,omy),abs(mx-omx),abs(my-omy)))   #abs makes it so that the rectangle will draw whether the omx,omy are 
        omx,omy = start                                                             #are smaller or bigger

    if tool == "fillellipse":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            screen.blit(oldscreen,(230,50))
            draw.ellipse(screen,c,(min(omx,mx),min(omy,my),abs(omx-mx),abs(omy-my)))
        omx,omy = start
        
    if tool == "polygon":
        if lift and canvas.collidepoint(mx,my):
            points += [(mx,my)]
        if lftclick == True:
            if len(points) >= 2:
                draw.polygon(screen,c,points,size)
                points = []
            
    if tool == "fillpolygon":
        if lift and canvas.collidepoint(mx,my):
            points += [(mx,my)]
        if lftclick == True:
            if len(points) >= 2:
                draw.polygon(screen,c,points)
                points = []

    if tool == "line":
        if mb[0] == 1 and canvas.collidepoint(mx,my):
            screen.blit(oldscreen,(230,50))
            draw.line(screen,c, start,(mx,my),size)
#---------------------EXTRA------------------------------       
    if sclick == "clear":
        draw.rect(screen,(255,255,255),canvas)
        sclick = ""

    if sclick == "bucket":
        draw.rect(screen,c,canvas)
        sclick = ""
        
    if sclick == "undo":
        if len(undo)-1 >= 1:        #this way, the program doesn't crash if the list is 0
            redo.append(undo[-1])
            undo.remove(undo[-1])
            screen.blit(undo[-1],(230,50))
            oldscreen = undo[-1]
        sclick = ""

    if sclick == "redo":
        if len(redo) >= 1:
            screen.blit(redo[-1],(230,50))
            oldscreen = redo[-1]
            undo.append(redo[-1])
            redo.remove(redo[-1])
        sclick = ""        
#---------------------COLOUR PALETTES----------------------------------  
    if colour == "colour":
        if click and mb[0] ==1 and colourRect.collidepoint(mx,my):
            c = screen.get_at((mx,my))
    if colour == "colour2":
        if click and mb[0] ==1 and colour2Rect.collidepoint(mx,my):
            c = screen.get_at((mx,my))            
#---------------------STAMPS-----------------------------------------------------
    for i in range(len(stampfunction)):                                             
        if tool == stampfunction[i]:
            if mb[0] == 1 and canvas.collidepoint(mx,my):       #if the right mouse button is held down, then the stamp can be dragged around
                screen.blit(oldscreen,(230,50))                 #and when it lifts, it will stamp
                screen.blit(stamps[i],(mx-70,my-75))

            if tool == "blackmage":                             #Since the Black Mage is so much larger than the other stamps,
                if mb[0] == 1 and canvas.collidepoint(mx,my):   #the mouse point has to be at a different point to be closer to the centre
                    screen.blit(oldscreen,(230,50))
                    screen.blit(blackmagestamp,(mx-150,my-100))    
#-----------------------------------------------------------------------------------------------------
    screen.set_clip(None)
#-----------------------------------------------------------------------------------------------------        
    if sclick == "save":                                        #This is outside the clippings so that the typing box will draw properly
        txt = getName(screen,False)
        txtPic = font.render(txt,True,(255,255,255))
        screen.blit(txtPic,(0,0))
        image.save(screen.subsurface(canvas),"save files/"+txt+".png")
        sclick = ""

    if sclick == "load":
        txt = getName(screen,False)
        txtPic = font.render(txt,True,(255,255,255))
        try:                                                    #program won't crash if image isn't found in the folder
            load = image.load("save files/"+txt+".png")
            screen.blit(load,(230,50))
        except error:
            None
        sclick = ""
                                                        
    for i in range(len(musicboxes)):
        if musicboxes[i].collidepoint(mx,my):#if the mouse hovers over the button, then the button will glow yellow to signal it can be clicked
            draw.rect(screen,(0,0,255),musicboxes[i],2)
        if music == musicfunction[i]:
            draw.rect(screen,(255,0,0),musicboxes[i],2)#shows which tool is selected
            
    for i in range(len(toolboxes)):
        if toolboxes[i].collidepoint(mx,my):#if the mouse hovers over the button, then the button will glow yellow to signal it can be clicked
            draw.rect(screen,(0,0,255),toolboxes[i],2)            
        if tool == toolfunction[i]:
            draw.rect(screen,(255,0,0),toolboxes[i],2)#shows which tool is selected
            draw.rect(screen,(255,255,255),(15,300,207,190))#Text box
            draw.rect(screen,(0,0,0),(15,300,207,190),1)
            
            txtpic = font.render(tooldescription[i],True,(0,0,0))       #these are used to blit the descriptions inside of the text box
            txtpic2 = font.render(tooldescription2[i],True,(0,0,0))
            txtpic3 = font.render(tooldescription3[i],True,(0,0,0))
            txtpic4 = font.render(tooldescription4[i],True,(0,0,0))
            screen.blit(txtpic,(25,300))
            screen.blit(txtpic2,(25,320))
            screen.blit(txtpic3,(25,335))
            screen.blit(txtpic4,(25,350))

    for i in range(len(stampboxes)):
        if stampboxes[i].collidepoint(mx,my):
            draw.rect(screen,(0,0,255),stampboxes[i],2)
        if tool == stampfunction[i]:
            draw.rect(screen,(255,0,0),stampboxes[i],2)
            draw.rect(screen,(255,255,255),(15,300,207,190))
            draw.rect(screen,(0,0,0),(15,300,207,190),1)
            
            txtpic = font.render(stampdescription[i],True,(0,0,0))
            txtpic2 = font.render(stampdescription2[i],True,(0,0,0))
            txtpic3 = font.render(stampdescription3[i],True,(0,0,0))
            txtpic4 = font.render(stampdescription4[i],True,(0,0,0))
            txtpic5 = font.render(stampdescription5[i],True,(0,0,0))
            txtpic6 = font.render(stampdescription6[i],True,(0,0,0))
            txtpic7 = font.render(stampdescription7[i],True,(0,0,0))
            txtpic8 = font.render(stampdescription8[i],True,(0,0,0))
            screen.blit(txtpic,(25,300))
            screen.blit(txtpic2,(25,320))
            screen.blit(txtpic3,(25,335))
            screen.blit(txtpic4,(25,350))
            screen.blit(txtpic5,(25,365))
            screen.blit(txtpic6,(25,380))
            screen.blit(txtpic7,(25,395))
            screen.blit(txtpic8,(25,410))
                
    for i in range(len(shapeboxes)):
        if shapeboxes[i].collidepoint(mx,my):
            draw.rect(screen,(0,0,255),shapeboxes[i],2)
        if tool == shapefunction[i]:
            draw.rect(screen,(255,0,0),shapeboxes[i],2)
            draw.rect(screen,(255,255,255),(15,300,207,190))
            draw.rect(screen,(0,0,0),(15,300,207,190),1)
            
            txtpic = font.render(shapedescription[i],True,(0,0,0))
            txtpic2 = font.render(shapedescription2[i],True,(0,0,0))
            txtpic3 = font.render(shapedescription3[i],True,(0,0,0))
            txtpic4 = font.render(shapedescription4[i],True,(0,0,0))
            txtpic5 = font.render(shapedescription5[i],True,(0,0,0))
            txtpic6 = font.render(shapedescription6[i],True,(0,0,0))
            screen.blit(txtpic,(25,300))
            screen.blit(txtpic2,(25,320))
            screen.blit(txtpic3,(25,335))
            screen.blit(txtpic4,(25,350))
            screen.blit(txtpic5,(25,365))
            screen.blit(txtpic6,(25,380))
            
    for i in range(len(sclickboxes)):
        if sclickboxes[i].collidepoint(mx,my):      #these work on collidepoint because they are single click functions
            draw.rect(screen,(255,255,0),sclickboxes[i],2)
            draw.rect(screen,(255,255,255),(15,300,207,190))
            draw.rect(screen,(0,0,0),(15,300,207,190),1)
            
            txtpic = font.render(sclickdescription[i],True,(0,0,0))
            txtpic2 = font.render(sclickdescription2[i],True,(0,0,0))
            txtpic3 = font.render(sclickdescription3[i],True,(0,0,0))
            txtpic4 = font.render(sclickdescription4[i],True,(0,0,0))
            screen.blit(txtpic,(25,300))
            screen.blit(txtpic2,(25,320))
            screen.blit(txtpic3,(25,335))
            screen.blit(txtpic4,(25,350))
            
    draw.rect(screen,(255,255,255),(133,577,70,15))
    
    musictxt =  font.render(labelmusic,True,(0,0,0))
    screen.blit(musictxt,(133,577))
    
    draw.rect(screen,(255,255,255),(45,430,100,15))
    txtlabelsize = font.render(labelsize,True,(0,0,0))#displays the word "size:" before the actual size is displayed
    txtsize = font.render(str(size),True,(0,0,0))#displays the size
    screen.blit(txtlabelsize,(25,430))
    screen.blit(txtsize,(60,430))
    
    txtlabelpixel = font.render(labelpixel,True,(0,0,0))
    txtpixel1 = font.render(str(mx),True,(0,0,0))       #these display the coordinates that the mouse is at
    txtpixel2 = font.render(str(my),True,(0,0,0))
    screen.blit(txtlabelpixel,(25,450))
    screen.blit(txtpixel1,(70,450))
    screen.blit(txtpixel2,(115,450))

    txtlabelcolour = font.render(labelcolour,True,(0,0,0))#display the word "colour:"
    txtcolour = font.render(str(c),True,(0,0,0))#displays the colour value in RGB
    screen.blit(txtlabelcolour,(25,470))
    screen.blit(txtcolour,(75,470))

    display.flip() 
quit()
