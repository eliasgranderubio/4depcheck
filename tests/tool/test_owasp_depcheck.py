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
import json
from tool.owasp_depcheck import _get_type
from tool.owasp_depcheck import _generate_report


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

    def test_generate_report(self):
        with open('./tests/mock_files/dependency-check-report.json', 'r') as report_file:
            raw_json = json.loads(''.join(report_file.readlines()))
        self.assertEqual(_generate_report(raw_json), json.loads(mock_owasp_dep_check_generated_repo))


# -- Mock Constants

mock_owasp_dep_check_generated_repo='[{"cve_product_version": "2.7.1", "cve_id": "CVE-2014-0107", "cve_product": "xalan-java", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-1999-0428", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2007-5536", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2009-0590", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2013-0169", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2014-0160", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0207", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0208", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0209", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0285", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0286", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0287", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0288", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0289", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0290", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0291", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-0293", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1787", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1788", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1789", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1790", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1791", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1792", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-1794", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-3193", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-3194", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-3195", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-3197", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2015-4000", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0701", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0702", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0703", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0704", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0705", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0797", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0798", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0799", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-0800", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2105", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2106", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2107", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2108", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2109", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2176", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2177", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2178", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2179", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2180", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2181", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2182", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-2842", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-6302", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-6303", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-6304", "cve_product": "openssl", "cve_type": "java", "cve_severity": "high"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-6306", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-7055", "cve_product": "openssl", "cve_type": "java", "cve_severity": "low"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2016-8610", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2017-3731", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2017-3732", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2017-3735", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.0.2", "cve_id": "CVE-2017-3736", "cve_product": "openssl", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "0.8.0", "cve_id": "CVE-2016-2166", "cve_product": "qpid_proton", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "0.8.0", "cve_id": "CVE-2016-4467", "cve_product": "qpid_proton", "cve_type": "java", "cve_severity": "medium"}, {"cve_product_version": "1.8.3", "cve_id": "CVE-2015-6748", "cve_product": "jsoup", "cve_type": "java", "cve_severity": "medium"}]'