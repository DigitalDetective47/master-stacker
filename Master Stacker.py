from copy import deepcopy
import json,math,pathlib,pygame,random
BigBagFull:tuple[int]=(12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29)
EmptyLine:list=[None,None,None,None,None,None,None,None,None,None,-1,-1,-1,-1,-1]
BlankBoard:list[list]=[deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),deepcopy(EmptyLine),[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
FrameDuration:float=50/3
KeyboardLayouts:tuple[dict[str,int]]=({"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"down":pygame.K_DOWN,"up":pygame.K_UP,"rotL":pygame.K_z,"rotR":pygame.K_x,"hold":pygame.K_c,"pause":pygame.K_SPACE},{"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"down":pygame.K_DOWN,"up":pygame.K_UP,"rotL":pygame.K_x,"rotR":pygame.K_z,"hold":pygame.K_c,"pause":pygame.K_SPACE},{"left":pygame.K_a,"right":pygame.K_d,"down":pygame.K_s,"up":pygame.K_w,"rotL":pygame.K_k,"rotR":pygame.K_l,"hold":pygame.K_SEMICOLON,"pause":pygame.K_SPACE},{"left":pygame.K_a,"right":pygame.K_d,"down":pygame.K_s,"up":pygame.K_w,"rotL":pygame.K_l,"rotR":pygame.K_k,"hold":pygame.K_SEMICOLON,"pause":pygame.K_SPACE},{"left":pygame.K_LEFT,"right":pygame.K_RIGHT,"down":pygame.K_DOWN,"up":pygame.K_SPACE,"rotL":pygame.K_z,"rotR":pygame.K_UP,"hold":pygame.K_x,"pause":pygame.K_p},{"left":pygame.K_a,"right":pygame.K_d,"down":pygame.K_s,"up":pygame.K_w,"rotL":pygame.K_q,"rotR":pygame.K_e,"hold":pygame.K_r,"pause":pygame.K_SPACE})
LineScores:tuple[int]=(0,50,125,375,1500,7500)
LineGarbage:tuple[int]=(0,0,1,2,4,6)
MultiplayerModes:frozenset[int]=frozenset({5,7})
PieceTilemaps:tuple[tuple[tuple[tuple]]]=((((None,None,None,None,None),(None,None,None,None,None),(None,None,None,None,None),(None,None,None,None,None),(None,None,None,None,None)),),(((None,None,None,None,None),(None,None,None,None,None),(None,None,112,None,None),(None,None,None,None,None),(None,None,None,None,None)),),(((None,None,None,None,None),(None,None,None,None,None),(None,None,280,276,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,274,None,None),(None,None,273,None,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,None,None),(None,168,172,164,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,162,None,None),(None,None,163,None,None),(None,None,161,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,306,None,None),(None,None,313,308,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,314,308,None),(None,None,305,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,312,310,None),(None,None,None,305,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,306,None),(None,None,312,309,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,None,None),(None,24,28,28,20),(None,None,None,None,None),(None,None,None,None,None)),((None,None,18,None,None),(None,None,19,None,None),(None,None,19,None,None),(None,None,17,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,34,None,None),(None,None,41,44,36),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,42,36),(None,None,None,35,None),(None,None,None,33,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,None,40,44,38),(None,None,None,None,33),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,34,None),(None,None,None,35,None),(None,None,40,37,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,50,None),(None,56,60,53,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,50,None,None),(None,None,51,None,None),(None,None,57,52,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,58,60,52,None),(None,49,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,56,54,None,None),(None,None,51,None,None),(None,None,49,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,74,70,None),(None,None,73,69,None),(None,None,None,None,None),(None,None,None,None,None)),),(((None,None,None,None,None),(None,None,90,84,None),(None,88,85,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,82,None,None),(None,None,89,86,None),(None,None,None,81,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,98,None,None),(None,104,109,100,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,98,None,None),(None,None,107,100,None),(None,None,97,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,104,110,100,None),(None,None,97,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,98,None,None),(None,104,103,None,None),(None,None,97,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,120,118,None),(None,None,None,121,116),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,114,None),(None,None,122,117,None),(None,None,113,None,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,130,None,None),(None,136,141,134,None),(None,None,None,129,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,130,None,None),(None,None,139,132,None),(None,136,133,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,130,None,None,None),(None,137,142,132,None),(None,None,129,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,138,132,None),(None,136,135,None,None),(None,None,129,None,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,146,None),(None,None,154,157,148),(None,None,145,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,152,150,None),(None,None,None,155,148),(None,None,None,145,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,146),(None,None,152,158,149),(None,None,None,145,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,146,None),(None,None,152,151,None),(None,None,None,153,148),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,None,None),(24,28,28,28,20),(None,None,None,None,None),(None,None,None,None,None)),((None,None,18,None,None),(None,None,19,None,None),(None,None,19,None,None),(None,None,19,None,None),(None,None,17,None,None))),(((None,None,None,None,None),(None,162,None,None,None),(None,169,172,172,164),(None,None,None,None,None),(None,None,None,None,None)),((None,None,170,164,None),(None,None,163,None,None),(None,None,163,None,None),(None,None,161,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,168,172,172,166),(None,None,None,None,161),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,162,None),(None,None,None,163,None),(None,None,None,163,None),(None,None,168,165,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,None,178),(None,184,188,188,181),(None,None,None,None,None),(None,None,None,None,None)),((None,None,178,None,None),(None,None,179,None,None),(None,None,179,None,None),(None,None,185,180,None),(None,None,None,None,None)),((None,None,None,None,None),(None,186,188,188,180),(None,177,None,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,184,182,None),(None,None,None,179,None),(None,None,None,179,None),(None,None,None,177,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,232,230,None,None),(None,None,233,236,228),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,226,None),(None,None,234,229,None),(None,None,227,None,None),(None,None,225,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,232,236,230,None),(None,None,None,233,228),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,226,None),(None,None,None,227,None),(None,None,234,229,None),(None,None,225,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,None,250,244),(None,248,252,245,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,242,None,None),(None,None,243,None,None),(None,None,249,246,None),(None,None,None,241,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,250,252,244),(None,248,245,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,242,None,None),(None,None,249,246,None),(None,None,None,243,None),(None,None,None,241,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,218,214,None),(None,None,217,221,212),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,218,214),(None,None,None,219,213),(None,None,None,209,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,None,216,222,214),(None,None,None,217,213),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,210,None),(None,None,218,215,None),(None,None,217,213,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,202,198,None),(None,200,205,197,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,194,None,None),(None,None,203,198,None),(None,None,201,197,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,202,206,196,None),(None,201,197,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,202,198,None,None),(None,201,199,None,None),(None,None,193,None,None),(None,None,None,None,None))),(((None,34,None,None,None),(None,41,44,38,None),(None,None,None,33,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,42,36,None),(None,None,35,None,None),(None,40,37,None,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,258,None,None),(None,None,259,None,None),(None,264,269,260,None),(None,None,None,None,None),(None,None,None,None,None)),((None,258,None,None,None),(None,267,268,260,None),(None,257,None,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,264,270,260,None),(None,None,259,None,None),(None,None,257,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,258,None),(None,264,268,263,None),(None,None,None,257,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,2,None,2,None),(None,9,12,5,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,10,4,None),(None,None,3,None,None),(None,None,9,4,None),(None,None,None,None,None)),((None,None,None,None,None),(None,None,None,None,None),(None,10,12,6,None),(None,1,None,1,None),(None,None,None,None,None)),((None,None,None,None,None),(None,8,6,None,None),(None,None,3,None,None),(None,8,5,None,None),(None,None,None,None,None))),(((None,2,None,None,None),(None,3,None,None,None),(None,9,12,4,None),(None,None,None,None,None),(None,None,None,None,None)),((None,10,12,4,None),(None,3,None,None,None),(None,1,None,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,8,12,6,None),(None,None,None,3,None),(None,None,None,1,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,2,None),(None,None,None,3,None),(None,8,12,5,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,2,None,None,None),(None,9,6,None,None),(None,None,9,4,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,10,4,None),(None,10,5,None,None),(None,1,None,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,8,6,None,None),(None,None,9,6,None),(None,None,None,1,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,2,None),(None,None,10,5,None),(None,8,5,None,None),(None,None,None,None,None),(None,None,None,None,None))),(((None,None,98,None,None),(None,104,111,100,None),(None,None,97,None,None),(None,None,None,None,None),(None,None,None,None,None)),),(((None,None,None,None,None),(None,None,None,274,None),(None,280,284,285,276),(None,None,None,None,None),(None,None,None,None,None)),((None,None,274,None,None),(None,None,275,None,None),(None,None,283,276,None),(None,None,273,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,280,286,284,276),(None,None,273,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,274,None),(None,None,280,279,None),(None,None,None,275,None),(None,None,None,273,None),(None,None,None,None,None))),(((None,None,None,None,None),(None,None,290,None,None),(None,296,301,300,292),(None,None,None,None,None),(None,None,None,None,None)),((None,None,290,None,None),(None,None,299,292,None),(None,None,291,None,None),(None,None,289,None,None),(None,None,None,None,None)),((None,None,None,None,None),(None,296,300,302,292),(None,None,None,289,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,None,290,None),(None,None,None,291,None),(None,None,296,295,None),(None,None,None,289,None),(None,None,None,None,None))),(((None,None,None,None,50),(None,None,58,60,53),(None,None,49,None,None),(None,None,None,None,None),(None,None,None,None,None)),((None,None,56,54,None),(None,None,None,51,None),(None,None,None,57,52),(None,None,None,None,None),(None,None,None,None,None))))
PlayerBoardPositions:tuple[tuple[tuple[int,int]]]=(((152,-72),(408,-72)),((72,-72),(280,-72),(488,-72)),((152,-152),(408,-152),(152,32),(408,32)),((72,-152),(280,-152),(488,-152),(152,32),(408,32)),((72,-152),(280,-152),(488,-152),(72,32),(280,32),(488,32)))
PlayerGarbageMeterPositions:tuple[tuple[tuple[int,int]]]=(((148,128),(404,128)),((68,128),(276,128),(484,128)),((148,48),(404,48),(148,232),(404,232)),((68,48),(276,48),(484,48),(148,232),(404,232)),((68,48),(276,48),(484,48),(68,232),(276,232),(484,232)))
PlayerHoldPositions:tuple[tuple[tuple[int,int]]]=(((104,96),(360,96)),((24,96),(232,96),(440,96)),((104,16),(360,16),(104,200),(360,200)),((24,16),(232,16),(440,16),(104,200),(360,200)),((24,16),(232,16),(440,16),(24,200),(232,200),(440,200)))
PlayerNextPositions:tuple[tuple[tuple[int,int]]]=(((240,96),(496,96)),((160,96),(368,96),(576,96)),((240,16),(496,16),(240,200),(496,200)),((160,16),(368,16),(576,16),(240,200),(496,200)),((160,16),(368,16),(576,16),(160,200),(368,200),(576,200)))
MediumBagFull:tuple[int]=(5,6,7,8,9,10,11)
Resolutions:tuple[tuple[int,int]]=((640,360),(1280,720),(1920,1080),(2560,1440),(3840,2160))
Root35:float=math.sqrt(35)
PiOverRoot35:float=math.pi/Root35
LevelScoreMultipliers:tuple[float]=tuple([(29*(math.sin(PiOverRoot35*math.sqrt(i))/math.pi-math.sqrt(i)*math.cos(PiOverRoot35*math.sqrt(i))/Root35)+1)for i in range(36)])
Root6Over3:float=math.sqrt(6)/3#sqrt(6)/3=1.5**(-1/2)
LevelSpeeds:tuple[float]=tuple([(Root6Over3**i*57.6650390625)for i in range(36)])#57.6650390625=1.5**10
SingleplayerModes:frozenset[int]=frozenset({1,2,3,4,6})
SmallBagFull:tuple[int]=(1,2,3,4)
VersionID:int=5
WallKickData:tuple[tuple[int]]=((0,1),(-1,0),(1,0),(-1,1),(1,1),(0,-1),(1,-1),(1,-1),(0,0))
del PiOverRoot35
del Root35
del Root6Over3
def blits(blitSequence:list[tuple[pygame.Surface,tuple[int,int],tuple[int,int,int,int]]])->None:
    global win
    for i in blitSequence:
        win.blit(i[0],(i[1][0]*scaleFactor//(smallMode+1),i[1][1]*scaleFactor//(smallMode+1)),(i[2][0]*scaleFactor//(smallMode+1),i[2][1]*scaleFactor//(smallMode+1),i[2][2]*scaleFactor//(smallMode+1),i[2][3]*scaleFactor//(smallMode+1)))
def drawText(text:str,pos:tuple[int,int],specialCharacterSubstitutions:dict[str,int]={})->None:
    blitData:list[tuple[pygame.Surface,tuple[int,int],tuple[int,int,int,int]]]=[]
    for i in range(len(text)):
        blitData.append((specialChars,(pos[0]+i*8,pos[1]),(specialCharacterSubstitutions[text[i]]%16*8,specialCharacterSubstitutions[text[i]]//16*8,8,8))if text[i]in specialCharacterSubstitutions else(font,(pos[0]+i*8,pos[1]),(ord(text[i])%16*8,(ord(text[i])-32*(ord(text[i])//128)-32)//16*8,8,8)))
    blits(blitData)
def updateBackground()->None:
    win.blit(currentBackground,(0,0))
def asset(path:pathlib.PurePath)->pygame.Surface:
    sourceImage=pygame.image.load(pathlib.Path("assets",pathlib.PurePath(path.with_name(path.name+".png"))))
    return pygame.transform.scale(sourceImage,(sourceImage.get_width()*scaleFactor//(smallMode+1),sourceImage.get_height()*scaleFactor//(smallMode+1)))
def drawPiece(x:int,y:int,pieceID:int,pieceR:int=0,ghost:bool=False)->None:
    blitdata=[]
    for x2 in range(5):
        for y2 in range(5):
            if PieceTilemaps[pieceID][pieceR][y2][x2]is not None and y+y2*8>=0:
                blitdata.append((ghosts if ghost else pieces,(x+x2*8,y+y2*8),(PieceTilemaps[pieceID][pieceR][y2][x2]//16*8,PieceTilemaps[pieceID][pieceR][y2][x2]%16*8,8,8)))
    blits(blitdata)
def testPieceCollision(player=None)->bool:
    for x in range(5):
        for y in range(5):
            if(PieceTilemaps[pieceID][pieceR][y][x]if player is None else PieceTilemaps[pieceID[player]][pieceR[player]][y][x])is not None and(gameBoard[pieceY+y][pieceX+x]if player is None else gameBoard[player][pieceY[player]+y][pieceX[player]+x])is not None:
                return True
    return False
def updateAssets()->None:
    global font
    global garbageMeter
    global ghosts
    global pieces
    global playerBoardMasks
    global scaleFactor
    global specialChars
    global win
    scaleFactor=resolution[1]//180
    if smallMode:
        garbageMeter=asset(pathlib.PurePath("meter"))
    else:
        specialChars=asset(pathlib.PurePath("spchr"))
        font=asset(pathlib.PurePath("font"))
    ghosts=asset(pathlib.PurePath("ghost"))
    pieces=asset(pathlib.PurePath("piece"))
    playerBoardMasks=((pygame.Rect(48*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(48*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(48*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(48*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(8*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)))
    win=pygame.display.set_mode(resolution,(pygame.FULLSCREEN if settings["fullscreen"]else 0))
try:
    with open("settings.json","x")as x:
        pass
except OSError:
    pass
settingsFile=open("settings.json","r+")
try:
    settings:dict={"controlSetting":0,"dasInit":12,"dasSpeed":2,"fullscreen":False,"garbageBlocking":True,"garbageType":1,"ghost":True,"maxLvl":20,"minLvl":0,"newBags":True,"resolutionSetting":0,"samePieces":False}|json.load(settingsFile)
except json.JSONDecodeError:
    settings:dict={"controlSetting":0,"dasInit":12,"dasSpeed":2,"fullscreen":False,"garbageBlocking":True,"garbageType":1,"ghost":True,"maxLvl":20,"minLvl":0,"newBags":True,"resolutionSetting":0,"samePieces":False}
if type(settings)!=dict:
    settings={"controlSetting":0,"dasInit":12,"dasSpeed":2,"fullscreen":False,"garbageBlocking":True,"garbageType":1,"ghost":True,"maxLvl":20,"minLvl":0,"newBags":True,"resolutionSetting":0,"samePieces":False}
if not(type(settings["controlSetting"])==int and 0<=settings["controlSetting"]<=5):
    settings["controlSetting"]=0
if type(settings["dasInit"])!=int or settings["dasInit"]<1:
    settings["dasInit"]=12
if type(settings["dasSpeed"])!=int or settings["dasSpeed"]<1:
    settings["dasSpeed"]=2
if type(settings["fullscreen"])!=bool:
    settings["fullscreen"]=False
if type(settings["garbageBlocking"])!=bool:
    settings["garbageBlocking"]=True
if not(type(settings["garbageType"])==int and 0<=settings["garbageType"]<=2):
    settings["garbageType"]=1
if type(settings["ghost"])!=bool:
    settings["ghost"]=True
if not(type(settings["maxLvl"])==int and 0<=settings["maxLvl"]<=35):
    settings["maxLvl"]=20
if not(type(settings["minLvl"])==int and 0<=settings["minLvl"]<=35):
    settings["minLvl"]=0
if settings["minLvl"]>settings["maxLvl"]:
    settings["maxLvl"]=20
    settings["minLvl"]=0
if type(settings["newBags"])!=bool:
    settings["newBags"]=True
if not(type(settings["resolutionSetting"])==int and 0<=settings["resolutionSetting"]<=4):
    settings["resolutionSetting"]=0
if type(settings["samePieces"])!=bool:
    settings["samePieces"]=False
resolution:tuple[int,int]=Resolutions[settings["resolutionSetting"]]
try:
    with open("leaderboard"+str(VersionID)+".json","x")as x:
        pass
except OSError:
    pass
leaderboardFile=open("leaderboard"+str(VersionID)+".json","r+")
try:
    leaderboard:list[dict]=json.load(leaderboardFile)
except json.JSONDecodeError:
    leaderboard:list[dict]=[]
if type(leaderboard)!=list:
    leaderboard=[]
for gameID in range(len(leaderboard)):
    if type(leaderboard[gameID])!=dict or not{"mode","name","settings","score"}.issubset(set(leaderboard[gameID].keys()))or type(leaderboard[gameID]["mode"])!=int or leaderboard[gameID]["mode"]not in SingleplayerModes or(leaderboard[gameID]["mode"]in{3,4,6}and("lines"not in leaderboard[gameID].keys()or type(leaderboard[gameID]["lines"])!=int or leaderboard[gameID]["lines"]<0))or type(leaderboard[gameID]["name"])!=str or len(leaderboard[gameID]["name"])!=6 or type(leaderboard[gameID]["score"])!=int or leaderboard[gameID]["score"]<0 or type(leaderboard[gameID]["settings"])!=dict or not{"dasInit","dasSpeed","maxLvl","minLvl"}.issubset(leaderboard[gameID]["settings"].keys())or type(leaderboard[gameID]["settings"]["dasInit"])!=int or leaderboard[gameID]["settings"]["dasInit"]<1 or type(leaderboard[gameID]["settings"]["dasSpeed"])!=int or leaderboard[gameID]["settings"]["dasSpeed"]<1 or type(leaderboard[gameID]["settings"]["maxLvl"])!=int or type(leaderboard[gameID]["settings"]["minLvl"])!=int or 0>=leaderboard[gameID]["settings"]["minLvl"]>=leaderboard[gameID]["settings"]["maxLvl"]>=35 or("time"in leaderboard[gameID].keys()and leaderboard[gameID]["time"]<0):
        del leaderboard[gameID]
    for key in leaderboard[gameID].keys():
        if key not in{"lines","mode","name","score","settings","time"}:
            del leaderboard[gameID][key]
    if leaderboard[gameID]["mode"]in{1,2}and"lines"in leaderboard[gameID].keys():
        del leaderboard[gameID]["lines"]
    if leaderboard[gameID]["mode"]in{3,4,6}and"time"in leaderboard[gameID].keys():
        del leaderboard[gameID]["time"]
    for key in leaderboard[gameID]["settings"].keys():
        if key not in{"dasInit","dasSpeed","maxLvl","minLvl"}:
            del leaderboard[gameID]["settings"][key]
currentLeaderboardLength:int=0
for game in leaderboard:
    if game["mode"]==0:
        currentLeaderboardLength+=1
smallMode:bool=False
pygame.init()
pygame.mouse.set_visible(False)
pygame.display.set_icon(pygame.image.load(pathlib.PurePath("assets","icon.png")))
updateAssets()
pygame.display.set_caption("Master Stacker")
mode:int=-3
name:str="      "
time:int=0
gameWin=False
combo=0
currentBackground:pygame.Surface=asset(pathlib.PurePath("bg","menu","title"))
gamePaused:bool=False
menuPage:int=1
leaderboardScrollPosition:int=0
vsPlayerCount:int=2
nameEntryPos:int=0
handlePlayer:int=0
playerBoardMasks:tuple[tuple[pygame.Rect]]=((pygame.Rect(48*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,43*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(48*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(48*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(48*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(176*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)),(pygame.Rect(8*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,3*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(8*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(112*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor),pygame.Rect(216*scaleFactor,95*scaleFactor,96*scaleFactor,82*scaleFactor)))
garbage:list[int]=[]
remainingAttack:int=0
framesElapsed:int=0
leftMem=False
rightMem=False
downMem=False
upMem=False
rotLMem=False
rotRMem=False
holdMem=False
pauseMem=False
dasTimer=0
try:
    while True:
        if pygame.QUIT in[event.type for event in pygame.event.get()]:
            raise KeyboardInterrupt
        keyboardInputs=pygame.key.get_pressed()
        if mode in MultiplayerModes:
            leftPressed=[keyboardInputs[x]for x in[pygame.K_a,pygame.K_j,pygame.K_DELETE,pygame.K_KP4,pygame.K_v,pygame.K_LEFT]]
            rightPressed=[keyboardInputs[x]for x in[pygame.K_d,pygame.K_l,pygame.K_PAGEDOWN,pygame.K_KP6,pygame.K_n,pygame.K_RIGHT]]
            downPressed=[keyboardInputs[x]for x in[pygame.K_s,pygame.K_k,pygame.K_END,pygame.K_KP5,pygame.K_b,pygame.K_DOWN]]
            upPressed=[keyboardInputs[x]for x in[pygame.K_w,pygame.K_i,pygame.K_HOME,pygame.K_KP8,pygame.K_g,pygame.K_UP]]
            rotLPressed=[keyboardInputs[x]for x in[pygame.K_q,pygame.K_u,pygame.K_INSERT,pygame.K_KP7,pygame.K_f,pygame.K_KP1]]
            rotRPressed=[keyboardInputs[x]for x in[pygame.K_e,pygame.K_o,pygame.K_PAGEUP,pygame.K_KP9,pygame.K_h,pygame.K_KP2]]
            holdPressed=[keyboardInputs[x]for x in[pygame.K_r,pygame.K_p,pygame.K_BREAK,pygame.K_KP_PLUS,pygame.K_y,pygame.K_KP0]]
            if vsPlayerCount>=3 and keyboardInputs[pygame.K_PAUSE]:
                holdPressed[2]=True
            pausePressed=keyboardInputs[pygame.K_SPACE]
            if time==-1:
                currentBackground=asset(pathlib.PurePath("bg","vs",str(vsPlayerCount)+"p"))
                gameBoard=[deepcopy(BlankBoard) for i in range(vsPlayerCount)]
                nextPieces=[[]for i in range(vsPlayerCount)]
                pieceID=[None,]*vsPlayerCount
                if settings["samePieces"]:
                    if mode==7 and settings["newBags"]:
                        smallBag=set(SmallBagFull)
                        mediumBag=set(MediumBagFull)
                        bigBag=set(BigBagFull)
                        x=[]
                        for i in range(4):
                            if i<2:
                                x.append(smallBag.pop())
                            x.append(mediumBag.pop())
                            x.append(bigBag.pop())
                    else:
                        x=random.sample(SmallBagFull,2)+random.sample(MediumBagFull,4)+random.sample(BigBagFull,4)if mode==7 else list(MediumBagFull)
                    random.shuffle(x)
                elif mode==7 and settings["newBags"]:
                    smallBag=[set(),]*vsPlayerCount
                    mediumBag=[set(),]*vsPlayerCount
                    bigBag=[set(),]*vsPlayerCount
                for i in range(vsPlayerCount):
                    if mode==7 and not settings["samePieces"]and settings["newBags"]:
                        smallBag[i]=set(SmallBagFull)
                        mediumBag[i]=set(MediumBagFull)
                        bigBag[i]=set(BigBagFull)
                        nextPieces[i]=[]
                        for j in range(4):
                            if j<2:
                                nextPieces[i].append(smallBag[i].pop())
                            nextPieces[i].append(mediumBag[i].pop())
                            nextPieces[i].append(bigBag[i].pop())
                    else:
                        nextPieces[i]=list(x)if settings["samePieces"]else random.sample(SmallBagFull,2)+random.sample(MediumBagFull,4)+random.sample(BigBagFull,4)if mode==7 else list(MediumBagFull)
                    if not settings["samePieces"]:
                        random.shuffle(nextPieces[i])
                    pieceID[i]=nextPieces[i][0]
                    del nextPieces[i][0]
                try:
                    del x
                except NameError:
                    pass
                pieceX=[2]*vsPlayerCount
                pieceY=[17]*vsPlayerCount
                pieceR=[0]*vsPlayerCount
                fallTime=[LevelSpeeds[0]]*vsPlayerCount
                lockTime=[60]*vsPlayerCount
                pieceLowestY=[17]*vsPlayerCount
                hold=[0]*vsPlayerCount
                toppedOut=[False]*vsPlayerCount
                time=0
                leftMem=[False]*vsPlayerCount
                rightMem=[False]*vsPlayerCount
                downMem=[False]*vsPlayerCount
                upMem=[False]*vsPlayerCount
                rotLMem=[False]*vsPlayerCount
                rotRMem=[False]*vsPlayerCount
                holdMem=[False]*vsPlayerCount
                holdUsed=[False]*vsPlayerCount
                dasTimer=[0]*vsPlayerCount
                combo=[0]*vsPlayerCount
                garbage=[0]*vsPlayerCount
            updateBackground()
            for currentPlayerHandle in range(vsPlayerCount):
                if toppedOut[currentPlayerHandle]:
                    win.fill(0,playerBoardMasks[vsPlayerCount-2][currentPlayerHandle])
                else:
                    if gamePaused:
                        if upPressed[currentPlayerHandle]and rotLPressed[currentPlayerHandle]:
                            toppedOut[currentPlayerHandle]=True
                    else:
                        if leftPressed[currentPlayerHandle]and not rightPressed[currentPlayerHandle]:
                            dasTimer[currentPlayerHandle]=min(dasTimer[currentPlayerHandle],0)
                            if dasTimer[currentPlayerHandle]>-2:
                                pieceX[currentPlayerHandle]-=1
                                if testPieceCollision(currentPlayerHandle):
                                    pieceX[currentPlayerHandle]+=1
                                else:
                                    dasTimer[currentPlayerHandle]=-(settings["dasInit"]if dasTimer[currentPlayerHandle]==0 else settings["dasSpeed"])
                            else:
                                dasTimer[currentPlayerHandle]+=1
                        if rightPressed[currentPlayerHandle]and not leftPressed[currentPlayerHandle]:
                            dasTimer[currentPlayerHandle]=max(dasTimer[currentPlayerHandle],0)
                            if dasTimer[currentPlayerHandle]<2:
                                pieceX[currentPlayerHandle]+=1
                                if testPieceCollision(currentPlayerHandle):
                                    pieceX[currentPlayerHandle]-=1
                                else:
                                    dasTimer[currentPlayerHandle]=settings["dasInit"]if dasTimer[currentPlayerHandle]==0 else settings["dasSpeed"]
                            else:
                                dasTimer[currentPlayerHandle]-=1
                        if not(leftPressed[currentPlayerHandle]or rightPressed[currentPlayerHandle]):
                            dasTimer[currentPlayerHandle]=0
                        if upPressed[currentPlayerHandle]:
                            if not upMem[currentPlayerHandle]:
                                lockTime[currentPlayerHandle]=1
                                pieceLowestY[currentPlayerHandle]=0
                                while not testPieceCollision(currentPlayerHandle):
                                    pieceY[currentPlayerHandle]+=1
                                pieceY[currentPlayerHandle]-=1
                                upMem[currentPlayerHandle]=True
                        else:
                            upMem[currentPlayerHandle]=False
                        if rotLPressed[currentPlayerHandle]:
                            if not rotLMem[currentPlayerHandle]:
                                pieceR[currentPlayerHandle]=(pieceR[currentPlayerHandle]-1)%len(PieceTilemaps[pieceID[currentPlayerHandle]])
                                if testPieceCollision(currentPlayerHandle):
                                    for i in range(8):
                                        pieceX[currentPlayerHandle]+=WallKickData[i][0]-WallKickData[i-1][0]
                                        pieceY[currentPlayerHandle]+=WallKickData[i][1]-WallKickData[i-1][1]
                                        if not testPieceCollision(currentPlayerHandle):
                                            break
                                    if testPieceCollision(currentPlayerHandle):
                                        pieceX[currentPlayerHandle]-=1
                                        pieceY[currentPlayerHandle]+=1
                                        pieceR[currentPlayerHandle]=(pieceR[currentPlayerHandle]+1)%len(PieceTilemaps[pieceID[currentPlayerHandle]])
                                rotLMem[currentPlayerHandle]=True
                        else:
                            rotLMem[currentPlayerHandle]=False
                        if rotRPressed[currentPlayerHandle]:
                            if not rotRMem[currentPlayerHandle]:
                                pieceR[currentPlayerHandle]=(pieceR[currentPlayerHandle]+1)%len(PieceTilemaps[pieceID[currentPlayerHandle]])
                                if testPieceCollision(currentPlayerHandle):
                                    for i in range(8):
                                        pieceX[currentPlayerHandle]-=WallKickData[i][0]-WallKickData[i-1][0]
                                        pieceY[currentPlayerHandle]+=WallKickData[i][1]-WallKickData[i-1][1]
                                        if not testPieceCollision(currentPlayerHandle):
                                            break
                                    if testPieceCollision(currentPlayerHandle):
                                        pieceX[currentPlayerHandle]+=1
                                        pieceY[currentPlayerHandle]+=1
                                        pieceR[currentPlayerHandle]=(pieceR[currentPlayerHandle]-1)%len(PieceTilemaps[pieceID[currentPlayerHandle]])
                                rotRMem[currentPlayerHandle]=True
                        else:
                            rotRMem[currentPlayerHandle]=False
                        if holdPressed[currentPlayerHandle]:
                            if not holdMem[currentPlayerHandle]:
                                if not holdUsed[currentPlayerHandle]:
                                    if hold[currentPlayerHandle]==0:
                                        hold[currentPlayerHandle]=nextPieces[currentPlayerHandle][0]
                                        del nextPieces[currentPlayerHandle][0]
                                    temp=pieceID[currentPlayerHandle]
                                    pieceID[currentPlayerHandle]=hold[currentPlayerHandle]
                                    hold[currentPlayerHandle]=temp
                                    del temp
                                    pieceX[currentPlayerHandle]=2
                                    pieceY[currentPlayerHandle]=17
                                    pieceR[currentPlayerHandle]=0
                                    fallTime[currentPlayerHandle]=LevelSpeeds[0]
                                    lockTime[currentPlayerHandle]=60
                                    pieceLowestY[currentPlayerHandle]=17
                                    holdUsed[currentPlayerHandle]=True
                                holdMem[currentPlayerHandle]=True
                        else:
                            holdMem[currentPlayerHandle]=False
                        pieceY[currentPlayerHandle]+=1
                        if testPieceCollision(currentPlayerHandle):
                            pieceY[currentPlayerHandle]-=1
                            lockTime[currentPlayerHandle]-=1
                            if lockTime[currentPlayerHandle]==0:
                                for x in range(5):
                                    for y in range(5):
                                        if PieceTilemaps[pieceID[currentPlayerHandle]][pieceR[currentPlayerHandle]][y][x]is not None:
                                            if gameBoard[currentPlayerHandle][pieceY[currentPlayerHandle]+y][pieceX[currentPlayerHandle]+x]is None:
                                                gameBoard[currentPlayerHandle][pieceY[currentPlayerHandle]+y][pieceX[currentPlayerHandle]+x]=PieceTilemaps[pieceID[currentPlayerHandle]][pieceR[currentPlayerHandle]][y][x]
                                            else:
                                                toppedOut[currentPlayerHandle]=True
                                linesCleared=0
                                for line in range(40):
                                    if None not in gameBoard[currentPlayerHandle][line]:
                                        linesCleared+=1
                                        for x in range(10):
                                            if gameBoard[currentPlayerHandle][line-1][x]is not None and gameBoard[currentPlayerHandle][line-1][x]!=-1:
                                                gameBoard[currentPlayerHandle][line-1][x]=gameBoard[currentPlayerHandle][line-1][x]&-3
                                            if gameBoard[currentPlayerHandle][line+1][x]is not None and gameBoard[currentPlayerHandle][line+1][x]!=-1:
                                                gameBoard[currentPlayerHandle][line+1][x]=gameBoard[currentPlayerHandle][line+1][x]&-2
                                        del gameBoard[currentPlayerHandle][line]
                                        gameBoard[currentPlayerHandle].insert(0,deepcopy(EmptyLine))
                                if linesCleared==0:
                                    combo[currentPlayerHandle]=0
                                    while garbage[currentPlayerHandle]>0:
                                        if gameBoard[currentPlayerHandle][0]==deepcopy(EmptyLine):
                                            gameBoard[currentPlayerHandle].insert(40,random.choice([[None,8,12,12,12,12,12,12,12,4,-1,-1,-1,-1,-1],[0,None,8,12,12,12,12,12,12,4,-1,-1,-1,-1,-1],[8,4,None,8,12,12,12,12,12,4,-1,-1,-1,-1,-1],[8,12,4,None,8,12,12,12,12,4,-1,-1,-1,-1,-1],[8,12,12,4,None,8,12,12,12,4,-1,-1,-1,-1,-1],[8,12,12,12,4,None,8,12,12,4,-1,-1,-1,-1,-1],[8,12,12,12,12,4,None,8,12,4,-1,-1,-1,-1,-1],[8,12,12,12,12,12,4,None,8,4,-1,-1,-1,-1,-1],[8,12,12,12,12,12,12,4,None,0,-1,-1,-1,-1,-1],[8,12,12,12,12,12,12,12,4,None,-1,-1,-1,-1,-1]]))
                                            del gameBoard[currentPlayerHandle][0]
                                        else:
                                            toppedOut[currentPlayerHandle]=True
                                        garbage[currentPlayerHandle]-=1
                                else:
                                    combo[currentPlayerHandle]+=1
                                    remainingAttack=LineGarbage[linesCleared]+(combo[currentPlayerHandle]-1)//2+(9 if mode==7 else 6)*(gameBoard[currentPlayerHandle]==BlankBoard)
                                    if garbage[currentPlayerHandle]>0 and settings["garbageBlocking"]:
                                        while garbage[currentPlayerHandle]>0 and remainingAttack>0:
                                            garbage[currentPlayerHandle]-=1
                                            remainingAttack-=1
                                    if settings["garbageType"]==0:
                                        for i in[x for x in range(vsPlayerCount)if x!=currentPlayerHandle and not toppedOut[x]]:
                                            garbage[i]+=remainingAttack
                                    elif settings["garbageType"]==1:
                                        garbage[random.choice([x for x in range(vsPlayerCount)if x!=currentPlayerHandle and not toppedOut[x]])]+=remainingAttack
                                pieceID[currentPlayerHandle]=nextPieces[currentPlayerHandle][0]
                                del nextPieces[currentPlayerHandle][0]
                                pieceX[currentPlayerHandle]=2
                                pieceY[currentPlayerHandle]=17
                                pieceR[currentPlayerHandle]=0
                                fallTime[currentPlayerHandle]=LevelSpeeds[0]
                                lockTime[currentPlayerHandle]=60
                                pieceLowestY[currentPlayerHandle]=17
                                holdUsed[currentPlayerHandle]=0
                        else:
                            pieceY[currentPlayerHandle]-=1
                            fallTime[currentPlayerHandle]-=1
                            if downPressed[currentPlayerHandle]:
                                fallTime[currentPlayerHandle]=min(fallTime[currentPlayerHandle],2)
                            if fallTime[currentPlayerHandle]<=0:
                                fallTime[currentPlayerHandle]+=LevelSpeeds[0]
                                pieceY[currentPlayerHandle]+=1
                                if pieceY[currentPlayerHandle]>pieceLowestY[currentPlayerHandle]:
                                    pieceLowestY[currentPlayerHandle]=pieceY[currentPlayerHandle]
                                    lockTime[currentPlayerHandle]=60
                        if len(nextPieces[currentPlayerHandle])<5:
                            if mode==7 and settings["newBags"]:
                                if settings["samePieces"]:
                                    temp=[]
                                    for i in range(4):
                                        if i<2:
                                            if len(smallBag)==0:
                                                smallBag=set(SmallBagFull)
                                            temp.append(smallBag.pop())
                                        if len(mediumBag)==0:
                                            mediumBag=set(MediumBagFull)
                                        while True:
                                            temp2=mediumBag.pop()
                                            if temp2 in temp:
                                                mediumBag.add(temp2)
                                            else:
                                                temp.append(temp2)
                                                break
                                        if len(bigBag)==0:
                                            bigBag=set(BigBagFull)
                                        while True:
                                            temp2=bigBag.pop()
                                            if temp2 in temp:
                                                bigBag.add(temp2)
                                            else:
                                                temp.append(temp2)
                                                break
                                    del temp2
                                else:
                                    temp=[]
                                    for i in range(4):
                                        if i<2:
                                            if len(smallBag[currentPlayerHandle])==0:
                                                smallBag[currentPlayerHandle]=set(SmallBagFull)
                                            temp.append(smallBag[currentPlayerHandle].pop())
                                        if len(mediumBag[currentPlayerHandle])==0:
                                            mediumBag[currentPlayerHandle]=set(MediumBagFull)
                                        while True:
                                            temp2=mediumBag[currentPlayerHandle].pop()
                                            if temp2 in temp:
                                                mediumBag[currentPlayerHandle].add(temp2)
                                            else:
                                                temp.append(temp2)
                                                break
                                        if len(bigBag[currentPlayerHandle])==0:
                                            bigBag[currentPlayerHandle]=set(BigBagFull)
                                        while True:
                                            temp2=bigBag[currentPlayerHandle].pop()
                                            if temp2 in temp:
                                                bigBag[currentPlayerHandle].add(temp2)
                                            else:
                                                temp.append(temp2)
                                                break
                            else:
                                temp=random.sample(SmallBagFull,2)+random.sample(MediumBagFull,4)+random.sample(BigBagFull,4)if mode==6 else list(MediumBagFull)
                            random.shuffle(temp)
                            if settings["samePieces"]:
                                for i in[x for x in range(vsPlayerCount)if not toppedOut[x]]:
                                    nextPieces[i]+=temp
                            else:
                                nextPieces[currentPlayerHandle]+=temp
                            del temp
                        drawPiece(*PlayerHoldPositions[vsPlayerCount-2][currentPlayerHandle],hold[currentPlayerHandle])
                        drawPiece(*PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle],nextPieces[currentPlayerHandle][0])
                        drawPiece(PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][0],PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][1]+32,nextPieces[currentPlayerHandle][1])
                        drawPiece(PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][0],PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][1]+64,nextPieces[currentPlayerHandle][2])
                        drawPiece(PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][0],PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][1]+96,nextPieces[currentPlayerHandle][3])
                        drawPiece(PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][0],PlayerNextPositions[vsPlayerCount-2][currentPlayerHandle][1]+128,nextPieces[currentPlayerHandle][4])
                        boardBlits=[]
                        for x in range(10):
                            for y in range(20,40):
                                if gameBoard[currentPlayerHandle][y][x]is not None:
                                    boardBlits.append((pieces,(PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][0]+x*8,PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][1]+y*8),(gameBoard[currentPlayerHandle][y][x]//16*8,gameBoard[currentPlayerHandle][y][x]%16*8,8,8)))
                        blits(boardBlits)
                        if settings["ghost"]:
                            prevY=pieceY[currentPlayerHandle]
                            pieceY[currentPlayerHandle]+=1
                            while not testPieceCollision(currentPlayerHandle):
                                pieceY[currentPlayerHandle]+=1
                            pieceY[currentPlayerHandle]-=1
                            drawPiece(PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][0]+8*pieceX[currentPlayerHandle],PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][1]+8*pieceY[currentPlayerHandle],pieceID[currentPlayerHandle],pieceR[currentPlayerHandle],True)
                            pieceY[currentPlayerHandle]=prevY
                        drawPiece(PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][0]+8*pieceX[currentPlayerHandle],PlayerBoardPositions[vsPlayerCount-2][currentPlayerHandle][1]+8*pieceY[currentPlayerHandle],pieceID[currentPlayerHandle],pieceR[currentPlayerHandle])
                        for i in range(15):
                            blits([(garbageMeter,(PlayerGarbageMeterPositions[vsPlayerCount-2][currentPlayerHandle][0],PlayerGarbageMeterPositions[vsPlayerCount-2][currentPlayerHandle][1]+8*i),((garbage[currentPlayerHandle]+i)//15*2,0,2,8))])
                if pausePressed:
                    if not pauseMem:
                        gamePaused=not gamePaused
                        pauseMem=True
                else:
                    pauseMem=False
            if toppedOut.count(False)<=1:
                if pausePressed:
                    menuPage=mode
                    gamePaused=False
                    smallMode=False
                    leftMem=False
                    rightMem=False
                    downMem=False
                    upMem=False
                    rotLMem=False
                    rotRMem=False
                    holdMem=False
                    pauseMem=True
                    currentBackground=asset(pathlib.PurePath("bg","menu",str(mode)))
                    mode=0
                    updateBackground()
                    updateAssets()
                else:
                    gamePaused=True
        else:
            leftPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["left"]]
            rightPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["right"]]
            downPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["down"]]
            upPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["up"]]
            rotLPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["rotL"]]
            rotRPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["rotR"]]
            holdPressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["hold"]]
            pausePressed=keyboardInputs[KeyboardLayouts[settings["controlSetting"]]["pause"]]
            if mode in SingleplayerModes:
                if time==-1:
                    currentBackground=asset(pathlib.PurePath("bg","polymino"if mode==6 else"game"))
                    gameBoard=deepcopy(BlankBoard)
                    if mode==6 and settings["newBags"]:
                        smallBag=set(SmallBagFull)
                        mediumBag=set(MediumBagFull)
                        bigBag=set(BigBagFull)
                        nextPieces=[]
                        for i in range(4):
                            if i<2:
                                nextPieces.append(smallBag.pop())
                            nextPieces.append(mediumBag.pop())
                            nextPieces.append(bigBag.pop())
                    else:
                        nextPieces=random.sample(SmallBagFull,2)+random.sample(MediumBagFull,4)+random.sample(BigBagFull,4)if mode==6 else list(MediumBagFull)
                    random.shuffle(nextPieces)
                    pieceID=nextPieces[0]
                    del nextPieces[0]
                    pieceX=2
                    pieceY=17
                    pieceR=0
                    lines=0
                    level=settings["minLvl"]
                    fallTime=LevelSpeeds[level]
                    lockTime=60
                    pieceLowestY=17
                    score=0
                    hold=0
                    holdUsed=False
                    dasTimer=0
                    leftMem=False
                    rightMem=False
                    downMem=False
                    upMem=False
                    rotLMem=False
                    rotRMem=False
                    holdMem=False
                    pauseMem=True
                    toppedOut=False
                    combo=0
                    if mode==4:
                        time=10801
                updateBackground()
                if not gamePaused:
                    time+=-1 if mode==4 else 1
                    if leftPressed and not rightPressed:
                        dasTimer=min(dasTimer,0)
                        if dasTimer>-2:
                            pieceX-=1
                            if testPieceCollision():
                                pieceX+=1
                            else:
                                dasTimer=-(settings["dasInit"]if dasTimer==0 else settings["dasSpeed"])
                        else:
                            dasTimer+=1
                    if rightPressed and not leftPressed:
                        dasTimer=max(dasTimer,0)
                        if dasTimer<2:
                            pieceX+=1
                            if testPieceCollision():
                                pieceX-=1
                            else:
                                dasTimer=settings["dasInit"]if dasTimer==0 else settings["dasSpeed"]
                        else:
                            dasTimer-=1
                    if leftPressed==rightPressed:
                        dasTimer=0
                    if upPressed:
                        if not upMem:
                            lockTime=1
                            pieceLowestY=0
                            if not testPieceCollision():
                                while not testPieceCollision():
                                    pieceY+=1
                                    score+=2
                                pieceY-=1
                                score-=2
                                upMem=True
                    else:
                        upMem=False
                    if rotLPressed:
                        if not rotLMem:
                            pieceR=(pieceR-1)%len(PieceTilemaps[pieceID])
                            if testPieceCollision():
                                for i in range(8):
                                    pieceX+=WallKickData[i][0]-WallKickData[i-1][0]
                                    pieceY+=WallKickData[i][1]-WallKickData[i-1][1]
                                    if not testPieceCollision():
                                        break
                                if testPieceCollision():
                                    pieceX-=1
                                    pieceY+=1
                                    pieceR=(pieceR+1)%len(PieceTilemaps[pieceID])
                            rotLMem=True
                    else:
                        rotLMem=False
                    if rotRPressed:
                        if not rotRMem:
                            pieceR=(pieceR+1)%len(PieceTilemaps[pieceID])
                            if testPieceCollision():
                                for i in range(8):
                                    pieceX-=WallKickData[i][0]-WallKickData[i-1][0]
                                    pieceY+=WallKickData[i][1]-WallKickData[i-1][1]
                                    if not testPieceCollision():
                                        break
                                if testPieceCollision():
                                    pieceX+=1
                                    pieceY+=1
                                    pieceR=(pieceR-1)%len(PieceTilemaps[pieceID])
                            rotRMem=True
                    else:
                        rotRMem=False
                    if holdPressed:
                        if not holdMem:
                            if not holdUsed:
                                if hold==0:
                                    hold=nextPieces[0]
                                    del nextPieces[0]
                                temp=pieceID
                                pieceID=hold
                                hold=temp
                                del temp
                                pieceX=2
                                pieceY=17
                                pieceR=0
                                fallTime=LevelSpeeds[level]
                                lockTime=60
                                pieceLowestY=17
                                holdUsed=True
                            holdMem=True
                    else:
                        holdMem=False
                    pieceY+=1
                    if testPieceCollision():
                        pieceY-=1
                        lockTime-=1
                        if lockTime==0:
                            for x in range(5):
                                for y in range(5):
                                    if PieceTilemaps[pieceID][pieceR][y][x]is not None:
                                        if gameBoard[pieceY+y][pieceX+x]is None:
                                            gameBoard[pieceY+y][pieceX+x]=PieceTilemaps[pieceID][pieceR][y][x]
                                        else:
                                            toppedOut=True
                            linesCleared=0
                            for line in range(40):
                                if None not in gameBoard[line]:
                                    lines+=1
                                    linesCleared+=1
                                    for x in range(10):
                                        if gameBoard[line-1][x]is not None and gameBoard[line-1][x]!=-1:
                                            gameBoard[line-1][x]=gameBoard[line-1][x]&-3
                                        if gameBoard[line+1][x]is not None and gameBoard[line+1][x]!=-1:
                                            gameBoard[line+1][x]=gameBoard[line+1][x]&-2
                                    del gameBoard[line]
                                    gameBoard.insert(0,deepcopy(EmptyLine))
                            if linesCleared==0:
                                combo=0
                            else:
                                combo+=1
                                score+=int(LineScores[linesCleared]*(0.95+0.05*combo)*LevelScoreMultipliers[level])
                                if gameBoard==BlankBoard:
                                    score+=int(45000*(0.95+0.05*combo)*LevelScoreMultipliers[level])
                                if settings["maxLvl"]>lines//10>level:
                                    level+=1
                            pieceID=nextPieces[0]
                            del nextPieces[0]
                            pieceX=2
                            pieceY=17
                            pieceR=0
                            fallTime=LevelSpeeds[level]
                            lockTime=60
                            pieceLowestY=17
                            holdUsed=0
                    else:
                        pieceY-=1
                        fallTime-=1
                        if downPressed:
                            fallTime=min(fallTime,2)
                        while fallTime<=0:
                            fallTime+=LevelSpeeds[level]
                            pieceY+=1
                            if pieceY>pieceLowestY:
                                pieceLowestY=pieceY
                                lockTime=60
                            if downPressed or level>16:
                                score+=1
                            if testPieceCollision():
                                fallTime-=LevelSpeeds[level]
                                pieceY-=1
                                if downPressed or level>16:
                                    score-=1
                                break
                    if len(nextPieces)<5:
                        if mode==6 and settings["newBags"]:
                            temp=[]
                            for i in range(4):
                                if i<2:
                                    if len(smallBag)==0:
                                        smallBag=set(SmallBagFull)
                                    temp.append(smallBag.pop())
                                if len(mediumBag)==0:
                                    mediumBag=set(MediumBagFull)
                                while True:
                                    temp2=mediumBag.pop()
                                    if temp2 in temp:
                                        mediumBag.add(temp2)
                                    else:
                                        temp.append(temp2)
                                        break
                                if len(bigBag)==0:
                                    bigBag=set(BigBagFull)
                                while True:
                                    temp2=bigBag.pop()
                                    if temp2 in temp:
                                        bigBag.add(temp2)
                                    else:
                                        temp.append(temp2)
                                        break
                            del temp2
                        else:
                            temp=random.sample(SmallBagFull,2)+random.sample(MediumBagFull,4)+random.sample(BigBagFull,4)if mode==6 else list(MediumBagFull)
                        random.shuffle(temp)
                        nextPieces+=temp
                        del temp
                    drawPiece(72,16,hold)
                    drawPiece(200+8*(mode==6),16,nextPieces[0])
                    drawPiece(200+8*(mode==6),48,nextPieces[1])
                    drawPiece(200+8*(mode==6),80,nextPieces[2])
                    drawPiece(200+8*(mode==6),112,nextPieces[3])
                    drawPiece(200+8*(mode==6),144,nextPieces[4])
                    boardBlits=[]
                    for x in range(10):
                        for y in range(20,40):
                            if gameBoard[y][x]is not None:
                                boardBlits.append((pieces,(120+x*8,-152+y*8),(gameBoard[y][x]//16*8,gameBoard[y][x]%16*8,8,8)))
                    blits(boardBlits)
                    if settings["ghost"]:
                        prevY=pieceY
                        pieceY+=1
                        while not testPieceCollision():
                            pieceY+=1
                        pieceY-=1
                        drawPiece(120+8*pieceX,-152+8*pieceY,pieceID,pieceR,True)
                        pieceY=prevY
                    drawPiece(120+8*pieceX,-152+8*pieceY,pieceID,pieceR)
                elif upPressed and rotLPressed:
                    toppedOut=True
                    upMem=True
                    rotLMem=True
                if pausePressed:
                    if not pauseMem:
                        gamePaused=not gamePaused
                        pauseMem=True
                else:
                    pauseMem=False
                drawText("{:02}".format(level),(88,80))
                drawText((" {:03}".format(lines)if lines<1000 else(str(lines)if lines<100000 else("#"+str(lines%10000)if lines<110000 else("##"+str(lines%1000)if lines<111000 else("###"+str(lines%100)if lines<111100 else("####"+str(lines%10)if lines<111110 else"#####")))))),(72,56),{'#':0})
                drawText(("{:07}".format(score)if score<10000000 else("#{:06}".format(score%1000000)if score<11000000 else("##{:05}".format(score%100000)if score<11100000 else("###{:04}".format(score%10000)if score<11110000 else("####{:03}".format(score%1000)if score<11111000 else("#####{:02}".format(score%100)if score<11111100 else("######{}".format(score%10)if score<11111110 else"#######"))))))),(57,104),{'#':0})
                drawText(name,(64,152))
                drawText("{:02}'{:02}\"{:02}".format(time//3600,time//60%60,time%60)if time<359999 else"99'59\"59",(48,128))
                if mode==4 and time==0 or mode==1 and lines>=200 or mode==2 and lines>=50:
                    toppedOut=True
                    gameWin=True
                if toppedOut:
                    leaderboard.append({"mode":mode,"name":name,"settings":{"dasInit":settings["dasInit"],"dasSpeed":settings["dasSpeed"],"maxLvl":settings["maxLvl"],"minLvl":settings["minLvl"]},"score":score}|({"lines":lines}if mode in{3,4,6}else({"time":time}if gameWin else{})))
                    currentLeaderboardLength+=1
                    currentBackground=asset(pathlib.PurePath("bg","menu",str(menuPage)))
                    mode=0
                    updateBackground()
                    gamePaused=False
            elif mode==0:
                if leftPressed:
                    if not leftMem:
                        if menuPage!=-2:
                            menuPage-=1
                            leaderboardScrollPosition=0
                        if menuPage in SingleplayerModes:
                            currentLeaderboardLength=0
                            for game in leaderboard:
                                if game["mode"]==menuPage:
                                    currentLeaderboardLength+=1
                        currentBackground=asset(pathlib.PurePath("bg","menu",str(menuPage)))
                        leftMem=True
                else:
                    leftMem=False
                if rightPressed:
                    if not rightMem:
                        if menuPage!=7:
                            menuPage+=1
                            leaderboardScrollPosition=0
                        if menuPage in SingleplayerModes:
                            currentLeaderboardLength=0
                            for game in leaderboard:
                                if game["mode"]==menuPage:
                                    currentLeaderboardLength+=1
                        currentBackground=asset(pathlib.PurePath("bg","menu",str(menuPage)))
                        rightMem=True
                else:
                    rightMem=False
                updateBackground()
                if downPressed:
                    if not downMem:
                        if menuPage==0:
                            settings["controlSetting"]=(settings["controlSetting"]+1)%6
                        if menuPage in SingleplayerModes and leaderboardScrollPosition<(currentLeaderboardLength-1)//5:
                                leaderboardScrollPosition+=1
                        elif menuPage in MultiplayerModes and vsPlayerCount<6:
                            vsPlayerCount+=1
                        downMem=True
                else:
                    downMem=False
                if upPressed:
                    if not upMem:
                        if menuPage==0:
                            settings["controlSetting"]=(settings["controlSetting"]-1)%6
                        elif menuPage in SingleplayerModes and leaderboardScrollPosition>0:
                            leaderboardScrollPosition-=1
                        elif menuPage in MultiplayerModes and vsPlayerCount>2:
                            vsPlayerCount-=1
                        upMem=True
                else:
                    upMem=False
                if rotLPressed:
                    if not rotLMem:
                        menuPage=1
                        mode=-3
                        currentBackground=asset(pathlib.PurePath("bg","menu","title"))
                        rotLMem=True
                else:
                    rotLMem=False
                if pausePressed:
                    if not pauseMem:
                        if menuPage in SingleplayerModes:
                            leaderboardScrollPosition=0
                            mode=-2
                            time=-1
                        elif menuPage in{-1,5,7}:
                            leaderboardScrollPosition=0
                            mode=menuPage
                            time=-1
                            if menuPage in MultiplayerModes:
                                smallMode=True
                                updateAssets()
                        elif menuPage==-2:
                            raise KeyboardInterrupt
                        pauseMem=True
                else:
                    pauseMem=False
                if menuPage in{1,2}:
                    formattedLeaderboardScoreData=[]
                    formattedLeaderboardTimeData=[]
                    for game in leaderboard:
                        if game["mode"]==menuPage:
                            formattedLeaderboardScoreData.append([game["name"],game["score"],game["settings"]=={"dasInit":settings["dasInit"],"dasSpeed":settings["dasSpeed"],"maxLvl":settings["maxLvl"],"minLvl":settings["minLvl"]}])
                            if"time"in game.keys():
                                formattedLeaderboardTimeData.append([game["name"],game["time"],game["settings"]=={"dasInit":settings["dasInit"],"dasSpeed":settings["dasSpeed"],"maxLvl":settings["maxLvl"],"minLvl":settings["minLvl"]}])
                    formattedLeaderboardScoreData.sort(reverse=True,key=lambda x:x[1])
                    formattedLeaderboardTimeData.sort(key=lambda x:x[1])
                    for i in range(5*leaderboardScrollPosition,5*leaderboardScrollPosition+5):
                        if len(formattedLeaderboardScoreData)>i:
                            drawText(formattedLeaderboardScoreData[i][0]+(" "if formattedLeaderboardScoreData[i][2]else"!")+("{:07}".format(formattedLeaderboardScoreData[i][1])if formattedLeaderboardScoreData[i][1]<10000000 else("#{:06}".format(formattedLeaderboardScoreData[i][1]%1000000)if formattedLeaderboardScoreData[i][1]<11000000 else("##{:05}".format(formattedLeaderboardScoreData[i][1]%100000)if formattedLeaderboardScoreData[i][1]<11100000 else("###{:04}".format(formattedLeaderboardScoreData[i][1]%10000)if formattedLeaderboardScoreData[i][1]<11110000 else("####{:03}".format(formattedLeaderboardScoreData[i][1]%1000)if formattedLeaderboardScoreData[i][1]<11111000 else("#####{:02}".format(formattedLeaderboardScoreData[i][1]%100)if formattedLeaderboardScoreData[i][1]<11111100 else("######{}".format(formattedLeaderboardScoreData[i][1]%10)if formattedLeaderboardScoreData[i][1]<11111110 else"#######"))))))),(40,128+8*(i-5*leaderboardScrollPosition)),('#',0))
                            if len(formattedLeaderboardTimeData)>i:
                                drawText(formattedLeaderboardTimeData[i][0]+(" "if formattedLeaderboardTimeData[i][2]else"!")+("{:02}'{:02}\"{:02}".format(formattedLeaderboardTimeData[i][1]//3600,formattedLeaderboardTimeData[i][1]//60%60,formattedLeaderboardTimeData[i][1]%60)if formattedLeaderboardTimeData[i][1]<359999 else"99'59\"59"),(168,128+8*(i-5*leaderboardScrollPosition)))
                        else:
                            break
                elif menuPage in{3,4,6}:
                    formattedLeaderboardScoreData=[]
                    formattedLeaderboardLinesData=[]
                    for game in leaderboard:
                        if game["mode"]==menuPage:
                            formattedLeaderboardScoreData.append([game["name"],game["score"],game["settings"]=={"dasInit":settings["dasInit"],"dasSpeed":settings["dasSpeed"],"maxLvl":settings["maxLvl"],"minLvl":settings["minLvl"]}])
                            formattedLeaderboardLinesData.append([game["name"],game["lines"],game["settings"]=={"dasInit":settings["dasInit"],"dasSpeed":settings["dasSpeed"],"maxLvl":settings["maxLvl"],"minLvl":settings["minLvl"]}])
                    formattedLeaderboardScoreData.sort(reverse=True,key=lambda x:x[1])
                    formattedLeaderboardLinesData.sort(reverse=True,key=lambda x:x[1])
                    for i in range(5*leaderboardScrollPosition,5*leaderboardScrollPosition+5):
                        if len(formattedLeaderboardScoreData)>i:
                            drawText(formattedLeaderboardScoreData[i][0]+(" "if formattedLeaderboardScoreData[i][2]else"!")+("{:07}".format(formattedLeaderboardScoreData[i][1])if formattedLeaderboardScoreData[i][1]<10000000 else("#{:06}".format(formattedLeaderboardScoreData[i][1]%1000000)if formattedLeaderboardScoreData[i][1]<11000000 else("##{:05}".format(formattedLeaderboardScoreData[i][1]%100000)if formattedLeaderboardScoreData[i][1]<11100000 else("###{:04}".format(formattedLeaderboardScoreData[i][1]%10000)if formattedLeaderboardScoreData[i][1]<11110000 else("####{:03}".format(formattedLeaderboardScoreData[i][1]%1000)if formattedLeaderboardScoreData[i][1]<11111000 else("#####{:02}".format(formattedLeaderboardScoreData[i][1]%100)if formattedLeaderboardScoreData[i][1]<11111100 else("######{}".format(formattedLeaderboardScoreData[i][1]%10)if formattedLeaderboardScoreData[i][1]<11111110 else"#######"))))))),(40,128+8*(i-5*leaderboardScrollPosition)),('#',0))
                            drawText(formattedLeaderboardLinesData[i][0]+(" "if formattedLeaderboardLinesData[i][2]else"!")+"{:05}".format(formattedLeaderboardLinesData[i][1])if formattedLeaderboardLinesData[i][1]<100000 else("#"+str(formattedLeaderboardLinesData[i][1]%10000)if formattedLeaderboardLinesData[i][1]<110000 else("##"+str(formattedLeaderboardLinesData[i][1]%1000)if formattedLeaderboardLinesData[i][1]<111000 else("###"+str(formattedLeaderboardLinesData[i][1]%100)if formattedLeaderboardLinesData[i][1]<111100 else("####"+str(formattedLeaderboardLinesData[i][1]%10)if formattedLeaderboardLinesData[i][1]<111110 else"#####")))),(168,128+8*(i-5*leaderboardScrollPosition)),{'#':0})
                        else:
                            break
                elif menuPage==0:
                    drawText(str(settings["controlSetting"]),(136,80))
                    blits([(asset(pathlib.PurePath("Control Type Diagrams",str(settings["controlSetting"]))),(80,112),(0,0,176,64))])
                elif menuPage in{7,5}:
                    drawText(str(vsPlayerCount),(128,136))
                    if vsPlayerCount>2:
                        blits([(specialChars,(128,128),(24,0,8,8)),])
                    if vsPlayerCount<6:
                        blits([(specialChars,(128,144),(32,0,8,8)),])
            elif mode==-1:
                if time==-1:
                    menuPage=0
                    time=0
                    win.fill(0)
                if leftPressed and not rightPressed:
                    leftMem=True
                    dasTimer=min(dasTimer,0)
                    if dasTimer>-2:
                        if menuPage==0 and settings["minLvl"]!=0:
                            settings["minLvl"]-=1
                        elif menuPage==1 and settings["maxLvl"]!=settings["minLvl"]:
                            settings["maxLvl"]-=1
                        elif menuPage==2 and not settings["ghost"]:
                            settings["ghost"]=True
                        elif menuPage==3 and settings["dasInit"]!=1:
                            settings["dasInit"]-=1
                        elif menuPage==4 and settings["dasSpeed"]!=1:
                            settings["dasSpeed"]-=1
                        elif menuPage==5 and settings["resolutionSetting"]!=0:
                            settings["resolutionSetting"]-=1
                            resolution=Resolutions[settings["resolutionSetting"]]
                            updateAssets()
                        elif menuPage==6 and not settings["fullscreen"]:
                            settings["fullscreen"]=True
                            updateAssets()
                        elif menuPage==7 and settings["garbageType"]!=0:
                            settings["garbageType"]-=1
                        elif menuPage==8 and not settings["garbageBlocking"]:
                            settings["garbageBlocking"]=True
                        elif menuPage==9 and not settings["samePieces"]:
                            settings["samePieces"]=True
                        elif menuPage==10 and not settings["newBags"]:
                            settings["newBags"]=True
                        dasTimer=-(settings["dasInit"]if dasTimer==0 else settings["dasSpeed"])
                    else:
                        dasTimer+=1
                else:
                    leftMem=False
                if rightPressed and not leftPressed:
                    rightMem=True
                    dasTimer=max(dasTimer,0)
                    if dasTimer<2:
                        if menuPage==0 and settings["minLvl"]!=settings["maxLvl"]:
                            settings["minLvl"]+=1
                        elif menuPage==1 and settings["maxLvl"]!=35:
                            settings["maxLvl"]+=1
                        elif menuPage==2 and settings["ghost"]:
                            settings["ghost"]=False
                        elif menuPage==3:
                            settings["dasInit"]+=1
                        elif menuPage==4:
                            settings["dasSpeed"]+=1
                        elif menuPage==5 and settings["resolutionSetting"]!=4:
                            settings["resolutionSetting"]+=1
                            resolution=Resolutions[settings["resolutionSetting"]]
                            updateAssets()
                        elif menuPage==6 and settings["fullscreen"]:
                            settings["fullscreen"]=False
                            updateAssets()
                        elif menuPage==7 and settings["garbageType"]!=2:
                            settings["garbageType"]+=1
                        elif menuPage==8 and settings["garbageBlocking"]:
                            settings["garbageBlocking"]=False
                        elif menuPage==9 and settings["samePieces"]:
                            settings["samePieces"]=False
                        elif menuPage==10 and settings["newBags"]:
                            settings["newBags"]=False
                        dasTimer=settings["dasInit"]if dasTimer==0 else settings["dasSpeed"]
                    else:
                        dasTimer-=1
                else:
                    rightMem=False
                if leftPressed==rightPressed:
                    dasTimer=0
                if downPressed:
                    if not downMem:
                        if menuPage==7 and settings["garbageType"]==2:
                            menuPage=9
                        elif menuPage!=11:
                            menuPage+=1
                        downMem=True
                else:
                    downMem=False
                if upPressed:
                    if not upMem:
                        if menuPage==9 and settings["garbageType"]==2:
                            menuPage=7
                        elif menuPage!=0:
                            menuPage-=1
                        upMem=True
                else:
                    upMem=False
                if rotLPressed:
                    if not rotLMem:
                        menuPage=-1
                        mode=0
                        currentBackground=asset(pathlib.PurePath("bg","menu","-1"))
                        updateBackground()
                        rotLMem=True
                else:
                    rotLMem=False
                if pausePressed:
                    if not pauseMem:
                        if menuPage==11:
                            menuPage=-1
                            mode=0
                            currentBackground=asset(pathlib.PurePath("bg","menu","-1"))
                            updateBackground()
                        pauseMem=True
                else:
                    pauseMem=False
                drawText("(1P) Starting Level:"+("<"if menuPage==0 and settings["minLvl"]!=0 else" ")+"{:02}".format(settings["minLvl"])+(">"if menuPage==0 and settings["minLvl"]!=settings["maxLvl"]else""),(0,0),{"<":1,">":2})
                drawText("(1P) Maximum Level:"+("<"if menuPage==1 and settings["maxLvl"]!=settings["minLvl"]else" ")+"{:02}".format(settings["maxLvl"])+(">"if menuPage==1 and settings["maxLvl"]!=35 else""),(0,8),{"<":1,">":2})
                drawText("Ghost:"+("<"if menuPage==2 and not settings["ghost"]else" ")+("On"if settings["ghost"]else"Off")+(">"if menuPage==2 and settings["ghost"]else""),(0,16),{"<":1,">":2})
                drawText("Initial DAS Delay:"+("<"if menuPage==3 and settings["dasInit"]!=1 else" ")+str(settings["dasInit"])+(">"if menuPage==3 else""),(0,24),{"<":1,">":2})
                drawText("DAS Speed:"+("<"if menuPage==4 and settings["dasSpeed"]!=1 else" ")+str(settings["dasSpeed"])+(">"if menuPage==4 else""),(0,32),{"<":1,">":2})
                drawText("Resolution:"+("<"if menuPage==5 and settings["resolutionSetting"]!=(640,360)else" ")+["640\xD7360 (SD)","1280\xD7720 (HD)","1920\xD71080 (FHD)","2560\xD71440 (QHD)","3840\xD72160 (4K/UHD)"][settings["resolutionSetting"]]+(">"if menuPage==5 and settings["resolutionSetting"]!=4 else""),(0,40),{"<":1,">":2})
                drawText("Fullscreen:"+("<"if menuPage==6 and not settings["fullscreen"]else" ")+("On"if settings["fullscreen"]else"Off")+(">"if menuPage==6 and settings["fullscreen"]else""),(0,48),{"<":1,">":2})
                drawText("(VS) Garbage Attacks:"+("<"if menuPage==7 and settings["garbageType"]>0 else" ")+["All","Random","None"][settings["garbageType"]]+(">"if menuPage==7 and settings["garbageType"]!=2 else""),(0,56),{"<":1,">":2})
                if settings["garbageType"]!=2:
                    drawText("(VS) Garbage Countering:"+("<"if menuPage==8 and not settings["garbageBlocking"]else" ")+("On"if settings["garbageBlocking"]else"Off")+(">"if menuPage==8 and settings["garbageBlocking"]else""),(0,64),{"<":1,">":2})
                drawText("(VS) All Players Get Same Pieces:"+("<"if menuPage==9 and not settings["samePieces"]else" ")+("On"if settings["samePieces"]else"Off")+(">"if menuPage==9 and settings["samePieces"]else""),(0,72),{"<":1,">":2})
                drawText("(Polymino) New Bag System:"+("<"if menuPage==10 and not settings["newBags"]else" ")+("On"if settings["newBags"]else"Off")+(">"if menuPage==10 and settings["newBags"]else""),(0,80),{"<":1,">":2})
                drawText("Back"+("<"if menuPage==11 else""),(0,88),{"<":1})
            elif mode==-2:
                if leftPressed:
                    if not leftMem:
                        if nameEntryPos>0:
                            nameEntryPos-=1
                        leftMem=True
                else:
                    leftMem=False
                if rightPressed:
                    if not rightMem:
                        if nameEntryPos<5:
                            nameEntryPos+=1
                        rightMem=True
                else:
                    rightMem=False
                if upPressed and not downPressed:
                    dasTimer=min(dasTimer,0)
                    if dasTimer>-2:
                        name=list(name)
                        if name[nameEntryPos]in{' ','\xA1','\xAE'}:
                            name[nameEntryPos]={' ':'\xFF','\xA1':'~','\xAE':'\xAC'}[name[nameEntryPos]]
                        else:
                            name[nameEntryPos]=chr(ord(name[nameEntryPos])-1)
                        name="".join(name)
                        dasTime=-(settings["dasInit"]if dasTimer==0 else settings["dasSpeed"])
                    else:
                        dasTimer+=1
                if downPressed and not upPressed:
                    dasTimer=max(dasTimer,0)
                    if dasTimer<2:
                        name=list(name)
                        if name[nameEntryPos]in{'\xFF','~','\xAC'}:
                            name[nameEntryPos]={'\xFF':' ','~':'\xA1','\xAC':'\xAE'}[name[nameEntryPos]]
                        else:
                            name[nameEntryPos]=chr(ord(name[nameEntryPos])+1)
                        name="".join(name)
                        dasTimer=settings["dasInit"]if dasTimer==0 else settings["dasSpeed"]
                    else:
                        dasTimer-=1
                if upPressed==downPressed:
                    dasTimer=0
                if rotLPressed:
                    if not rotLMem:
                        mode=0
                        currentBackground=asset(pathlib.PurePath("bg","menu",str(menuPage)))
                        rotLMem=True
                else:
                    rotLMem=False
                if pausePressed:
                    if not pauseMem:
                        mode=menuPage
                        pauseMem=True
                else:
                    pauseMem=False
                drawText(name,(128,96))
                blits([(specialChars,(128+8*nameEntryPos,88),(24,0,8,8)),])
                blits([(specialChars,(128+8*nameEntryPos,104),(32,0,8,8)),])
            elif mode==-3:
                updateBackground()
                if rotLPressed:
                    if not rotLMem:
                        raise KeyboardInterrupt
                else:
                    rotLMem=False
                if pausePressed:
                    if not pauseMem:
                        mode=0
                        currentBackground=asset(pathlib.PurePath("bg","menu","1"))
                        pauseMem=True
                else:
                    pauseMem=False
        while pygame.time.get_ticks()<(framesElapsed+1)*FrameDuration:
            pass
        framesElapsed=round(pygame.time.get_ticks()/FrameDuration)
        pygame.display.update()
        win.fill(0)
except KeyboardInterrupt:
    pass
finally:
    leaderboardFile.seek(0)
    leaderboardFile.truncate()
    json.dump(leaderboard,leaderboardFile,separators=(",",":"),sort_keys=True)
    leaderboardFile.close()
    settingsFile.seek(0)
    settingsFile.truncate()
    json.dump(settings,settingsFile,separators=(",",":"),sort_keys=True)
    settingsFile.close()
    pygame.display.quit()
    pygame.quit()