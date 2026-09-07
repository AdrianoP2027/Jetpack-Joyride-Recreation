'''
Adriano P
May - June 2025
This is a replica of Jetpack Joyride, where you dodge obstacles forever
'''

import pgzrun
import os
import random
import time

#***Known Bugs******************#

#User cannot select normal flame after a colored flame is purchased.
#Cosmetics Menu says "you do not own this flame", when you might own it.
#To equip cosmetics press the number of the flame you own and press enter 2-3 times to ensure it selects.
#Hitboxes of zappers are slightly bigger than actual zappers. ( You might die even if you didn't visually touch an obstacle)
#Scrolling Background might sometimes have a gap.

#_______________________________#


#***Game Environment Settings***#
os.environ['SDL_VIDEO_CENTERED'] = '1'

TITLE = 'Jetpack Joyride'

#Set screen size
WIDTH = 1000
HEIGHT = 600

#_______________________________#


#---Global Variables------------#

#Setup Music
GamePlayMusic = 'jetpackjoyride'

#Setup Player
Player = Actor('barry')

#Player animation frames
PlayerRunFrames = ['walk1', 'walk2', 'walk3']
PlayerFlyFrame = 'barry'
PlayerFrameIndex = 0
PlayerLastFrameTime = time.time()

#Setup Jetpack
JetFlameFramesNormal = ['normalflame1', 'normalflame2', 'normalflame3']
JetFlameFramesRed = ['redflame1', 'redflame2', 'redflame3' ]
JetFlameFramesOrange= ['orangeflame1', 'orangeflame2', 'orangeflame3' ]
JetFlameFramesYellow= ['yellowflame1', 'yellowflame2', 'yellowflame3' ]
JetFlameFramesGreen= ['greenflame1', 'greenflame2', 'greenflame3' ]
JetFlameFramesBlue= ['blueflame1', 'blueflame2', 'blueflame3' ]
JetFlameFramesPurple= ['purpleflame1', 'purpleflame2', 'purpleflame3' ]
JetFlameFramesPink= ['pinkflame1', 'pinkflame2', 'pinkflame3' ]
JetFlameFramesGrey= ['greyflame1', 'greyflame2', 'greyflame3' ]
JetFlameFramesWhite= ['whiteflame1', 'whiteflame2', 'whiteflame3' ]

JetFlameFrameIndex = 0
JetFlameLastFrameTime = time.time()
JetFlame = Actor(JetFlameFramesNormal[0])
JetFlame.visible = False
IsThrusting = False
JetpackPower = 7  

#Scrolling background setup
Background1 = Actor('gamebackground')
Background2 = Actor('gamebackground')
Background1.x = WIDTH // 2
Background2.x = WIDTH + WIDTH // 2
Background1.y = HEIGHT // 2
Background2.y = HEIGHT // 2

#Normal Variables
GameState = -2
Score = 0
Coins = 0
Gravity = 0.5
VSpeed = 0
GroundY = 490
LastScoreTime = 0
LastSpawnTime = 0
HighScore = 0
PowerUpTimer = 0
ActivePowerUp = None
KeyPressed = None

#Boolean Variables
Bought = False
NotEnoughCoins = False
ConfirmSelect = False
NotInInventory = False
Selected = False
ConfirmPurchase = False

#Lists
PowerUps = []
CoinActors = []
Inventory = []
Obstacles = []

#Loading Screen Variables#
LoadingStartTime = time.time()
LoadingBarWidth = 0
RotationAngle = 0
CurrentTip = ""
Tips = [
    "TIP: Tap SPACE to control your altitude!",
    "TIP: Collect coins to unlock new flames!",
    "TIP: The shield lasts for five seconds!",
    "TIP: Avoid zappers and missiles to survive!"
]


LoadingLogo = Actor("star1")
LoadingLogo.x = WIDTH // 2
LoadingLogo.y = HEIGHT // 2 - 100

#GAMESTATES

#-2 --> Start Screen
#-1 --> Loading
# 0 --> Menu
# 1 --> In Game
# 2 --> Cosmetics
# 3 --> Shop
# 4 --> Game Over
# 5 --> Tutorial

#_______________________________#

#***Functions*******************#

