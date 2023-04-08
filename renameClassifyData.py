import os
import shutil
import cv2



# Function to rename multiple files
def main():
	i = 0
	j = 0 #number of twins
	pathSource = os.path.dirname(__file__) + "/instaPictures/"
	pathDest =  os.path.dirname(__file__) + "/analysisAlgorithm/Data/InputData/training/images/"
	
	for filename in os.listdir(pathSource):
		
		originalImage =pathSource + filename
		if not(originalImage[-5] == ')'):
			newName = str(i)+ "_training" + ".tif"
			# Read the input image
			img = cv2.imread('test.jpg')
			# Convert into grayscale
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# Detect faces
			faces = face_cascade.detectMultiScale(gray, 1.1, 4)
			# Draw rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
				# Display the output
				cv2.imshow('img', img)
				cv2.waitKey()
			#enregistre l'image
			shutil.copyfile(originalImage, pathDest+newName)

		else:
			j +=1
			print("doublon : "+filename)
		i += 1
# Driver Code
if __name__ == '__main__':
	# Load the cascade
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	# Calling main() function
	main()


# tri des trops grands visages



