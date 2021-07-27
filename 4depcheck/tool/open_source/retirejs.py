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
import subprocess


class RetireJS:

    # RetireJS Constructor
    def __init__(self, path):
        super(RetireJS, self).__init__()
        self.path = path

    # Run Retire.js
    def run_retirejs(self):
        # Run retire.js for Javascript libraries
        js_raw_json_output = json.loads(self._execute_retirejs("-j"))
        js_vuln_report = self._generate_report(js_raw_json_output, "js")

        # Run npm audit for NPM packages
        # TODO egrande: Add "npm audit --json --audit-level=none". It will be necessary to update the base image
        #               in the Dockerfile because, at this moment, the npm version is 3.10.3

        # Return
        return js_vuln_report

    # -- Private methods

    # Execute subprocess with retirejs
    def _execute_retirejs(self, type):
        return subprocess.check_output(["retire", "--exitwith", "0",
                                                  "--outputformat", "json",
                                                  "--path", self.path,
                                                  type],
                                                  stderr=subprocess.STDOUT).decode("utf-8")

    # Prepare output
    @staticmethod
    def _generate_report(raw_json, type):
        output = []
        if 'data' in raw_json:
            for vul_product in raw_json['data']:
                if vul_product["results"] is not None and "file" in vul_product and vul_product["file"] is not None:
                    file_path = vul_product["file"]
                    for result in vul_product["results"]:
                        product = result["component"]
                        version = result["version"]
                        if "vulnerabilities" in result:
                            for vulnerability in result["vulnerabilities"]:
                                severity = vulnerability["severity"]
                                try:
                                    for cve in vulnerability["identifiers"]["CVE"]:
                                        if 'CVE-XXXX-XXXX' not in cve:
                                            o = {}
                                            o["cve_id"] = cve
                                            o["cve_type"] = type
                                            o["cve_severity"] = severity
                                            o["cve_product"] = product
                                            o["cve_product_version"] = version
                                            o["cve_product_file_path"] = file_path
                                            output.append(o)
                                except KeyError:
                                    pass
        return output
