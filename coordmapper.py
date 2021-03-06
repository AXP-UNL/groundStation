import math

#def gps2ecef_pyproj(lat, lon, alt):
#	cosLat = math.cos(lat * math.pi / 180.0)
#	sinLat = math.sin(lat * math.pi / 180.0)
#	cosLon = math.cos(lon * math.pi / 180.0)
#	sinLon = math.sin(lon * math.pi / 180.0)
#	rad = 6378137.0
#	f = 1.0 / 298.257224
#	C = 1.0 / math.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
#	S = (1.0 - f) * (1.0 - f) * C
#	h = 0.0
#	x = (rad * C + h) * cosLat * cosLon
#	y = (rad * C + h) * cosLat * sinLon
#	z = (rad * S + h) * sinLat

	# Depreciated due to pyproj being difficult to install on ARM architechture
	#ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
	#lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')
	#x, y, z = pyproj.transform(lla, ecef, lon, lat, alt, radians=False)
#	return x, y, z
# hidden
def gps2ecef_custom(latitude, longitude, altitude):
	# (lat, lon) in WSG-84 degrees
	# altitude in meters
	cosLat = math.cos(latitude * math.pi / 180)
	sinLat = math.sin(latitude * math.pi / 180)

	cosLong = math.cos(longitude * math.pi / 180)
	sinLong = math.sin(longitude * math.pi / 180)
 
	c = 1 / math.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
	s = (1 - f) * (1 - f) * c

	x = (R*c + altitude) * cosLat * cosLong
	y = (R*c + altitude) * cosLat * sinLong
	z = (R*s + altitude) * sinLat
	return x, y, z
# hidden
def ecef_to_enu(x, y, z, latRef, longRef, altRef):
	cosLatRef = math.cos(latRef * math.pi / 180)
	sinLatRef = math.sin(latRef * math.pi / 180)

	cosLongRef = math.cos(longRef * math.pi / 180)
	sinLongRef = math.sin(longRef * math.pi / 180)

	cRef = 1 / math.sqrt(cosLatRef * cosLatRef + (1 - f) * (1 - f) * sinLatRef * sinLatRef)

	x0 = (R*cRef + altRef) * cosLatRef * cosLongRef
	y0 = (R*cRef + altRef) * cosLatRef * sinLongRef
	z0 = (R*cRef*(1-e2) + altRef) * sinLatRef

	xEast = (-(x-x0) * sinLongRef) + ((y-y0)*cosLongRef)

	yNorth = (-cosLongRef*sinLatRef*(x-x0)) - (sinLatRef*sinLongRef*(y-y0)) + (cosLatRef*(z-z0))

	zUp = (cosLatRef*cosLongRef*(x-x0)) + (cosLatRef*sinLongRef*(y-y0)) + (sinLatRef*(z-z0))
	return xEast, yNorth, zUp

# Geodetic Coordinates (Latitude, Longitude, Altitude)
def geodetic_to_enu(lat, lon, h, lat_ref, lon_ref, h_ref):
	x, y, z = gps2ecef_custom(lat, lon, h)
	return ecef_to_enu(x, y, z, lat_ref, lon_ref, h_ref)

def geodetic_to_enu(qu_LLA, rf_LLA):
	ECEF    = gps2ecef_custom(qu_LLA)
	ENU     = ecef_to_enu(ECEF, rf_LLA)
	return ENU

#class centerPivot():
#	def __init__(self):
#		self.pos = 0;
#		centerPivot.start()
#	def start():
#		# TODO go to 0* north
#	def gotoPos(bearing)
#		# TODO 


def run_test():
	ex_LLA = [
		(0,  45,  1000),
		(45, 90,  2000),
		(48.8567,  2.3508,  80),
		(61.4140105652, 23.7281341313, 149.821),
		(51.760597, -1.261247, 114.284188),
	]
	customTest = [
		(41.552214, 96.132324, 0),
	]

	for pt in ex_LLA:
		#xPy,yPy,zPy = gps2ecef_pyproj(pt[0], pt[1], pt[2])
		xF,yF,zF        = gps2ecef_custom(pt[0], pt[1], pt[2])
		xE, yN, zU  = ecef_to_enu(xF,yF,zF, pt[0], pt[1], pt[2])

		print('\n>>> LLA: {}'.format(pt))
		#print(">> pyproj (XYZ)\t = ", xPy, yPy, zPy)
		print(">> ECEF (XYZ)\t = ", xF, yF, zF)
		print('>> ENU (XYZ) \t = ', xE, yN, zU)
		print('-'*100)

	for pt in customTest:
		xF, yF, zF 	= gps2ecef_custom(pt[0], pt[1], pt[2])
		print('\n>>> LLA: {}'.format(pt))
		print(">>ECEF (XYZ)\t = ", xF, yF, zF)
		print('-'*100)
R = 6378137
f_inv = 298.257224
f = 1.0 / f_inv
e2 = 1 - (1 - f) * (1 - f)
run_test()
