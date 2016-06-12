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
from django import forms
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(label=_(u'用户名'))
    password = forms.CharField(label=_(u'密码'),widget=forms.PasswordInput(render_value=False))



class Register(forms.Form):
    mail_show = u'邮箱'
    username = forms.EmailField(label=_(mail_show),required=True)


class PasswdForm(forms.Form):
    #_widget = forms.TextInput(attrs={'class': 'textInput'})
    #email = forms.CharField(widget=_widget)
    #first_name = forms.CharField(widget=_widget)
    #last_name = forms.CharField(widget=_widget)
    # do not use password here since password, as a native field in
    # User Model, has certain encoding algorithm that a raw password
    # string wont fit. Therefore, we use password1 to get a raw
    # password and use set_password of User model to save it later
    username = forms.CharField(widget=forms.HiddenInput())
    password1 = forms.CharField(label=_(u'密码'),widget=forms.PasswordInput(),required=False)
    password2 = forms.CharField(label=_(u'确认密码'),
                                widget=forms.PasswordInput(),
                                required=False)

    def clean(self):
        cleaned_data = super(PasswdForm, self).clean()
        password1 = cleaned_data.get('password1', '')
        password2 = cleaned_data.get('password2', '')
        if password1 != password2:
            raise forms.ValidationError(_(u'两次输入密码不一致'))
        return cleaned_data



class PasswordChangeForm(forms.Form):
    password = forms.CharField(initial='',
                               label=_(u'原密码'),
                               widget=forms.PasswordInput(),
                               required=False)
    new1 = forms.CharField(label=_(u'新密码'),
                           widget=forms.PasswordInput(),
                           required=False)
    new2 = forms.CharField(label=_(u'确认密码'),
                           widget=forms.PasswordInput(),
                           required=False)
    def clean(self):
        cleaned_data = super(PasswordChangeForm, self).clean()
        password = cleaned_data.get('password', '')
        new1 = cleaned_data.get('new1', '')
        new2 = cleaned_data.get('new2', '')
        if new1 != new2:
            raise forms.ValidationError(_(u'两次输入密码不一致'))
        return cleaned_data
