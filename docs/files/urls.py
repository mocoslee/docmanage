#coding:utf-8
from django.conf.urls import include,url
from . import views


urlpatterns = [
    url(r'^upload$',views.UploadView.as_view(),name="upload"),
    url(r'^filelist$',views.FileListView.as_view(action=""),name="filelist"),
    url(r'^add_dir$',views.FileListView.as_view(action="add_dir"),name="add_dir"),
    url(r'^allfiles$',views.FileListView.as_view(action="allfiles"),name="allfiles"),
    url(r'^allimages$',views.FileListView.as_view(action="allimages"),name="allimages"),
    url(r'^allvideos$',views.FileListView.as_view(action="allvideos"),name="allvideos"),
]
