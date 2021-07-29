from db_model.firebase import conn_Firestore
from datetime import datetime

class BlogSession():
    blog_page = {'A':'blog_A.html','B':'blog_B.html'}
    session_count = True

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime('%d/%m/%Y %H:%M:%S')
        
        db = conn_Firestore()
        db.collection(u'session_info').add({
            u'session_ip':session_ip,
            u'user_email':user_email,
            u'page' : webpage_name,
            u'access_time' : now_time
        })

    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.session_count == True:
                BlogSession.session_count =False
                return BlogSession.blog_page['A']
            else :
                BlogSession.session_count = True
                return BlogSession.blog_page['B']
        else :
            return BlogSession.blog_page[blog_id]
        

# class BlogSession():
#   blog_page = {'A': 'blog_A.html', 'B':'blog_B.html'}
#   session_count = 0

#   @staticmethod
#   def save_session_info(session_ip,user_email,webpage_name):
#     now = datetime.now()
#     now_time = nowstrftime('%d/%m/%Y %H:%M:%S')
# blogs_ref.add(
#   session_ip = session_ip,
#   user_email = user_email,
#   page = webpage_name,
#   access_time = now_time
# )

# @staticmethod
# def get_blog_page(force=None):
#       print(force)
#       if(force == None):
#             if BlogSession.session_count == 0:
#               BlogSession.session_count =1
#               return 'blog_A.html'
#             else :
#               BlogSession.session_count = 0
#               return 'blog_B.html'
#       else :
#         return BlogSession.blog_page[force]