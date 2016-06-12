# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.conf import settings
from files.models import UserDir,UserFile
import os
# Create your views here.


def groupcheck(func):
    
    def wrapped(cls,request):
        if request.session.get("gid")==-1:
            message = _(u"请先划定分组")
            redirect = "%s?message=%s" % (reverse("user:welcome"),message)
            return HttpResponseRedirect(redirect)
        else:
            return func(cls,request) 

    return wrapped

class UploadView(View):

    def get(self,request):

        return render(request,'files/upload.html')

    def post(self,request):

        for files in request.FILES.keys():
            with open(request.FILES[files].name,"wb") as fd:
                for line in request.FILES[files].readlines():
                    fd.write(line)

        return HttpResponse("ok")

class FileListView(View):

    action = ""
    flist = ("pdf","xls","csv","txt","doc","docx","ppt","pptx","iso","rar","zip","html","exe")
    imglist = ("bmp","gif","pic","png","tif","jpeg")
    vlist = ("mp4","kvm","avi","mov","mpg","swf")

    @groupcheck
    def get(self,request):

        if self.action=="allfiles":
            return self.all_files(request)
        elif self.action=="allimages":
            return self.all_images(request)
        elif self.action=="allvideos":
            return self.all_videos(request)
        else:
            return self.gdefault(request)

    def gdefault(self,request):
        
        did = request.GET.get("did","0")
        if did==0:
            dirs = UserDir.objects.filter(parentid=0)
            files = []
        else:
            dirs = UserDir.objects.filter(parentid=did)
            files = UserFile.objects.filter(did=did)

        try:
            node = UserDir.objects.get(pk=did)
            pid = node.parentid
        except Exception:
            pid = 0

        return render(request,"files/filelist.html",{"dirs":dirs,"files":files,"did":did,"pid":pid})

    def all_files(self,request):
        
        files = UserFile.objects.filter(ftype__in=self.flist)
        return render(request,"files/filelist.html",{"dirs":[],"files":files,"did":"0","pid":0})

    def all_videos(self,request):
        
        files = UserFile.objects.filter(ftype__in=self.vlist)
        return render(request,"files/filelist.html",{"dirs":[],"files":files,"did":"0","pid":0})

    def all_images(self,request):
        
        files = UserFile.objects.filter(ftype__in=self.imglist)
        return render(request,"files/filelist.html",{"dirs":[],"files":files,"did":"0","pid":0})

    def post(self,request):

        if self.action=="add_dir":
            return self.add_dir(request)
        else:
            return self.default(request)

    def default(self,request):

        return HttpResponse("ok")

    def add_dir(self,request):
        
        did = request.POST.get("did",0)      
        fname = request.POST.get("fname")
        d = UserDir(name=fname,parentid=did,uid=request.session.get('uid'),\
            gid=request.session.get("gid"))
        d.save()
        pdir = []
        try:
            t_dir = UserDir.objects.get(pk=did)
        except Exception:
            t_dir = None
        while t_dir:
            pdir.append(t_dir.name)
            try:
                t_dir = User.objects.get(pk=t_dir.parentid)
            except Exception:
                break

        pdir.reverse()
        new_dir = "%s/%s/%s" % (settings.ROOT_DIR,"/".join(pdir),fname)
        os.makedirs(new_dir)

        return redirect("%s?did=%s" % (reverse("files:filelist"),did))

