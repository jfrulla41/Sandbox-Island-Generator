import random, math, perlin, sys, tile, noise

class Map(object):

#*slaps roof of program*
#this bad boy can hold so many if-statements
    

###############################################################################
# CONSTRUCTOR
###############################################################################

    def __init__(self,rows,cols):
        
        #create datamembers rows, cols, current_i, current_j, and tilemap
        self.rows=rows
        self.cols=cols
        self.tilemap=[]
        self.current_i=0
        self.current_j=0
        self.borderBuffer=128.0

        #set the default values for generating the perlin noise elevation map
        self.perlinOffset=0.002
        self.perlinOctaves=8
        self.elevationSeed=random.random()*1000000
        self.perlinPersistence=0.5        

        #fill two dimensional tilemap with empty tile objects
        for i in range(0,rows):
            row=[]
            for j in range(0,cols):
                row.append(tile.Tile())
            self.tilemap.append(row)


    def getDistance(self,x,y):
        return int(math.sqrt(x**2 + y**2))

    def getDistance2(self,x1,y1,x2,y2):
        return int(math.sqrt((x2-x1)**2 + (y2-y1)**2))


###############################################################################
# SET NEW VALUES FOR THE PERLIN NOISE MAP FUNCTION
###############################################################################

    def setPerlinVariables(self, offset, octaves, persistence, seed=(random.random()*1000000)):
        self.perlinOffset=offset
        self.elevationSeed=seed
        self.perlinOctaves=octaves
        self.perlinPersistence=persistence


###############################################################################
# RECURSIVE METHOD FOR CREATING RIVERS
###############################################################################

    def extend_river(self,i,j):
        if(self.tilemap[i][j].type!="water" and self.tilemap[i][j].elevation<64):
            #river starts at the ocean
            sys.setrecursionlimit(100000)
            self.tilemap[i][j].type="water"
            self.tilemap[i][j].subtype="river"
            
            #first the river moves up via elevation
            if(self.tilemap[i-1][j].elevation>self.tilemap[i][j].elevation and self.tilemap[i-1][j].type!="water"):
                self.extend_river(i-1,j)
            elif(self.tilemap[i][j-1].elevation>self.tilemap[i][j].elevation and self.tilemap[i][j-1].type!="water"):
                self.extend_river(i,j-1)
            elif(self.tilemap[i+1][j].elevation>self.tilemap[i][j].elevation and self.tilemap[i+1][j].type!="water"):
                self.extend_river(i+1,j)
            elif(self.tilemap[i][j+1].elevation>self.tilemap[i][j].elevation and self.tilemap[i][j+1].type!="water"):
                self.extend_river(i,j+1)
            elif(self.tilemap[i-1][j-1].elevation>self.tilemap[i][j].elevation and self.tilemap[i-1][j-1].type!="water"):
                self.extend_river(i-1,j-1)
            elif(self.tilemap[i+1][j-1].elevation>self.tilemap[i][j].elevation and self.tilemap[i+1][j-1].type!="water"):
                self.extend_river(i+1,j-1)
            elif(self.tilemap[i+1][j+1].elevation>self.tilemap[i][j].elevation and self.tilemap[i+1][j+1].type!="water"):
                self.extend_river(i+1,j+1)
            elif(self.tilemap[i-1][j+1].elevation>self.tilemap[i][j].elevation and self.tilemap[i-1][j+1].type!="water"):
                self.extend_river(i-1,j+1)


            #river stays on level surfaces if there's no adjacent higher elevation tiles
            elif(self.tilemap[i-1][j].elevation==self.tilemap[i][j].elevation and self.tilemap[i-1][j].type!="water"):
                self.extend_river(i-1,j)
            elif(self.tilemap[i][j-1].elevation==self.tilemap[i][j].elevation and self.tilemap[i][j-1].type!="water"):
                self.extend_river(i,j-1)
            elif(self.tilemap[i+1][j].elevation==self.tilemap[i][j].elevation and self.tilemap[i+1][j].type!="water"):
                self.extend_river(i+1,j)
            elif(self.tilemap[i][j+1].elevation==self.tilemap[i][j].elevation and self.tilemap[i][j+1].type!="water"):
                self.extend_river(i,j+1)
            elif(self.tilemap[i-1][j-1].elevation==self.tilemap[i][j].elevation and self.tilemap[i-1][j-1].type!="water"):
                self.extend_river(i-1,j-1)
            elif(self.tilemap[i+1][j-1].elevation==self.tilemap[i][j].elevation and self.tilemap[i+1][j-1].type!="water"):
                self.extend_river(i+1,j-1)
            elif(self.tilemap[i-1][j+1].elevation==self.tilemap[i][j].elevation and self.tilemap[i-1][j+1].type!="water"):
                self.extend_river(i-1,j+1)
            elif(self.tilemap[i+1][j+1].elevation==self.tilemap[i][j].elevation and self.tilemap[i+1][j+1].type!="water"):
                self.extend_river(i+1,j+1)

            #if the current tile is surrounded by lower elevation tiles, it will move towards higher humidities
            
            elif(self.tilemap[i-1][j].type!="water"):
                self.extend_river(i-1,j)
            elif(self.tilemap[i][j-1].type!="water"):
                self.extend_river(i,j-1)
            elif(self.tilemap[i+1][j].type!="water"):
                self.extend_river(i+1,j)
            elif(self.tilemap[i][j+1].type!="water"):
                self.extend_river(i,j+1)
            elif(self.tilemap[i-1][j-1].type!="water"):
                self.extend_river(i-1,j-1)
            elif(self.tilemap[i+1][j-1].type!="water"):
                self.extend_river(i+1,j-1)
            elif(self.tilemap[i-1][j+1].type!="water"):
                self.extend_river(i-1,j+1)
            elif(self.tilemap[i+1][j+1].type!="water"):
                self.extend_river(i+1,j+1)
            
            #once the main course of the river is plotted, extend the river out to the surrounding
            #adjacent tiles
            if(self.tilemap[i-1][j].type!="water"):    
                self.tilemap[i-1][j].type="water"
                self.tilemap[i-1][j].subtype="river"
            if(self.tilemap[i][j-1].type!="water"):    
                self.tilemap[i][j-1].type="water"
                self.tilemap[i][j-1].subtype="river"
            if(self.tilemap[i+1][j].type!="water"):    
                self.tilemap[i+1][j].type="water"
                self.tilemap[i+1][j].subtype="river"
            if(self.tilemap[i][j+1].type!="water"):    
                self.tilemap[i][j+1].type="water"
                self.tilemap[i][j+1].subtype="river"



