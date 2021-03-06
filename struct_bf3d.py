#Written by Michael Schnabel
#Last Modification 08.02.2016
#Structs of the BF3D Format 
from mathutils import Vector, Quaternion, Matrix

class Struct:
	def __init__ (self, *argv, **argd):
		if len(argd):
			# Update by dictionary
			self.__dict__.update (argd)
		else:
			# Update by position
			attrs = filter (lambda x: x[0:2] != "__", dir(self))
			for n in range(len(argv)):
				setattr(self, attrs[n], argv[n])
			
#######################################################################################
# Basic Structs
#######################################################################################
			
class RGBA(Struct):
	r = 0
	g = 0
	b = 0
	a = 0
	
#######################################################################################
# Model
#######################################################################################

#chunk 128
class Model(Struct):
	hieraName = "" # is empty
	meshes = []
	bSphere = None
	bBox = None
	
#######################################################################################
# Mesh
#######################################################################################	

#chunk 130
class MeshHeader(Struct):
	type = 0
	# 0	  -> normal mesh
	# 1	  -> normal mesh - two sided
	# 2	  -> normal mesh - camera oriented
	# 128 -> skin
	# 129 -> skin - two sided
   
	meshName = ""
	materialID = 0
	parentPivot = 0
	faceCount = 0
	vertCount = 0

#chunk 129
class Mesh(Struct):
	header = MeshHeader()
	verts = []
	normals = []
	faces = []
	uvCoords = []
	vertInfs = []
	
#######################################################################################
# VertexInfluences
#######################################################################################

#chunk 136
class MeshVertexInfluences(Struct):
	boneIdx = 0
	boneInf = 0.0
	xtraIdx = 0
	xtraInf = 0.0
	
#######################################################################################
# Box
#######################################################################################	

#chunk 192
class Box(Struct): 
	center = Vector((0.0, 0.0 ,0.0))
	extend = Vector((0.0, 0.0 ,0.0))
	
#######################################################################################
# Sphere
#######################################################################################	

#chunk 193
class Sphere(Struct): 
	center = Vector((0.0, 0.0 ,0.0))
	radius = 0.0
	
#######################################################################################
# Hierarchy
#######################################################################################

#chunk 257
class HierarchyHeader(Struct):
	name = ""
	pivotCount = 0
	centerPos = Vector((0.0, 0.0 ,0.0))

#chunk 258
class HierarchyPivot(Struct):
	name = ""
	parent = 0
	isBone = 1 #default 1
	matrix = Matrix()

# chunk 256
class Hierarchy(Struct):
	header = HierarchyHeader()
	pivots = []
	
#######################################################################################
# Animation
#######################################################################################

#chunk 513
class AnimationHeader(Struct):
	name = ""
	hieraName = ""
	frameRate = 0.0
	numFrames = 0
	
#chunk 515
class TimeCodedAnimationKey(Struct):
	frame = 0
	value = 0.0

#chunk 514
class TimeCodedAnimationChannel(Struct):
	pivot = 0 
	extrapolation = 0 #constant, linear or beizier
	type = 0 # xyz or quvw
	timeCodedKeys = []
	
#chunk 512
class Animation(Struct):
	header = AnimationHeader()
	channels = []
	