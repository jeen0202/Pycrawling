import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "flask-blog-574c4",
})

db = firestore.client()

doc_ref = db.collection(u'user_info').document('test')
users_ref = db.collection(u'user_info')
batch= db.batch()
## Create
doc_ref.set({
    u'user_id': u'test',
    u'user_email': u'test@gmail.com',
})


##Read
# docs = users_ref.stream()

# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

##Update
batch.update(doc_ref,{u'last' : 'Kim',u'first' :'Jieun'})

##delete
#db.collection(u'users').document(u'test').delete()

class User(UserMixin):

  def __init__(self,user_id,user_email,blog_id):
    self.id = user_id
    self.user_email = user_email
    self.blog_id = blog_id

  def get_id(self):
    return str(self.id)
  @staticmethod
  def get(user_id):
    docs = users_ref.stream()
    for doc in docs:
      if doc.user_id == user_id :
            return doc
