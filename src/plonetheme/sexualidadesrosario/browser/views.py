# -*- coding: utf-8 -*-
from plone.app.contenttypes.behaviors.leadimage import ILeadImage
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class FolderLeadImages(BrowserView):
    """ 
    """

    @property
    def images(self):
        images = []
        for i in self.context.listFolderContents():
            try:
                ob = ILeadImage(i)
            except TypeError:
                continue
            if ob.image:
                images.append(ob)
        return images