###############################################################################
# MAIN METHOD TO CREATE THE MAP
###############################################################################
    
    def createMap(self):



        #indirection for a few variables that will be used frequently
        rows=self.rows
        cols=self.cols
        borderBuffer=self.borderBuffer
      

  
        #First Create the elevation map using (perlin) noise
        #######################################################################        
        
        print("Carving Land...")

        #setup initial values
        offset=self.perlinOffset
        i_offset=0.0
        j_offset=0.0

        #create the elevation map
        for i in range(rows):
            i_offset=i*offset
            for j in range(cols):
                j_offset=j*offset

                #get noisy value between -1 and 1
                pnoise = noise.pnoise3(i_offset,j_offset,self.elevationSeed,self.perlinOctaves,self.perlinPersistence)
                
                #set current tile's elevation to between -255 and +255
                self.tilemap[i][j].elevation=int(pnoise*255)
        



        #Reduce the elevation of tiles as they approach the border of the map
        ####################################################################### 

        print("Shifting Techtonic plates...")
        
        #for each tile
        for i in range(0,rows):
            for j in range(0,cols):

                #if the tile is less than borderBuffer(128) tiles away from the edge, 
                #then reduce its elevation
                distance=self.getDistance2(i,j,rows/2,cols/2)
                if(distance>=(rows/2 - borderBuffer)):
                    self.tilemap[i][j].elevation+=int(float(rows)/2.0-borderBuffer-float(distance))

                #if the elevation is less than -255, then set it equal to -255
                self.tilemap[i][j].elevation = self.tilemap[i][j].elevation if self.tilemap[i][j].elevation>=-255 else -255


        
        #TODO--Smooth the coastlines
        

        #Create rivers
        ####################################################################### 
        
        print("Melting Glaciers...")

        #for each tile
        for i in range(1,rows-1):
            for j in range(1,cols-1):
                if(self.tilemap[i][j].elevation==0):
                    if(random.random()>0.999):
                        self.extend_river(i,j)
                


        #Identify ocean and lake tiles, set baseline humidity, and disperse humidity values
        ####################################################################### 

        ocean_identified=False
        fanned=False
        count=0

        print("Flooding... (takes a sec)")

        #this will continue cycling through every tile until
        #all of the oceans tiles and lake tiles are identified
        #it will also keep going until the humidity map is complete
        while(not ocean_identified and not fanned):

            #reset flags
            ocean_identified=True
            fanned=True
            count+=1

            #the for-loops toggle between going from 
            #left->right;top->bottom and left->right;bottom->top
            #(this helps areas like bays that only have land tiles above them)
            if(count%2==1):
                startrow=0
                startcol=0
                endrow=rows
                endcol=cols
                direction=1
            else:
                startrow=rows-1
                startcol=cols-1
                endrow=0
                endcol=0
                direction=-1

            #for each tile
            for i in range(startrow,endrow,direction):
                for j in range(startcol,endcol,direction):

                    #if the tile is along the edge, then it's ocean
                    if((i==0 or j==0 or i==rows-1 or j==cols-1) and self.tilemap[i][j].subtype==""):
                        self.tilemap[i][j].type="water"
                        self.tilemap[i][j].subtype="ocean"
                        self.tilemap[i][j].humidity=100

                    #if it's not along the edges...
                    else:

                        #if it's land, mark it and forget about it
                        if(self.tilemap[i][j].elevation>0 and self.tilemap[i][j].type==""):
                            self.tilemap[i][j].type="land"

                        #if it's water and it hasn't been labelled yet...      
                        elif(self.tilemap[i][j].elevation<=0 and self.tilemap[i][j].subtype==""):

                            #set the initial humidity to 75 
                            #(lake tiles should be the only ones with 75 after this loop)
                            self.tilemap[i][j].type = "water"
                            self.tilemap[i][j].humidity=75.0

                            #if any of the adjacent tiles are ocean, then this one is too.
                            if self.tilemap[i-1][j  ].subtype == "ocean" or self.tilemap[i  ][j-1].subtype == "ocean" or self.tilemap[i+1][j  ].subtype == "ocean" or self.tilemap[i  ][j+1].subtype == "ocean":
                                self.tilemap[i][j].subtype = "ocean"
                                self.tilemap[i][j].humidity=100.0

                                #set the flag so we know that not all the ocean tiles
                                #have been identified yet
                                ocean_identified=False

                    #if the current tile is land, then distribute the humidity
                    if(self.tilemap[i][j].elevation>0):

                        #initial max humidity set to current tile
                        max_humidity=self.tilemap[i][j].humidity

                        #max humidity is set to the highest humidity of all the adjacent tiles
                        if(self.tilemap[i-1][j].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j].humidity-.5
                        if(self.tilemap[i][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i][j-1].humidity-.5
                        if(self.tilemap[i+1][j].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j].humidity-.5
                        if(self.tilemap[i][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i][j+1].humidity-.5

                        if(self.tilemap[i-1][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j-1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i+1][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j-1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i+1][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j+1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i-1][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j+1].humidity-math.sqrt(2.0*(.5**2))

                        #if an adjacent tile has a higher humidity than the current tile,
                        #recalculate humidity and set the flag
                        if(max_humidity>self.tilemap[i][j].humidity):
                            fanned=False
                            self.tilemap[i][j].humidity=max_humidity

        #Add additional humidity for increased elevations and rivers
        #######################################################################
        print("Misting...")
        for i in range(rows):
            for j in range(cols):

                if(self.tilemap[i][j].type=="water" and self.tilemap[i][j].humidity==75):
                    self.tilemap[i][j].subtype="lake"
                
                #rivers add 25 humidity to what was already there
                if(self.tilemap[i][j].subtype=="river"):
                    self.tilemap[i][j].humidity+=25.0

                #higher elevations add humidity too
                if(self.tilemap[i][j].elevation>=1):
                    self.tilemap[i][j].humidity+=(self.tilemap[i][j].elevation/3.0)




        #Fan it a second time to disperse the additional humidity
        #######################################################################
        print("Evaporating...")
        while(not fanned):

            #reset flags
            fanned=True
            count+=1

            #the for-loops toggle between going from 
            #left->right;top->bottom and left->right;bottom->top
            #(this helps areas like bays that only have land tiles above them)
            if(count%2==1):
                startrow=0
                startcol=0
                endrow=rows
                endcol=cols
                direction=1
            else:
                startrow=rows-1
                startcol=cols-1
                endrow=0
                endcol=0
                direction=-1

            #for each tile
            for i in range(startrow,endrow,direction):
                for j in range(startcol,endcol,direction):
                    #if the current tile is land, then distribute the humidity
                    if(self.tilemap[i][j].elevation>0):

                        #initial max humidity set to current tile
                        max_humidity=self.tilemap[i][j].humidity

                        #max humidity is set to the highest humidity of all the adjacent tiles
                        if(self.tilemap[i-1][j].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j].humidity-.5
                        if(self.tilemap[i][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i][j-1].humidity-.5
                        if(self.tilemap[i+1][j].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j].humidity-.5
                        if(self.tilemap[i][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i][j+1].humidity-.5

                        if(self.tilemap[i-1][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j-1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i+1][j-1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j-1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i+1][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i+1][j+1].humidity-math.sqrt(2.0*(.5**2))
                        if(self.tilemap[i-1][j+1].humidity-1>max_humidity):
                            max_humidity=self.tilemap[i-1][j+1].humidity-math.sqrt(2.0*(.5**2))

                        #if an adjacent tile has a higher humidity than the current tile,
                        #recalculate humidity and set the flag
                        if(max_humidity>self.tilemap[i][j].humidity):
                            fanned=False
                            self.tilemap[i][j].humidity=max_humidity

        #Use Humidity and elevation values to Identify the biomes
        ####################################################################### 
        print("Climatizing...")
        for i in range(0,rows):
            for j in range(0,cols):

                #separate the map into 4 or 5 different elevation zones
                if(self.tilemap[i][j].elevation<5):
                    elevation_zone=-1
                elif(self.tilemap[i][j].elevation>=100):
                    elevation_zone=4
                elif(self.tilemap[i][j].elevation<100 and self.tilemap[i][j].elevation>=75):
                    elevation_zone=3
                elif(self.tilemap[i][j].elevation<75 and self.tilemap[i][j].elevation>=50):
                    elevation_zone=2
                elif(self.tilemap[i][j].elevation<50 and self.tilemap[i][j].elevation>=25):
                    elevation_zone=1
                else:
                    elevation_zone=0

                #separate the map into 7 different moisture zones
                if(self.tilemap[i][j].humidity>=95):
                    moisture_zone=6
                elif(self.tilemap[i][j].humidity<95 and self.tilemap[i][j].humidity>=80):
                    moisture_zone=5
                elif(self.tilemap[i][j].humidity<80 and self.tilemap[i][j].humidity>=65):
                    moisture_zone=4
                elif(self.tilemap[i][j].humidity<65 and self.tilemap[i][j].humidity>=50):
                    moisture_zone=3
                elif(self.tilemap[i][j].humidity<50 and self.tilemap[i][j].humidity>=35):
                    moisture_zone=2
                elif(self.tilemap[i][j].humidity<35 and self.tilemap[i][j].humidity>=15):
                    moisture_zone=1
                elif(self.tilemap[i][j].humidity<15):
                    moisture_zone=0

                if(elevation_zone==-1 and moisture_zone==6):
                    self.tilemap[i][j].biome="beach"
                elif(elevation_zone<=3 and moisture_zone==0):
                    self.tilemap[i][j].biome="desert"
                elif(elevation_zone==4 and moisture_zone==0):
                    self.tilemap[i][j].biome="scorched"
                elif((elevation_zone<=2 and moisture_zone==1) or (moisture_zone==2 and elevation_zone==2)):
                    self.tilemap[i][j].biome="grassland"
                elif(elevation_zone==3 and moisture_zone==1):
                    self.tilemap[i][j].biome="desert"
                elif(elevation_zone==4 and moisture_zone==1):
                    self.tilemap[i][j].biome="bare"
                elif(elevation_zone<=1 and (moisture_zone==2 or moisture_zone==3)):
                    self.tilemap[i][j].biome="seasonal_forest"
                elif(elevation_zone==3 and (moisture_zone==2 or moisture_zone==3)):
                    self.tilemap[i][j].biome="shrubland"
                elif(elevation_zone==4 and moisture_zone==2):
                    self.tilemap[i][j].biome="tundra"
                elif(elevation_zone==4 and moisture_zone>=3):
                    self.tilemap[i][j].biome="snow"
                elif(elevation_zone==3 and moisture_zone>=4):
                    self.tilemap[i][j].biome="taiga"
                elif(elevation_zone==2 and (moisture_zone==3 or moisture_zone==4)):
                    self.tilemap[i][j].biome="temperate_forest"
                elif(elevation_zone==2 and moisture_zone==5):
                    self.tilemap[i][j].biome="temperate_rainforest"
                else:
                    self.tilemap[i][j].biome="tropical_rainforest"


        #TODO--Create populated areas
        #TODO--Generate zones where trees are clustered (and plant individual trees within those clusters)
        
        return self.tilemap
