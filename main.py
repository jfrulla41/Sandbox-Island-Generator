import sys, pygame, time,random,Map

#start pygame
pygame.init()

#define size of window (also the size of the map)
size = width, height = 1024, 1024
#tiles are 1px by 1px
tilesize=1

#map size is windowsize divided by the tilesize
rows=int(width/tilesize)
cols=int(height/tilesize)

#random seed 
seed=random.random()*1000000


print("seed: %15.30f" % seed)


#create map object
mainMap=Map.Map(rows,cols)

#set the perlin values
mainMap.setPerlinVariables(0.002,8,0.6,seed)

#create the map
tilemap=mainMap.createMap()
    

#define biome colors
black = 0,0,0
ocean = 25,25,125
lake = 50,50,150
river = 25,0,100
beach = 150,150,50 
desert = 175,125,50
scorched = 100,100,100
grassland = 125,175,125
bare = 150,150,150
seasonal_forest = 125,150,125
shrubland = 100,175,75
tundra = 150,150,175
snow = 200,200,200
taiga = 175,200,125
temperate_forest = 75,125,75
temperate_rainforest = 35,100,35
tropical_rainforest = 0,75,0


#start with a black screen
screen = pygame.display.set_mode(size)
screen.fill(black)


#fill the screen with colored tiles
for i in range(rows):
    for j in range(cols):


        #the color depends on biome and water type
        if tilemap[i][j].subtype=="ocean":
            color=ocean
        elif tilemap[i][j].subtype=="lake":
            color=lake
        elif tilemap[i][j].subtype=="river":
            color=river
        elif tilemap[i][j].biome=="beach":
            color=beach
        elif tilemap[i][j].biome=="desert":
            color=desert
        elif tilemap[i][j].biome=="scorched":
            color=scorched
        elif tilemap[i][j].biome=="grassland":
            color=grassland
        elif tilemap[i][j].biome=="bare":
            color=bare
        elif tilemap[i][j].biome=="seasonal_forest":
            color=seasonal_forest
        elif tilemap[i][j].biome=="shrubland":
            color=shrubland
        elif tilemap[i][j].biome=="tundra":
            color=tundra
        elif tilemap[i][j].biome=="snow":
            color=snow
        elif tilemap[i][j].biome=="taiga":
            color=taiga
        elif tilemap[i][j].biome=="temperate_forest":
            color=temperate_forest
        elif tilemap[i][j].biome=="temperate_rainforest":
            color=temperate_rainforest
        elif tilemap[i][j].biome=="tropical_rainforest":
            color=tropical_rainforest
        elif tilemap[i][j].biome=="unknown":
            color=black
        else:
            color=black

        #render the tiles
        tile=pygame.Surface((tilesize,tilesize))
        tile.fill(color)
        screen.blit(tile,(i*tilesize, j*tilesize))

#I dont know why this is here but it probably does something important
pygame.display.flip()

#hit enter when you're done looking at the map
asdf=input("hit <enter> to exit")
