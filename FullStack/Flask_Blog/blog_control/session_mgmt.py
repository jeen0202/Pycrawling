from db_model.firebase import conn_Firestore
from datetime import datetime

class BlogSession():
    blog_page = {'A':'blog_A.html','B':'blog_B.html'}
    sesson_count = 0

    @staticmethod
    def save_session_info(session_ip, user_email, webpage_name):
        now = datetime.now()
        now_time = now.strftime('%d/%m/%Y %H:%M:%S')
        
        db = conn_Firestore()
        db.add(
            session_ip=session_ip,
            user_email=user_email,
            page = webpage_name,
            access_time = now_time)

    @staticmethod
    def get_blog_page(blog_id=None):
        if blog_id == None:
            if BlogSession.sesson_count == 0:
                BlogSession.sesson_count = 1
                return 'blog_A.html'
            else :
                BlogSession.sesson_count =0
                return 'blog_B.html'
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