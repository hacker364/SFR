import face_recognition
from sklearn import svm
import os

encodings = []
names = []

#Directory with Training Data
os.chdir('/home/henil/Projects/hackathon/SFR')
train_dir = os.listdir('StudentDetails')
base = "/home/henil/Projects/hackathon/SFR/"
#Looping through each folder in train_dir
for person in train_dir:
    pid = os.listdir(base + "StudentDetails/" + person)

    for person_img in pid:
        #Looping through each photo of a person for training
        face = face_recognition.load_image_file(base + "/StudentDetails/" + person + "/" + person_img)
        face_bounding_box = face_recognition.face_locations(face)

        #Training Data must contain exactly one face per photo
        if len(face_bounding_box) == 1:
            face_enc = face_recognition.face_encodings(face)[0]
            #Appending the Data to array
            encodings.append(face_enc)
            names.append(person)
        else:
            print(person + "/" + person_img + " was skipped and can't be processed")

#Create and train the SVC classifier
clf = svm.SVC(gamma='scale')
clf.fit(encodings,names)

#Loading the test image with unknown faces into a numpy array
test_image = face_recognition.load_image_file(base + 'test_image.jpeg')

#Find all the faces in the test image
face_locations = face_recognition.face_locations(test_image)
no = len(face_locations)
print("Number of faces detected: ", no)

print("Found: ")
for i in range(no):
    test_image_enc = face_recognition.face_encodings(test_image)[i]
    name = clf.predict([test_image_enc])
    print(*name)
