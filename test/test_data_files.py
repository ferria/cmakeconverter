#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2017:
#   Matthieu Estrada, ttamalfor@gmail.com
#
# This file is part of (CMakeConverter).
#
# (CMakeConverter) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# (CMakeConverter) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with (CMakeConverter).  If not, see <http://www.gnu.org/licenses/>.

import unittest2
import lxml
import _io

from cmake_converter.data_files import get_vcxproj_data, get_cmake_lists
from cmake_converter.data_files import get_propertygroup, get_definitiongroup


class TestDataFiles(unittest2.TestCase):
    """
        This file test 'data_files' functions
    """

    vs_project = 'test/project_test.vcxproj'

    def test_get_vcxproj_data(self):
        """Get VS Project Data"""

        under_test = get_vcxproj_data(self.vs_project)

        self.assertTrue('ns' in under_test)
        self.assertEqual(
            {'ns': 'http://schemas.microsoft.com/developer/msbuild/2003'},
            under_test['ns']
        )
        self.assertTrue('tree' in under_test)
        self.assertIsInstance(under_test['tree'], lxml.etree._ElementTree)

    def test_get_propertygroup(self):
        """Get Property Group"""

        under_test = get_propertygroup('debug', 'x86')
        self.assertTrue('PropertyGroup' in under_test)

        self.assertTrue('Debug' in under_test)
        self.assertTrue('Win32' in under_test)

        under_test = get_propertygroup('debug', 'x64')

        self.assertTrue('Debug' in under_test)
        self.assertTrue('x64' in under_test)

        under_test = get_propertygroup('release', 'x86')

        self.assertTrue('Release' in under_test)
        self.assertTrue('Win32' in under_test)

        under_test = get_propertygroup('release', 'x64')

        self.assertTrue('Release' in under_test)
        self.assertTrue('x64' in under_test)

    def test_get_definitiongroup(self):
        """Get Definition Group"""

        under_test = get_definitiongroup('debug', 'x86')
        self.assertTrue('ItemDefinitionGroup' in under_test)

        self.assertTrue('Debug' in under_test)
        self.assertTrue('Win32' in under_test)

        under_test = get_definitiongroup('debug', 'x64')

        self.assertTrue('Debug' in under_test)
        self.assertTrue('x64' in under_test)

        under_test = get_definitiongroup('release', 'x86')

        self.assertTrue('Release' in under_test)
        self.assertTrue('Win32' in under_test)

        under_test = get_definitiongroup('release', 'x64')

        self.assertTrue('Release' in under_test)
        self.assertTrue('x64' in under_test)

    def test_get_cmakelists(self):
        """Get CMakeLists.txt"""

        under_test = get_cmake_lists('./')

        self.assertTrue(under_test)
        self.assertIsInstance(under_test, _io.TextIOWrapper)
