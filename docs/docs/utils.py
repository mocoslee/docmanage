#coding:utf-8


class PopMessage(object):

    def __init__(self,message,style='info'):
        
        self.body = message
        self.style = style

    def css_class(self):

        return self.style
