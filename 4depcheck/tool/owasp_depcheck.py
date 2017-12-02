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
import tempfile
import subprocess


# Run OWASP DepCheck
def run_owasp_depcheck(path):
    # Run OWASP DepCheck
    subprocess.call(["dependency-check.sh",
                     "--cveValidForHours", "24",
                     "-f", "JSON",
                     "--disableAssembly",
                     "--bundleAudit", "/usr/bin/bundler-audit",
                     "--data", tempfile.gettempdir() + "/4depcheck/dependency-check/data",
                     "--enableExperimental", "--project", '"test"',
                     "-s", path,
                     "--out", tempfile.gettempdir()],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL)

    # Read and parse the OWASP DepCheck report
    vuln_report = _read_report()

    # Return
    return vuln_report


# -- Private methods

# Read and parse the OWASP DepCheck report
def _read_report():
    raw_json = {}
    # Read OWASP DepCheck json report
    with open(tempfile.gettempdir() + '/dependency-check-report.json', 'r') as report_file:
        raw_json = json.loads(''.join(report_file.readlines()))

    # Parse json
    return _generate_report(raw_json)


# Prepare output
def _generate_report(raw_json):
    output = []
    if 'dependencies' in raw_json:
        for dependency in raw_json['dependencies']:
            if 'vulnerabilities' in dependency:
                for vulnerability in dependency['vulnerabilities']:
                    if 'name' in vulnerability and vulnerability['name'].startswith('CVE-') and \
                       'identifiers' in dependency:
                        for identifier in dependency['identifiers']:
                            if identifier['type'] == 'cpe' and identifier['confidence'] != 'LOW':
                                splitted_package = identifier['name'].split(":")
                                if len(splitted_package) > 4:
                                    d = {}
                                    d["cve_id"] = vulnerability['name']
                                    d["cve_type"] = _get_type(dependency['fileName'])
                                    d["cve_severity"] = vulnerability['severity'].lower()
                                    d["cve_product"] = splitted_package[3]
                                    d["cve_product_version"] = splitted_package[4]
                                    output.append(d)
    return output


# Get type based on filename
def _get_type(filename):
    if filename.endswith('.jar') or filename.endswith('.war'):
        return 'java'
    elif filename.endswith('.py') or filename.endswith('.whl') or filename.endswith('.egg'):
        return 'python'
    elif filename.endswith('.js'):
        return 'js'
    elif filename.endswith('.rb') or filename.endswith('Rakefile') or filename.endswith('.gemspec'):
        return 'ruby'
    elif filename.endswith('.php'):
        return 'php'
    else:
        return 'unknown'
