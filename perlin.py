class Perlin(object):
	'''private static readonly int[] permutation = { 151,160,137,91,90,15,					// Hash lookup table as defined by Ken Perlin.  This is a randomly
		131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,	// arranged array of all numbers from 0-255 inclusive.
		190, 6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,
		88,237,149,56,87,174,20,125,136,171,168, 68,175,74,165,71,134,139,48,27,166,
		77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,
		102,143,54, 65,25,63,161, 1,216,80,73,209,76,132,187,208, 89,18,169,200,196,
		135,130,116,188,159,86,164,100,109,198,173,186, 3,64,52,217,226,250,124,123,
		5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,
		223,183,170,213,119,248,152, 2,44,154,163, 70,221,153,101,155,167, 43,172,9,
		129,22,39,253, 19,98,108,110,79,113,224,232,178,185, 112,104,218,246,97,228,
		251,34,242,193,238,210,144,12,191,179,162,241, 81,51,145,235,249,14,239,107,
		49,192,214, 31,181,199,106,157,184, 84,204,176,115,121,50,45,127, 4,150,254,
		138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180
	};

	
	#Hash lookup table as defined by Ken Perlin.  This is a randomly
	#arranged array of all numbers from 0-255 inclusive.
	self.permutation=[151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]

	#private static readonly int[] p; 	(Doubled permutation to avoid overflow)
	self.p=[]

	self.repeat=0;
	
	#public Perlin(int repeat = -1)
	def __init__(self, repeat = -1):
		self.repeat = repeat
	}'''

	'''static Perlin() {
		p = new int[512];
		for(int x=0;x<512;x++) {
			p[x] = permutation[x%256];
		}
	}'''
	def __init__(self):
            	#p = new int[512];
		#for (int x=0;x<512;x++)
                self.permutation=[151,160,137,91,90,15,131,13,201,95,96,53,194,233,7,225,140,36,103,30,69,142,8,99,37,240,21,10,23,190,6,148,247,120,234,75,0,26,197,62,94,252,219,203,117,35,11,32,57,177,33,88,237,149,56,87,174,20,125,136,171,168,68,175,74,165,71,134,139,48,27,166,77,146,158,231,83,111,229,122,60,211,133,230,220,105,92,41,55,46,245,40,244,102,143,54,65,25,63,161,1,216,80,73,209,76,132,187,208,89,18,169,200,196,135,130,116,188,159,86,164,100,109,198,173,186,3,64,52,217,226,250,124,123,5,202,38,147,118,126,255,82,85,212,207,206,59,227,47,16,58,17,182,189,28,42,223,183,170,213,119,248,152,2,44,154,163,70,221,153,101,155,167,43,172,9,129,22,39,253,19,98,108,110,79,113,224,232,178,185,112,104,218,246,97,228,251,34,242,193,238,210,144,12,191,179,162,241,81,51,145,235,249,14,239,107,49,192,214,31,181,199,106,157,184,84,204,176,115,121,50,45,127,4,150,254,138,236,205,93,222,114,67,29,24,72,243,141,128,195,78,66,215,61,156,180]
                self.p=[]
                self.repeat=0
                for x in range(0,512):
                    self.p.append(self.permutation[x%256])

	#public double OctavePerlin(double x, double y, double z, int octaves, double persistence)
	def OctavePerlin(self, x, y, z, octaves, persistence):
		total = 0.0
		frequency = 1.0
		amplitude = 1.0
		maxValue = 0.0		# Used for normalizing result to 0.0 - 1.0

		#for (int i=0;i<octaves;i++)
		for i in range(0,octaves):

			total += self.perlin(x * frequency, y * frequency, z * frequency) * amplitude
			
			maxValue += amplitude
			
			amplitude *= persistence

			frequency *= 2
		
		return (float(total)/float(maxValue))
	
	
	#public double perlin(double x, double y, double z)
	def perlin(self, x, y, z):

		#If we have any repeat on, change the coordinates to their "local" repetitions
		if(self.repeat > 0):
			x = x%self.repeat;
			y = y%self.repeat;
			z = z%self.repeat;
		

		xi = int(x) & 255 #Calculate the "unit cube" that the point asked will be located in
		yi = int(y) & 255 #The left bound is ( |_x_|,|_y_|,|_z_| ) and the right bound is that
		zi = int(z) & 255 #plus 1.  Next we calculate the location (from 0.0 to 1.0) in that cube.
		xf = float(float(x)-int(x)) #We also fade the location to smooth the result.
		yf = float(float(y)-int(y))
		zf = float(float(z)-int(z))
		u = self.fade(xf)
		v = self.fade(yf)
		w = self.fade(zf)

											
		#int aaa, aba, aab, abb, baa, bba, bab, bbb;

		aaa = self.p[self.p[self.p[xi]+yi]+zi]
		aba = self.p[self.p[self.p[xi]+yi+1]+zi]
		aab = self.p[self.p[self.p[xi]+yi]+zi+1]
		abb = self.p[self.p[self.p[xi]+yi+1]+zi+1]
		baa = self.p[self.p[self.p[xi+1]+yi]+zi]
		bba = self.p[self.p[self.p[xi+1]+yi+1]+zi]
		bab = self.p[self.p[self.p[xi+1]+yi]+zi+1]
		bbb = self.p[self.p[self.p[xi+1]+yi+1]+zi+1]
	
		
		#double x1, x2, y1, y2;

		#The gradient function calculates the dot product between a pseudorandom
		#gradient vector and the vector from the input coordinate to the 8
		#surrounding points in its unit cube.
		x1 = self.lerp(self.grad (aaa, xf  , yf  , zf), self.grad (baa, xf-1, yf  , zf), u)
		#This is all then lerped together as a sort of weighted average based on the faded (u,v,w)
		#values we made earlier.
		x2 = self.lerp(	self.grad (aba, xf  , yf-1, zf), self.grad (bba, xf-1, yf-1, zf), u)


		y1 = self.lerp(x1, x2, v)

		x1 = self.lerp(	self.grad (aab, xf  , yf  , zf-1), self.grad (bab, xf-1, yf  , zf-1), u)

		x2 = self.lerp(	self.grad (abb, xf  , yf-1, zf-1), self.grad (bbb, xf-1, yf-1, zf-1), u)

		y2 = self.lerp(x1, x2, v)
		
		#For convenience we bound it to 0 - 1 (theoretical min/max before is -1 - 1)
		return float((self.lerp(y1, y2, w)+1.0)/2.0)
	
	'''public int inc(int num) {
		num++;
		if (repeat > 0) num %= repeat;
		
		return num;
	}'''
	

	#public static double grad(int hash, double x, double y, double z)
	def grad(self, hsh, x, y, z):

		#Take the hashed value and take the first 4 bits of it (15 == 0b1111)
		h = int(hsh & 15)

		#If the most significant bit (MSB) of the hash is 0 then set u = x.  Otherwise y.
		u = float(x) if h<8 else float(y)
		
		#In Ken Perlin's original implementation this was another conditional operator (?:).  I
		#expanded it for readability.
		v=0.0
		
		#If the first and second significant bits are 0 set v = y
		if(h < 4):
			v = y

		#If the first and second significant bits are 1 set v = x
		elif(h == 12 or h == 14 ):
			v = x

		#If the first and second significant bits are not equal (0/1, 1/0) set v = z
		else:
			v = z

		#Use the last 2 bits to decide if u and v are positive or negative
		#Then return their addition.
		return float( u if (h&1) == 0 else -u)+ float( v if (h&2) == 0 else -v)
	
	#public static double fade(double t)
	def fade(self,t):
		#Fade function as defined by Ken Perlin.  This eases coordinate values
		#so that they will "ease" towards integral values.  This ends up smoothing
		#the final output.

		return float(t * t * t * (t * (t * 6.0 - 15.0) + 10.0)) #6t^5 - 15t^4 + 10t^3
	

	#public static double lerp(double a, double b, double x)
	def lerp(self, a, b, x):
		return float(a + x * (b - a))

if __name__=='__main__':
        pclass=Perlin()
        tilemap=[]
        for i in range(0,16):
                row=[]
                for j in range(0,16):
                        row.append(int(255.0*pclass.OctavePerlin(float(i/10.0),float(j/10.0),1.0,2,0.1)))
                tilemap.append(row)
                print(row)
        #print(tilemap)