#Initialize Game
def InitGame():
    global GameState
    global Player
    global Obstacles
    global Score
    global Coins
    global LastSpawnTime
    global LastScoreTime
    global GamePlayMusic

    #Reset score and timer
    Score = 0
    LastScoreTime = time.time()

    #Setup the Player
    Player.x = 50
    Player.y = 490

    #Setup the Obstacles
    Obstacles = []

    #Reset timer for spawning sbstacles
    LastSpawnTime = time.time()

    #Setup Sounds
    music.stop()
    music.play(GamePlayMusic)
    music.set_volume(1.5)  #Control volume

    #Load the highscore
    LoadHighScore()

#Draw the menu on the screen
def ShowMenu():
    screen.clear()
    Background.draw()
    screen.draw.text(str("Jetpack Joyride"),(360, 30), fontname="monogram", fontsize = 50)
    screen.draw.text(str("Press 1 to Start"), (390, 250), fontname="monogram", fontsize = 36)
    screen.draw.text(str("Press 2 for Cosmetics"), (355, 300), fontname="monogram", fontsize = 36)
    screen.draw.text(str("Press 3 for Shop"), (390, 350), fontname="monogram", fontsize = 36)
    screen.draw.text(str("Press 4 to Quit"), (400, 400), fontname="monogram", fontsize = 36)
    screen.draw.text(str("Press 5 for Tutorial"), (370, 450), fontname="monogram", fontsize = 36)

#Draw the menu for Game Over
def ShowGameOver():
    screen.clear()
    screen.draw.text(str("GAME OVER!"), (400, 30), fontname="monogram", fontsize = 50)
    screen.draw.text(str("Press 1 for Menu"), (380, 250), fontname="monogram", fontsize = 36)
    screen.draw.text(str("Press 2 to Quit"), (385, 300), fontname="monogram", fontsize = 36)
    screen.draw.text(str(f"Your score was {Score}"), (383, 400), fontname="monogram", fontsize = 36)
    screen.draw.text(str(f"High Score: {HighScore}"), (383, 440), fontname="monogram", fontsize = 36)

