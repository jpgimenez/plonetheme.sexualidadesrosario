# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.sexualidadesrosario


class PlonethemeSexualidadesrosarioLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plonetheme.sexualidadesrosario)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.sexualidadesrosario:default')


PLONETHEME_SEXUALIDADESROSARIO_FIXTURE = PlonethemeSexualidadesrosarioLayer()


PLONETHEME_SEXUALIDADESROSARIO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_SEXUALIDADESROSARIO_FIXTURE,),
    name='PlonethemeSexualidadesrosarioLayer:IntegrationTesting'
)


PLONETHEME_SEXUALIDADESROSARIO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_SEXUALIDADESROSARIO_FIXTURE,),
    name='PlonethemeSexualidadesrosarioLayer:FunctionalTesting'
)


PLONETHEME_SEXUALIDADESROSARIO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_SEXUALIDADESROSARIO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeSexualidadesrosarioLayer:AcceptanceTesting'
)
