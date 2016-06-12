# -*- coding: utf-8 -*-
#
# Copyright 2015, Jianing Yang
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# Author: Jianing Yang <jianingy.yang@gmail.com>
#
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _

#from coreops.nav import nav_manager
from . import views



urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^welcome/$', login_required(views.Welcome.as_view()), name='welcome'),
    url(r'^vpninfo/$', login_required(views.VpnInfo.as_view()), name='vpninfo'),
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]

#nav_manager.add_sidebar_item(_(u'欢迎使用'),reverse_lazy('coreops_user:welcome'))
#nav_manager.add_sidebar_item(_(u'VPN指南'),reverse_lazy('coreops_user:vpninfo'))
#nav_manager.add_sidebar_item(_(u'密码修改'),reverse_lazy('coreops_user:profile'))
