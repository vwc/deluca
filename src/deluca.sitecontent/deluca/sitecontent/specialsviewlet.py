from five import grok
from Acquisition import aq_inner
from zope.component import getMultiAdapter
from plone.app.layout.viewlets.interfaces import IPortalHeader
from Products.CMFCore.interfaces import IContentish
from plone.app.layout.navigation.navtree import buildFolderTree
from plone.app.layout.navigation.root import getNavigationRoot
from Products.CMFPlone.browser.navtree import DefaultNavtreeStrategy


class SpecialsViewlet(grok.Viewlet):
    grok.name('deluca.sitecontent.SpecialsViewlet')
    grok.context(IContentish)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    def update(self):
        context = aq_inner(self.context)
        context_url = context.absolute_url()
