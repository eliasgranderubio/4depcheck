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

import json
import unittest
from unittest.mock import patch

from tool.open_source.retirejs import RetireJS


# -- Test suite

class RetireJSTestSuite(unittest.TestCase):

    def test_generate_report(self):
        self.assertEqual(RetireJS('')._generate_report(json.loads(mock_retirejs_output), 'js'), json.loads(mock_generated_report))

    @patch('subprocess.check_output', return_value='[]'.encode('utf-8'))
    def test_run_retirejs(self, m1):
        self.assertEqual(RetireJS('').run_retirejs(),[])

# -- Mock Constants

mock_retirejs_output = '[{"file":"jquery-migrate.js","results":[{"version":"1.1.1","component":"jquery-migrate","detection":"filecontent","vulnerabilities":[{"info":["http://blog.jquery.com/2013/05/01/jquery-migrate-1-2-0-released/"],"severity":"medium","identifiers":{"release":"jQuery Migrate 1.2.0 Released","summary":"cross-site-scripting"}},{"info":["http://bugs.jquery.com/ticket/11290","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"bug":"11290","summary":"Selector interpreted as HTML"}}]}]},{"file":"jquery-migrate.min.js","results":[{"version":"1.1.1","component":"jquery-migrate","detection":"filecontent","vulnerabilities":[{"info":["http://blog.jquery.com/2013/05/01/jquery-migrate-1-2-0-released/"],"severity":"medium","identifiers":{"release":"jQuery Migrate 1.2.0 Released","summary":"cross-site-scripting"}},{"info":["http://bugs.jquery.com/ticket/11290","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"bug":"11290","summary":"Selector interpreted as HTML"}}]}]},{"file":"jquery.js","results":[{"version":"1.10.1","component":"jquery","detection":"filecontent","vulnerabilities":[{"info":["https://github.com/jquery/jquery/issues/2432","http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"2432","summary":"3rd party CORS request may execute"}},{"info":["https://bugs.jquery.com/ticket/11974","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"11974","summary":"parseHTML() executes scripts in event handlers"}}]}]},{"file":"jquery.min.js","results":[{"version":"1.10.1","component":"jquery","detection":"filecontent","vulnerabilities":[{"info":["https://github.com/jquery/jquery/issues/2432","http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"2432","summary":"3rd party CORS request may execute"}},{"info":["https://bugs.jquery.com/ticket/11974","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"11974","summary":"parseHTML() executes scripts in event handlers"}}]}]},{"file":"speed/jquery-basis.js","results":[{"version":"1.4.2","component":"jquery","detection":"filecontent","vulnerabilities":[{"info":["http://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2011-4969","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"CVE":["CVE-2011-4969"]}},{"info":["http://bugs.jquery.com/ticket/11290","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"bug":"11290","summary":"Selector interpreted as HTML"}},{"info":["https://github.com/jquery/jquery/issues/2432","http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"2432","summary":"3rd party CORS request may execute"}}]}]},{"file":"test/data/jquery-1.9.1.ajax_xhr.min.js","results":[{"version":"1.9.1.ajax_xhr.min","component":"jquery","detection":"filename","vulnerabilities":[{"info":["https://github.com/jquery/jquery/issues/2432","http://blog.jquery.com/2016/01/08/jquery-2-2-and-1-12-released/","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"2432","summary":"3rd party CORS request may execute"}},{"info":["https://bugs.jquery.com/ticket/11974","http://research.insecurelabs.org/jquery/test/"],"severity":"medium","identifiers":{"issue":"11974","summary":"parseHTML() executes scripts in event handlers"}}]}]}]'

mock_generated_report = '[{"cve_id": "CVE-2011-4969", "cve_type": "js", "cve_product": "jquery", "cve_product_version": "1.4.2", "cve_severity": "medium", "cve_product_file_path": "speed/jquery-basis.js"}]'