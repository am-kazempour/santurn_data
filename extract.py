import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



def train(X,Y):

    dt = DecisionTreeClassifier()
    clf = SVC(kernel='linear')

    x_ta,x_te,y_ta,y_te = train_test_split(X,Y,test_size=0.3)

    # Training and predict with Decision Tree algorithm
    dt.fit(x_ta,y_ta)
    DT_y = dt.predict(x_te)

    # Training and predict with svm algorithm
    clf.fit(x_ta, y_ta)
    svm_y = clf.predict(x_te)

    # Evaluation of Decision Tree algorithm
    print("DecisionTree accuracy: ",accuracy_score(y_te,DT_y))

    # Evaluation of SVM algorithm
    print("SVM accuracy: ",accuracy_score(y_te,svm_y))

images_path = [['datasets/wather/'+dir+"/"+file,dir ] for dir in os.listdir('datasets/wather') for file in os.listdir('datasets/wather/' + dir)]

images = []
labels = []

for image_file in images_path:
    image = cv2.imread(image_file[0])
    image = cv2.resize(image, (32, 32))
    image = np.array(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)).ravel()
    images.append(image)
    labels.append(image_file[1])
images = pd.DataFrame(images)
labels = pd.DataFrame(labels)
train(images,labels)