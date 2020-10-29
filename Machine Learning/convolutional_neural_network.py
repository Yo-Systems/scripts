#Convolutional Neural Network

from keras.models import Sequential
from keras.layers import Convolutional2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialize the CNN
classifier = Sequential()

#Step 1 Convolution 
classifier.add(Convolutional2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))

#Step 2 Pooling is the max pooling step to make it smaller to enter into input layer of the ANN
classifier.add(MaxPooling2D(pool_size = (2, 2)))

#Adding a second convolutional layer for more accuracy
classifier.add(Convolutional2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))


#Flattening creates a vector that inputs into ANN
classifier.add(Flatten())

#Step 4 - Full connection 
classifier.add(Dense(output_dim = 128, activation = 'relu'))
classifier.add(Dense(output_dim = 1 , activation = 'sigmoid'))

#Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
		rescale=1./255,
		shear_range=0.2,
		zoom_range=0.2,
		horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('folder/subfolder', 
												target_size=(64, 64), 
												batch_size=32, 
												class_mode='binary')

test_set = test_datagen.flow_from_directory('folder/subfolder', 
											target_size=(64, 64), 
											batch_size=32, 
											class_mode ='binary')

classifier.fit(training_set,
			steps_per_epoch=8000,
			epochs=25,
			validation_data=test_set,
			validation_steps=2000)

