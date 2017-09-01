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

import argparse
import sys
import os


class DepCheckCLIParser:

    # -- Public methods

    # DepCheckCLIParser Constructor
    def __init__(self):
        super(DepCheckCLIParser, self).__init__()
        self.parser = argparse.ArgumentParser(prog='4depcheck.py')
        self.parser.add_argument('project_name', metavar='PROJECT_NAME', type=str,
                                 help='Project name for this analysis')
        self.parser.add_argument('dir', metavar='PATH_TO_SCAN', type=str, help='The path to scan')
        self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
        self.args, self.unknown = self.parser.parse_known_args(sys.argv)
        # Verify command line arguments
        status = self.verify_args(self.args)
        if status != 0:
            exit(status)

    # -- Getters

    # Gets project name
    def get_project_name(self):
        return self.args.project_name

    # Gets dir
    def get_dir(self):
        return self.args.dir

    # -- Static methods

    # Verify command line arguments
    @staticmethod
    def verify_args(args):
        if not os.path.isdir(args.dir):
            print('[ERROR] The path argument is not valid.')
            return 1
        return 0
