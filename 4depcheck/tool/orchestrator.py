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

from tool.open_source.owasp_depcheck import OwaspDepCheck
from tool.open_source.retirejs import RetireJS


# Run all tools
def run_tools(path_to_analyze):
    # -- Run all analysis
    retirejs_report = RetireJS(path=path_to_analyze).run_retirejs()
    owasp_depcheck_report = OwaspDepCheck(path=path_to_analyze).run_owasp_depcheck()

    # -- Generate full report and return
    full_report = json.dumps(retirejs_report + owasp_depcheck_report)
    return full_report