#Draw the menu for Cosmetics
def Cosmetics():
    screen.clear()
    Background.draw()
    screen.draw.text("Cosmetics", center=(WIDTH // 2, 50), fontsize=60, fontname="monogram", color="white")
    screen.draw.text("Press ENTER to confirm", (370, 100), fontsize=30, fontname="monogram", color="white")
    screen.draw.text("Red Flame  (Press 1)" , (350, 130), fontsize=30, fontname="monogram", color="red")
    screen.draw.text("Orange Flame (Press 2)" , (340, 170), fontsize=30, fontname="monogram", color="orange")
    screen.draw.text("Yellow Flame (Press 3)" , (340, 210), fontsize=30, fontname="monogram", color="yellow")
    screen.draw.text("Green Flame (Press 4)" , (345, 250), fontsize=30, fontname="monogram", color="green")
    screen.draw.text("Blue Flame (Press 5)" , (350, 290), fontsize=30, fontname="monogram", color="blue")
    screen.draw.text("Purple Flame (Press 6)" , (340, 330), fontsize=30, fontname="monogram", color="purple")
    screen.draw.text("Pink Flame (Press 7)" , (350, 370), fontsize=30, fontname="monogram", color="pink")
    screen.draw.text("Grey Flame (Press 8)" , (350, 410), fontsize=30, fontname="monogram", color= "grey")
    screen.draw.text("White Flame (Press 9)" , (340, 450), fontsize=30, fontname="monogram", color="white")
    screen.draw.text("Normal Flame (Press 0)" , (340, 490), fontsize=30, fontname="monogram", color="Black")
    screen.draw.text("ESC" , (20, 40), fontsize=30, fontname="monogram", color="White")
    screen.draw.text("<--" , (20, 65), fontsize=30, fontname="monogram", color="White")

#Draw the menu for shop
def ShowShop():
    screen.clear()
    Background = Actor('shopbackground')
    Background.draw()
    screen.draw.text("SHOP", center=(WIDTH // 2, 50), fontsize=60, fontname="monogram", color="white")
    screen.draw.text(f"Coins: {Coins}", (WIDTH - 200, HEIGHT - 100), fontsize=40, fontname="monogram", color="white")
    screen.draw.text("Red Flame - 25 coins (Press 1)" , (350, 130), fontsize=30, fontname="monogram", color="red")
    screen.draw.text("Orange Flame - 25 coins (Press 2)" , (340, 170), fontsize=30, fontname="monogram", color="orange")
    screen.draw.text("Yellow Flame - 25 coins (Press 3)" , (340, 210), fontsize=30, fontname="monogram", color="yellow")
    screen.draw.text("Green Flame - 25 coins (Press 4)" , (345, 250), fontsize=30, fontname="monogram", color="green")
    screen.draw.text("Blue Flame - 25 coins (Press 5)" , (350, 290), fontsize=30, fontname="monogram", color="blue")
    screen.draw.text("Purple Flame - 25 coins (Press 6)" , (340, 330), fontsize=30, fontname="monogram", color="purple")
    screen.draw.text("Pink Flame - 25 coins (Press 7)" , (350, 370), fontsize=30, fontname="monogram", color="pink")
    screen.draw.text("Grey Flame - 25 coins (Press 8)" , (350, 410), fontsize=30, fontname="monogram", color= "grey")
    screen.draw.text("White Flame - 25 coins (Press 9)" , (340, 450), fontsize=30, fontname="monogram", color="white")
    screen.draw.text("Normal Flame - free (Press 0)" , (340, 490), fontsize=30, fontname="monogram", color="Black")
    screen.draw.text("ESC" , (20, 40), fontsize=30, fontname="monogram", color="White")
    screen.draw.text("<--" , (20, 65), fontsize=30, fontname="monogram", color="White")

#Check inventory for Flame
def CheckInventory():
    global GameState
    global Selected
    global NotInInventory
    global JetFlameFramesNormal
   
    #If Player selected red Flame
    if KeyPressed == 1:
        if JetFlameFramesRed in Inventory:
            JetFlameFramesNormal = JetFlameFramesRed
            Selected = True
            NotInInventory = False

    #If Player selected orange Flame
    if KeyPressed == 2:
        if JetFlameFramesOrange in Inventory:
            JetFlameFramesNormal = JetFlameFramesOrange
            Selected = True
            NotInInventory = False
            
    #If Player selected yellow Flame
    if KeyPressed == 3:
        if JetFlameFramesYellow in Inventory:
            JetFlameFramesNormal = JetFlameFramesYellow
            Selected = True
            NotInInventory = False

    #If Player selected green Flame
    if KeyPressed == 4:
        if JetFlameFramesGreen in Inventory:
            JetFlameFramesNormal = JetFlameFramesGreen
            Selected = True
            NotInInventory = False

    #If Player selected blue Flame
    if KeyPressed == 5:
        if JetFlameFramesBlue in Inventory:
            JetFlameFramesNormal = JetFlameFramesBlue
            Selected = True
            NotInInventory = False

    #If Player selected purple Flame
    if KeyPressed == 6:
        if JetFlameFramesPurple in Inventory:
            JetFlameFramesNormal = JetFlameFramesPurple
            Selected = True
            NotInInventory = False   

    #If Player selected pink Flame
    if KeyPressed == 7:
        if JetFlameFramesPink in Inventory:
            JetFlameFramesNormal = JetFlameFramesPink
            Selected = True
            NotInInventory = False

    #If Player selected grey Flame
    if KeyPressed == 8:
        if JetFlameFramesGrey in Inventory:
            JetFlameFramesNormal = JetFlameFramesGrey
            Selected = True
            NotInInventory = False

    #If Player selected white Flame
    if KeyPressed == 9:
        if JetFlameFramesWhite in Inventory:
            JetFlameFramesNormal = JetFlameFramesWhite
            Selected = True
            NotInInventory = False   

    #If Player selected normal Flame
    if KeyPressed == 0:
        Inventory.append(JetFlameFramesNormal)
        JetFlameFramesNormal = JetFlameFramesNormal
        Selected = True
        NotInInventory = False

#Purchase Flame
def BuyFlame():
    global Bought
    global GameState
    global Coins
   
    #If Player selected red Flame
    if KeyPressed == 1:
        if JetFlameFramesRed not in Inventory:
            Inventory.append(JetFlameFramesRed)
            Coins -= 25
            Bought = True

    #If Player selected orange Flame
    if KeyPressed == 2:
        if JetFlameFramesOrange not in Inventory:
            Inventory.append(JetFlameFramesOrange)
            Coins -= 25
            Bought = True

    #If Player selected yellow Flame
    if KeyPressed == 3:
        if JetFlameFramesYellow not in Inventory:
            Inventory.append(JetFlameFramesYellow)
            Coins -= 25
            Bought = True

    #If Player selected green Flame
    if KeyPressed == 4:
        if JetFlameFramesGreen not in Inventory:
            Inventory.append(JetFlameFramesGreen)
            Coins -= 25
            Bought = True

    #If Player selected blue Flame
    if KeyPressed == 5:
        if JetFlameFramesBlue not in Inventory:
            Inventory.append(JetFlameFramesBlue)
            Coins -= 25
            Bought = True
 
    #If Player selected purple Flame
    if KeyPressed == 6:
        if JetFlameFramesPurple not in Inventory:
            Inventory.append(JetFlameFramesPurple)
            Coins -= 25
            Bought = True
 
    #If Player selected pink Flame
    if KeyPressed == 7:
        if JetFlameFramesPink not in Inventory:
            Inventory.append(JetFlameFramesPink)
            Coins -= 25
            Bought = True
 
    #If Player selected grey Flame
    if KeyPressed == 8:
        if JetFlameFramesGrey not in Inventory:
            Inventory.append(JetFlameFramesGrey)
            Coins -= 25
            Bought = True

    #If Player selected white Flame
    if KeyPressed == 9:
        if JetFlameFramesWhite not in Inventory:
            Inventory.append(JetFlameFramesWhite)
            Coins -= 25
            Bought = True
    
#Load High Score
def LoadHighScore():
    global HighScore
    try:
        with open("highscore.txt", "r") as File:
            HighScore = int(File.read())
    except:
        HighScore = 0

#Save High Score
def SaveHighScore():
    with open("highscore.txt", "w") as File:
        File.write(str(HighScore))

#Spawn Power Up
def SpawnPowerUp():
    if random.random() < 0.05:  # 5% chance
        PowerUp = Actor('powerup')
        PowerUp.x = random.randint(1070, 1570)
        PowerUp.y = 490
        PowerUp.speed = -6
        PowerUp.Type = 'shield'
        PowerUps.append(PowerUp)

#Draw the loading screen
def ShowLoadingScreen():
    global RotationAngle
    global LoadingBarWidth
    global CurrentTip

    screen.fill((15, 15, 15))  # Dark gray background

    #Rotate the logo using angle property
    LoadingLogo.angle += 3  #PGZRun built-in rotation
    LoadingLogo.draw()
    LoadingLogo.x = 500
    LoadingLogo.y = 250

    #Draw loading bar background
    BarX = WIDTH // 2 - 200
    BarY = HEIGHT // 2 + 20
    BarWidth = 400
    BarHeight = 25

    screen.draw.filled_rect(Rect((BarX, BarY), (BarWidth, BarHeight)), (50, 50, 50))

    #Draw loading bar fill
    LoadingBarWidth = min(LoadingBarWidth + 4, BarWidth)
    screen.draw.filled_rect(Rect((BarX, BarY), (LoadingBarWidth, BarHeight)), (0, 200, 0))


    #Draw title text
    screen.draw.text("Loading...", center= (WIDTH // 2 + 17, HEIGHT // 2 - 160), fontsize=50, fontname="monogram", color="white")

    #Show a random tip
    if CurrentTip == "":
        CurrentTip = random.choice(Tips)
    screen.draw.text(CurrentTip, center=(WIDTH // 2, HEIGHT // 2 + 70), fontsize=28, fontname="monogram", color="white")

#Draw the tutorial screen
def ShowTutorial():
    screen.clear()
    Background = Actor('shopbackground')
    Background.draw()
    screen.draw.text("HOW TO PLAY", center=(WIDTH // 2, 50), fontsize=60, fontname="monogram", color="white")
    screen.draw.text("USE SPACE or UP ARROW to FLY", (100, 120), fontsize=36, fontname="monogram", color="white")
    screen.draw.text("HOLD to KEEP FLYING - RELEASE to FALL", (100, 160), fontsize=30, fontname="monogram", color="lightgray")
    screen.draw.text("AVOID ZAPPERS AND MISSILES", (100, 220), fontsize=36, fontname="monogram", color="red")
    screen.draw.text("COLLECT POWER-UPS TO SURVIVE LONGER", (100, 270), fontsize=30, fontname="monogram", color="lightblue")
    screen.draw.text("COLLECT COINS TO BUY FLAMES", (100, 310), fontsize=30, fontname="monogram", color="yellow")
    screen.draw.text("POWER-UPS INCLUDE:", (100, 370), fontsize=34, fontname="monogram", color="white")
    screen.draw.text("- SHIELD (Blue Orb): Protects for five seconds", (120, 410), fontsize=28, fontname="monogram", color="blue")
    screen.draw.text("- MORE TO COME IN FUTURE UPDATES!", (120, 450), fontsize=28, fontname="monogram", color="gray")
    screen.draw.text("PRESS ESC TO RETURN TO MAIN MENU", (100, 520), fontsize=30, fontname="monogram", color="white")

    screen.draw.text("FYI: Please see known bugs in comments near top of code.", (100, 570), fontsize=30, fontname="monogram", color="green")

#Spawn the Obstacles
def SpawnObstacle():
    ObstacleTypes = ['missile', 'zapper', 'zapper2', 'zapper3', 'zapper4']
    ObstacleType = random.choice(ObstacleTypes)
    Obstacle = Actor(ObstacleType)
    Obstacle.x = WIDTH + 50  # Start offscreen right
    Obstacle.y = random.randint(100, GroundY - 50)  # Random vertical position
    Obstacle.speed = -6  # Speed moving left
    return Obstacle

#Show Start Menu
def ShowStartMenu():
    global MenuBackground
    screen.clear()
    MenuBackground = Actor('menu')
    MenuBackground.y = 300
    MenuBackground.x = 500
    MenuBackground.draw()
    screen.draw.text(str("Press enter to start"), (350, 530), fontname="monogram", fontsize = 36)

#Spawn Coins
def SpawnCoin():
    Coin = Actor('coin')
    Coin.x = random.randint(1070, 1570)
    Coin.y = random.randint(150, GroundY - 40)
    Coin.speed = -6
    CoinActors.append(Coin)

#Check if a certain key is pressed down
def on_key_down(key):
    global GameState
    global VSpeed
    global Coins
    global LoadingBarWidth
    global LoadingStartTime
    global RotationAngle
    global CurrentTip
    global Tips

    if GameState == -2:
        if key == keys.RETURN:
            #Continue . . .
            GameState = -1

    if GameState == 0:
        #Accepted down keys while in a menu.
        if key == keys.K_1:
            #Code to start game
            GameState = 1
            InitGame()

        if key == keys.K_2:
            #Code to select flame
            GameState = 2
            Cosmetics()
   
        if key == keys.K_3:
            #Code to create menu
            GameState = 3
            ShowShop()

        if key == keys.K_4:
            #Quit the game
            quit()

        if key == keys.K_5:
            # Go to tutorial screen
            GameState = 5  

    elif GameState == 1:
        if key == keys.SPACE or key == keys.UP:
            global IsThrusting
            IsThrusting = True

    elif GameState == 2:
        global ConfirmSelect
        global KeyPressed
        global Selected
        global NotInInventory

        if key == keys.ESCAPE:
            GameState = 0  # Cancel shop and go back to menu
            NotInInventory = True
            ConfirmSelect = False
            KeyPressed = 0

        elif key == keys.K_1:
            KeyPressed = 1
        elif key == keys.K_2:
            KeyPressed = 2
        elif key == keys.K_3:
            KeyPressed = 3
        elif key == keys.K_4:
            KeyPressed = 4
        elif key == keys.K_5:
            KeyPressed = 5
        elif key == keys.K_6:
            KeyPressed = 6
        elif key == keys.K_7:
            KeyPressed = 7
        elif key == keys.K_8:
            KeyPressed = 8
        elif key == keys.K_9:
            KeyPressed = 9
        elif key == keys.K_0:
            KeyPressed = 0       
       
        if KeyPressed >= 0 and KeyPressed <= 9:
            #Player selected a Flame
            ConfirmSelect = True
           
            if key == keys.RETURN:  # Confirm selection  
                CheckInventory()
                NotInInventory = False
            else:
                NotInInventory = True

    elif GameState == 3:
        global ConfirmPurchase
        global NotEnoughCoins

        if key == keys.ESCAPE:
            GameState = 0  # Cancel shop and go back to menu
            NotEnoughCoins = False
            ConfirmPurchase = False
            KeyPressed = 100

        elif key == keys.K_1:
            KeyPressed = 1
        elif key == keys.K_2:
            KeyPressed = 2
        elif key == keys.K_3:
            KeyPressed = 3
        elif key == keys.K_4:
            KeyPressed = 4
        elif key == keys.K_5:
            KeyPressed = 5
        elif key == keys.K_6:
            KeyPressed = 6
        elif key == keys.K_7:
            KeyPressed = 7
        elif key == keys.K_8:
            KeyPressed = 8
        elif key == keys.K_9:
            KeyPressed = 9
        elif key == keys.K_0:
            KeyPressed = 0
       
        if KeyPressed == 0 or KeyPressed <= 9 and KeyPressed > 0:
            #Player selected a Flame
            ConfirmPurchase = True
           
            if key == keys.RETURN:  # Confirm purchase/selection  
                if Coins >= 25:
                    BuyFlame()
                else:
                     NotEnoughCoins = True
       
    elif GameState == 4:
        if key == keys.K_1:
            GameState = 0
        elif key == keys.K_2:
            quit()

    elif GameState == 5:
        # Tutorial screen
        if key == keys.ESCAPE:
            GameState = 0  # Return to main menu

#Check if a certain key is not pressed
def on_key_up(key):
    global IsThrusting

    if GameState == 1:
        if key == keys.SPACE or key == keys.UP:
            IsThrusting = False

#_______________________________#

#---Game Functions--------------#

#Update - built in function for the code of all objects on the screen
def update():
    global GameState
    global Player
    global Score
    global VSpeed
    global LastSpawnTime
    global LastScoreTime
    global Obstacles
    global Coins
    global HighScore
    global ActivePowerUp
    global PowerUpTimer
    global JetFlameLastFrameTime
    global JetFlameFrameIndex
    global PlayerLastFrameTime
    global PlayerFrameIndex

    #Loading Screen
    if GameState == -1:
        if time.time() - LoadingStartTime > 3.0:
            global LoadingBarWidth
            global CurrentTip
            GameState = 0  #Move to Menu
            LoadingBarWidth = 0
            CurrentTip = ""
        return

    if GameState == 1:
        #In gameplay mode
        #Scroll background to the left
        Background1.x -= 2  
        Background2.x -= 2
        Background1.x = int(Background1.x)
        Background2.x = int(Background2.x)

        #Reset background positions to loop
        if Background1.x <= -WIDTH // 2:
            Background1.x = Background2.x + WIDTH -10  #Slight overlap
        if Background2.x <= -WIDTH // 2:
            Background2.x = Background1.x + WIDTH - 10

        #Jetpack thrust movement
        if IsThrusting:
            VSpeed = -JetpackPower  #Apply upward thrust
        else:
            VSpeed += Gravity       #Apply gravity when not thrusting

        Player.y += VSpeed

        #Animate player
        Now = time.time()
        if Now - PlayerLastFrameTime > 0.05:  #50ms between frames
            if Player.y < GroundY:  #In air
                Player.image = PlayerFlyFrame
            else:  #On ground = running
                PlayerFrameIndex = (PlayerFrameIndex + 1) % len(PlayerRunFrames)
                Player.image = PlayerRunFrames[PlayerFrameIndex]

            PlayerLastFrameTime = Now

        #Prevent flying above the screen
        if Player.y <= 40:  
            Player.y = 40
            VSpeed = 0

        #Prevent falling below ground
        if Player.y >= GroundY:
            Player.y = GroundY
            VSpeed = 0

        #Update jet flame position and visibility
        JetFlame.x = Player.x - 17
        JetFlame.y = Player.y + 30
        JetFlame.visible = IsThrusting

        #Animate jet flame if visible
        if IsThrusting:
            CurrentTime = time.time()
            if CurrentTime - JetFlameLastFrameTime > 0.1:  #Change frame every 0.1s
                JetFlameFrameIndex = (JetFlameFrameIndex + 1) % len(JetFlameFramesNormal)
                JetFlame.image = JetFlameFramesNormal[JetFlameFrameIndex]
                JetFlameLastFrameTime = CurrentTime

        #Move all the Obstacles
        for Obstacle in Obstacles:
            Obstacle.x += Obstacle.speed

            if Obstacle.x < -20:
                Obstacles.remove(Obstacle)

            #Collision check
            if Obstacle.colliderect(Player):
                if ActivePowerUp != 'shield':
                    music.stop()
                    GameState = 4
                    if Score > HighScore:
                        SaveHighScore()

        # Spawn new Obstacles at random heights every 1 second
        CurrentTime = time.time()
        if CurrentTime - LastSpawnTime > 1:
            Obstacles.append(SpawnObstacle())
            LastSpawnTime = CurrentTime

        #Increase score every 0.05 seconds
        if CurrentTime - LastScoreTime > 0.05:
            Score += 1
            LastScoreTime = CurrentTime

        if Score > HighScore:
            HighScore = Score

        #Spawn a power-up every few seconds
        if random.random() < 0.05: # 5% chance
            SpawnPowerUp()

        # Move and check collisions
        for PowerUp in PowerUps[:]:
            PowerUp.x += PowerUp.speed
            if PowerUp.x < -20:
                PowerUps.remove(PowerUp)
            if PowerUp.colliderect(Player):
                ActivePowerUp = PowerUp.Type
                PowerUpTimer = time.time()
                PowerUps.remove(PowerUp)

        #Handle active power-up (Shield for 5 seconds)
        if ActivePowerUp == 'shield':
            if time.time() - PowerUpTimer > 5:
                ActivePowerUp = None

        #Every few seconds, spawn a coin (3% chance every frame)
        if random.random() < 0.03:
            SpawnCoin()

        for Coin in CoinActors[:]:
            Coin.x += Coin.speed
            if Coin.x < -20:
                CoinActors.remove(Coin)
            if Coin.colliderect(Player):
                Coins += 1
                CoinActors.remove(Coin)

#Draw - built in function that draws all the objects on the screen
def draw():
    screen.clear()
    global Background
    global ConfirmPurchase
    global Bought
    global NotEnoughCoins
    global Selected
   
    #Draw Start Screen
    if GameState == -2:
        ShowStartMenu()

    #Draw Loading Screen
    if GameState == -1:
        ShowLoadingScreen()
        return

    #Draw based on the game state
    if GameState == 0:
        #We are in the main menu
        Background = Actor('shopbackground')
        ShowMenu()
   
    elif GameState == 1:
        #We are in the game

        #Setup the Background
        Background1.draw()
        Background2.draw()

        #Draw the Flame
        if JetFlame.visible:
            JetFlame.draw()

        #Draw the Player
        Player.draw()

        #Draw Obstacles
        for Obstacle in Obstacles:
            Obstacle.draw()

        #Draw the Coins
        for Coin in CoinActors:
            Coin.draw()

        #Draw the score top-right corner
        screen.draw.text(f"Score: {Score}", (WIDTH - 170, 30), fontsize=40, fontname="monogram", color="white")

        #Draw the coins top-right corner
        screen.draw.text(f"Coins: {Coins}", (WIDTH - 150, 80), fontsize=30, fontname="monogram", color="yellow")

        #Draw the Powerup
        for PowerUp in PowerUps:
            PowerUp.draw()

        if ActivePowerUp:
            screen.draw.text(f"Power: {ActivePowerUp}", (30, 30), fontsize=30, fontname="monogram", color="lightblue")

    elif GameState == 2:
        #We are in the Cosmetics Menu
        Cosmetics()

        if ConfirmSelect == True:
            screen.draw.text("Confirm Select? (Press Enter)" , (335, 550), fontsize=30, fontname="monogram", color="white")
            if Selected == True:
                Cosmetics()
                Selected = False

        if NotInInventory == True:
            Cosmetics()
            screen.draw.text("You do not own this Flame! (Press ESC)" , (335, 550), fontsize=30, fontname="monogram", color="white")
           
    elif GameState == 3:
        #We are in the shop
        ShowShop()
       
        if ConfirmPurchase == True:
            screen.draw.text("Confirm Purchase? (Press Enter)" , (335, 550), fontsize=30, fontname="monogram", color="white")
            if Bought == True:
                ShowShop()
                Bought = False
                ConfirmPurchase = False
       
        if NotEnoughCoins == True:
            ShowShop()
            screen.draw.text("Not Enough Coins! (Press ESC)" , (335, 550), fontsize=30, fontname="monogram", color="white")
           
    elif GameState == 4:
        #We are in game over
        ShowGameOver()

    elif GameState == 5:
        #---Tutorial Screen---#
        ShowTutorial()

#_______________________________#

#Run the game
pgzrun.go()
