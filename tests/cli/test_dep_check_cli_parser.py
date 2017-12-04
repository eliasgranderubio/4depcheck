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

import sys, os
sys.path.insert(1, str(os.path.dirname(os.path.abspath(__file__))) + '/../../4depcheck')
from cli.dep_check_cli_parser import DepCheckCLIParser


# -- Test suite

class DepCheckCLIParserTestSuite(unittest.TestCase):

    def test_check_full_happy_path(self):
        sys.argv = ['4depcheck.py', 'jboss_project', '/tmp']
        parsed_args = DepCheckCLIParser()
        self.assertEqual(parsed_args.get_project_name(), 'jboss_project')
        self.assertEqual(parsed_args.get_dir(), '/tmp')

    def test_check_exit_1(self):
        sys.argv = ['4depcheck.py', 'jboss_project', '/path/to/dir']
        with self.assertRaises(SystemExit) as cm:
            DepCheckCLIParser()
        self.assertEqual(cm.exception.code, 1)

    def test_with_no_dir(self):
        args = generate_args('jboss_project', '/path/to/dir')
        status = DepCheckCLIParser.verify_args(args)
        self.assertEqual(status, 1)


# -- Util methods

def generate_args(project_name, dir):
    return AttrDict([('project_name', project_name), ('dir', dir)])


# -- Util classes

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
