import pyimgur

CLIENT_ID = "f0e83904a2dee5a"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image("IMAGE.jpg", title="Uploaded with PyImgur") #sends out url


# hello......eEEEEEEEEEEE is it me you're looking for.........

from firebase import firebase
#firebase = firebase.FirebaseApplication('https://peoplecon2.firebaseio.com', None)
#new_user = 'Utkarsh Tandon'

#result = firebase.post('/', {'print': 'silent', 'people': numfaces , 'name': 'Tanay', 'state' : 'California', 'url' : uploaded_image.link})

firebase = firebase.FirebaseApplication("https://testdetectpy.firebaseio.com/", None)
new_user = 'sbsripad'

result = firebase.get('/users', None)
print result
#result = firebase.post('/', {'url' : uploaded_image.link})