from django.urls import path

from . import views

urlpatterns = [

    path('', views.BlogListview.as_view(), name='home'),
    path('detail/detail',views.BlogDetailview.as_view(),name='detail_blog'),
    path('detail/create',views.BlogCreateview.as_view(),name='create_blog'),
    path('detail/update',views.BlogUpdateview.as_view(),name='update_blog'),
    path('detail/delete',views.BlogDeleteview.as_view(),name='delete_blog')

]