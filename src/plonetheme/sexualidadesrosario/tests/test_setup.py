# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.sexualidadesrosario.testing import PLONETHEME_SEXUALIDADESROSARIO_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.sexualidadesrosario is properly installed."""

    layer = PLONETHEME_SEXUALIDADESROSARIO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.sexualidadesrosario is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.sexualidadesrosario'))

    def test_browserlayer(self):
        """Test that IPlonethemeSexualidadesrosarioLayer is registered."""
        from plonetheme.sexualidadesrosario.interfaces import (
            IPlonethemeSexualidadesrosarioLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeSexualidadesrosarioLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_SEXUALIDADESROSARIO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.sexualidadesrosario'])

    def test_product_uninstalled(self):
        """Test if plonetheme.sexualidadesrosario is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.sexualidadesrosario'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeSexualidadesrosarioLayer is removed."""
        from plonetheme.sexualidadesrosario.interfaces import IPlonethemeSexualidadesrosarioLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeSexualidadesrosarioLayer, utils.registered_layers())
