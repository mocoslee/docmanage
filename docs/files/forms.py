
from django import forms
from django.utils.translation import ugettext_lazy as _

CHOICE = ((_(u"同组共享"),1),(_(u"个人私有"),0))


class Folder(forms.Form):
    
    fdname = forms.CharField(label=_(u''))
    is_owner = forms.CharField(label=_(u''),widget=forms.Select(choices=CHOICE))

