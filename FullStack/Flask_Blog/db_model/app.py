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
blogs_ref = db.collection(u'session_info')
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
      if doc.id == user_id :
            user = doc
            break
    if not user:
      return None
    
    print(user)
    user = User(user_id=user[0],user_email=user[1], blog_id=user[2])

  @staticmethod
  def create(user_email, blog_id):
    user = User.find(user_email)
    if user == None :
      users_ref.add(
        user_email = user_email,
        blog_id = blog_id
      )
      return User.find(user_email)
    else :
      return user

  @staticmethod
  def find(user_email):
    user = users_ref.where('user_email','==',user_email)
    if not user:
      return None
    
    print(user)
    user = User(user_id=user[0], user_email=user[1],blog_id=user[2])
    return user

class BlogSession():
  blog_page = {'A': 'blog_A.html', 'B':'blog_B.html'}
  session_count = 0

  @staticmethod
  def save_session_info(session_ip,user_email,webpage_name):
    now = datetime.now()
    now_time = nowstrftime('%d/%m/%Y %H:%M:%S')
blogs_ref.add(
  session_ip = session_ip,
  user_email = user_email,
  page = webpage_name,
  access_time = now_time
)

@staticmethod
def get_blog_page(force=None):
      print(force)
      if(force == None):
            if BlogSession.session_count == 0:
              BlogSession.session_count =1
              return 'blog_A.html'
            else :
              BlogSession.session_count = 0
              return 'blog_B.html'
      else :
        return BlogSession.blog_page[force]
    