import cv2
import face_recognition
import os
import numpy as np



# (STEP 1)READING THE IMAGE  ONE BY ONE

path='known_images'             # storage dir of te known images
images=[]                   #  used to store the images
classNames=[]               # used to store the names
mylist=os.listdir(path)
print(mylist)

# import one by one image

for cls in mylist:
    curimg=cv2.imread(f'{path}/{cls}')    # cls is  the image from the path
    images.append(curimg)

    classNames.append(os.path.splitext(cls)[0])
print("known names are" ,classNames)


# (STEP 2)ENCODE THE IMAGE FROM THE IMAGE LIST
# find encodings for each one of them

def findencodings(images):
    encodelist=[]                       # list to store the group of encodings of each image
    for img in images:
        #convert the images into RGB
        img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        # add the encodings to append  list
        encodelist.append(encode)
    return encodelist


encodelistknown=findencodings(images)

print('encodings completed')



# (STEP 3 ) FIND THE MATCHES

# using the ontime rendering image
img=cv2.imread('gang.jpg')
# resize the image to spped up the process
img=cv2.resize(img,(700,500))
img_small = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faces_cur_frame = face_recognition.face_locations(img_small)
encode_cur_frame= face_recognition.face_encodings(img_small,faces_cur_frame)

# iterate through frame
for encodeface,faceloc in zip(encode_cur_frame,faces_cur_frame):
    matches=face_recognition.compare_faces(encodelistknown,encodeface)
    facedis=face_recognition.face_distance(encodelistknown,encodeface)  # compare with all the faces
                                                                        # in known list
    # lowest dis will be our best match
    print(facedis)
    matchindex=np.argmin(facedis)

    print(matches)
    if matches[matchindex]:             # if true
        name=classNames[matchindex].upper() #capital ltr
        print(name)

        y1,x2,y2,x1=faceloc

        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(img,(x1,y2-20),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(img,name,(x1+3,y2-3),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
    else:
        name = "Unknown"  # capital ltr
        print(name)

        y1, x2, y2, x1 = faceloc

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (x1 + 3, y2 - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow('images', img)
cv2.waitKey(0)

cv2.destroyAllWindows()









