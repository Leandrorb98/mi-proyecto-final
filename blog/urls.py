from blog.views import *

urlpatterns=[
    path('list/', ListPost.as_view(), name="list_post"),
    path('', index, name="index-blog"),
    path('logout/', BlogLogout.as_view(), name="blog-logout"),
    
]