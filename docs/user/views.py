# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.contrib import auth as django_auth
from django.contrib.auth.models import User,Group
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.conf import settings
from docs.utils import PopMessage
from user import forms


class Welcome(View):

    template_name = "user/welcome.html"
    
    def get(self,request):

        message = request.GET.get("message","")
        return render(request,self.template_name,{"message":message})


class VpnInfo(View):

    template_name = "user/vpninfo.html"
    
    def get(self,request):
        
        return render(request,self.template_name,
                {'vpn_address':settings.VPN_ADDRESS})


class LoginView(View):

    form_class = forms.LoginForm
    template_name = 'user/login.html'

    def get(self, req):
        return render(req, 'user/login.html',
                      {'login_form': self.form_class()})

    def post(self, req):
        next_page = req.GET.get('next',reverse('user:welcome'))
        form = self.form_class(req.POST)
        if form.is_valid():
            cred = dict(username=form.cleaned_data['username'],
                        password=form.cleaned_data['password'])
            user = django_auth.authenticate(**cred)
            if user and user.is_active:
                django_auth.login(req, user)
                group = Group.objects.filter(user=user)
                
                req.session['uid'] = user.id
                if len(group)>0:
                    req.session['gid'] = group[0].id
                else:
                    req.session['gid'] = -1
                response = HttpResponseRedirect(next_page)
                response.set_cookie('username',user.username)
                return response
            else:
                form.add_error(None, _(u'用户名或密码错误'))
                form.add_error('username', '')
                form.add_error('password', '')
        else:
            form.add_error(None, _(u'表单错误'))
        return render(req, self.template_name, {'login_form': form})


class LogoutView(View):

    template_name = 'common/message.html'

    def get(self, req):
        django_auth.logout(req)
        renders =  render(req, self.template_name,
                      {'message': PopMessage(_(u'您已成功登出'))})
        renders.delete_cookie('username')
        return renders

