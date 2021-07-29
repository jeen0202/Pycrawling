import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "flask-blog-574c4",
})

db = firestore.client()

def conn_Firestore():
  if not firebase_admin.get_app():
    cred = credentials.ApplicationDefault()
    firebase_admin.initialize_app(cred, {
      'projectId': "flask-blog-574c4",
    })
  db = firestore.client()
  return db 