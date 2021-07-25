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
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': "flask-blog-574c4",
  })
  db = firestore.client()
  return db

# doc_ref = db.collection(u'user_info').document('test')
# users_ref = db.collection(u'user_info')
# blogs_ref = db.collection(u'session_info')
# batch= db.batch()

## Create
# doc_ref.set({
#     u'user_id': u'test',
#     u'user_email': u'test@gmail.com',
# })
##Read
# docs = users_ref.stream()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')
##Update
#batch.update(doc_ref,{u'last' : 'Kim',u'first' :'Jieun'})
##delete
#db.collection(u'users').document(u'test').delete()    