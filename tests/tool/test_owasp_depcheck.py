#
# Licensed to 4depcheck under one or more contributor
# license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright
# ownership. 4depcheck licenses this file to you under
# the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import unittest
from tool.owasp_depcheck import _get_type


# -- Test suite

class OwaspDepCheckTestSuite(unittest.TestCase):

    def test_get_type_java(self):
        self.assertEqual(_get_type('dependency.jar'), 'java')

    def test_get_type_js(self):
        self.assertEqual(_get_type('dependency.js'), 'js')

    def test_get_type_python(self):
        self.assertEqual(_get_type('dependency.py'), 'python')

    def test_get_type_ruby(self):
        self.assertEqual(_get_type('dependency.rb'), 'ruby')

    def test_get_type_php(self):
        self.assertEqual(_get_type('dependency.php'), 'php')

    def test_get_type_unknown(self):
        self.assertEqual(_get_type('dependency.exe'), 'unknown')
