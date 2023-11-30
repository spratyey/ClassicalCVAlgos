import numpy as np
import cv2

class Tomasi:
	def __init__(self, L, R):
		def SubPixelColor(img, shape):
			
			imgMin = np.zeros_like(img)
			imgMax = np.zeros_like(img)
			
			imgPadded = np.pad(img, ((1,1),(1,1),(0,0)), mode='edge')
			
			I1 = (imgPadded[1:-1,:-2,:] + imgPadded[1:-1,1:-1,:]) / 2
			I2 = (imgPadded[1:-1,2:,:] + imgPadded[1:-1,1:-1,:]) / 2
			I3 = (imgPadded[:-2,1:-1,:] + imgPadded[1:-1,1:-1,:]) / 2
			I4 = (imgPadded[2:,1:-1,:] + imgPadded[1:-1,1:-1,:]) / 2
			
			I_min = img
			I_min = np.minimum(I_min, I1)
			I_min = np.minimum(I_min, I2)
			I_min = np.minimum(I_min, I3)
			I_min = np.minimum(I_min, I4)

			I_max = img
			I_max = np.maximum(I_max, I1)
			I_max = np.maximum(I_max, I2)
			I_max = np.maximum(I_max, I3)
			I_max = np.maximum(I_max, I4)

			
			imgMin[1:-1,1:-1,:] = I_min
			imgMax[1:-1,1:-1,:] = I_max

			return imgMin, imgMax

		self.LMin = np.zeros(shape=(L.shape[0], L.shape[1], 3))
		self.LMax = np.zeros(shape=(L.shape[0], L.shape[1], 3))
		self.RMin = np.zeros(shape=(R.shape[0], R.shape[1], 3))
		self.RMax = np.zeros(shape=(R.shape[0], R.shape[1], 3))

		self.LMin, self.LMax = SubPixelColor(L, self.LMin.shape)
		self.RMin, self.RMax = SubPixelColor(R, self.RMin.shape)


	def get_tomasi_penalty(self, coordL, coordR, L, R, cutoff):
		Ip = L[tuple(coordL)].astype(np.float32)
		Iq = R[tuple(coordR)].astype(np.float32)

		IpMin = self.LMin[tuple(coordL)].astype(np.float32)
		IqMin = self.RMin[tuple(coordR)].astype(np.float32)

		IpMax = self.LMax[tuple(coordL)].astype(np.float32)
		IqMax = self.RMax[tuple(coordR)].astype(np.float32)

		dp = np.maximum(Ip - IqMax, 0) + np.maximum(IqMin - Ip, 0)
		dq = np.maximum(Iq - IpMax, 0) + np.maximum(IpMin - Iq, 0)

		d = np.minimum(dp, dq)

		d[d > cutoff] = cutoff
		d = d ** 2
		return np.sum(d)
	


    
    
