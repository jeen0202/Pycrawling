from flask_login import UserMixin
from db_model.firebase import conn_Firestore

class User(UserMixin):

    def __init__(self,user_id,user_email,blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id
    
    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        db = conn_Firestore()
        query = db.collection(u'user_info').document(user_id).get()        
        id = query.id
        result= query.to_dict()
        print(result)
        if not result:
            return None
        user= User(user_id = id, user_email = result[u'user_email'], blog_id= result[u'blog_id'])
        return user
    
    @staticmethod
    def find(user_email):
        db = conn_Firestore()
        query = db.collection(u'user_info').where(u'user_email' ,u'==', user_email).get()
        result = None
        for doc in query:
            id = doc.id
            result= doc.to_dict()        
        if not result :
            return None
        else :            
            user= User( user_id = id,user_email = result[u'user_email'], blog_id= result[u'blog_id'])                       
            return user
    
    @staticmethod
    def create(user_email, blog_id):
        user = User.find(user_email)
        if user == None:
            db = conn_Firestore()
            db.collection(u'user_info').add({u'user_email':user_email, u'blog_id':blog_id})
            print(f'test : {User.find(user_email)}')
            return User.find(user_email)
        else :
            return user
    
    @staticmethod
    def delete(user_id):
        db = conn_Firestore()
        result= db.collection(u'user_info').document(user_id).delete()    
        print('Data Deleted')
        return result












# class User(UserMixin):

#   def __init__(self,user_id,user_email,blog_id):
#     self.id = user_id
#     self.user_email = user_email
#     self.blog_id = blog_id

#   def get_id(self):
#     return str(self.id)

#   @staticmethod
#   def get(user_id):
#     docs = users_ref.stream()
#     for doc in docs:
#       if doc.id == user_id :
#             user = doc
#             break
#     if not user:
#       return None
    
#     print(user)
#     user = User(user_id=user[0],user_email=user[1], blog_id=user[2])

#   @staticmethod
#   def create(user_email, blog_id):
#     user = User.find(user_email)
#     if user == None :
#       users_ref.add(
#         user_email = user_email,
#         blog_id = blog_id
#       )
#       return User.find(user_email)
#     else :
#       return user

#   @staticmethod
#   def find(user_email):
#     user = users_ref.where('user_email','==',user_email)
#     if not user:
#       return None
    
#     print(user)
#     user = User(user_id=user[0], user_email=user[1],blog_id=user[2])
#     return user



