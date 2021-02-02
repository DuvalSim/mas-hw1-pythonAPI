import pyrebase

config = {
  "apiKey": "AIzaSyAQXySEkoPmkUhXsebjLbRv7Ri9NeS4RWo",
  "authDomain": "mas-hw1.firebaseapp.com",
  "databaseURL": "https://mas-hw1-default-rtdb.firebaseio.com",
  "storageBucket": "mas-hw1.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
print(db.child("users").get().val())
data = {"username": "Tintin ", "id":"2"}
db.child("users").child("Simon").set(data)
