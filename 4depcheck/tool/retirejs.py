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


# Run Retire.js
def run_retirejs(path):
    # Run retire.js for Javascript libraries
    js_raw_json_output = json.loads(_execute_retirejs(path, "-j"))
    js_vuln_report = _generate_report(js_raw_json_output, "js")

    # Run retire.js for Node.js libraries
    nodejs_raw_json_output = json.loads(_execute_retirejs(path, "-n"))
    nodejs_vuln_report = _generate_report(nodejs_raw_json_output, "nodejs")

    # Return
    return js_vuln_report + nodejs_vuln_report


# -- Private methods

# Execute subprocess with retirejs
def _execute_retirejs(path, type):
    return subprocess.check_output(["retire", "--exitwith", "0",
                                              "--outputformat", "json",
                                              "--path", path,
                                              type],
                                              stderr=subprocess.STDOUT).decode("utf-8")


# Prepare output
def _generate_report(raw_json, type):
    output = []
    for vul_product in raw_json:
        if vul_product["results"] is not None:
            for result in vul_product["results"]:
                product = result["component"]
                version = result["version"]
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
                                output.append(o)
                    except KeyError:
                        pass
    return output
