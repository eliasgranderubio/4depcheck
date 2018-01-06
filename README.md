# 4depcheck
[![Build Status](https://travis-ci.org/eliasgranderubio/4depcheck.svg?branch=master)](https://travis-ci.org/eliasgranderubio/4depcheck)
[![Coverage Status](https://coveralls.io/repos/github/eliasgranderubio/4depcheck/badge.svg?branch=master)](https://coveralls.io/github/eliasgranderubio/4depcheck?branch=master)
[![Python](https://img.shields.io/badge/python-3.3%2C%203.4%2C%203.5%2C%203.6-blue.svg)](https://github.com/eliasgranderubio/4depcheck)
[![Docker Pulls](https://img.shields.io/docker/pulls/3grander/4depcheck.svg)](https://hub.docker.com/r/3grander/4depcheck/)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/eliasgranderubio/4depcheck)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Feliasgranderubio%2F4depcheck.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Feliasgranderubio%2F4depcheck?ref=badge_shield)

**4depcheck** is a tool to analyze and detect vulnerable dependencies/libraries from different programming languages thanks to:
   * [OWASP dependency check](https://github.com/jeremylong/DependencyCheck)
   * [Retire.js](https://github.com/retirejs/retire.js/)


## Requirements

Before **4depcheck** usage, you must have installed the next requirements:

* Docker

### Installation of Docker

You must have installed Docker for using **4depcheck**. If you need instructions for Docker installation, see the [How-to install Docker](https://docs.docker.com/engine/getstarted/step_one/) page.

In order to avoid having to use `sudo` when you use the `docker` command, create a Unix group called `docker` and add users to it. When the `docker` daemon starts, it makes the ownership of the Unix socket read/writable by the `docker` group.

## Usage

For **4depcheck** usage, you can set the next environment variables as you need:
```
    export PROJECT_NAME='project_to_analyze'
    export ABSOLUTE_PATH_TO_YOUR_PROJECT='/home/user/project_to_analyze'
```

If you has set the previous environment variables, you only need run the next docker command:
```
    $ docker run -v /tmp/4depcheck:/tmp/4depcheck 
                 -v $ABSOLUTE_PATH_TO_YOUR_PROJECT:$ABSOLUTE_PATH_TO_YOUR_PROJECT 
                 3grander/4depcheck:0.1.0 $PROJECT_NAME $ABSOLUTE_PATH_TO_YOUR_PROJECT
```
If you has not set the environment variables, you only need replace the variables in the previous docker command as you need.

The expected output for the previous query will be shown in the stdout and it will be stored in `/tmp/4depcheck/$PROJECT_NAME.json`. An example for this output is shown below:

```
    [{
        "cve_severity": "medium",
        "cve_product": "batik",
        "cve_product_version": "1.7",
        "cve_id": "CVE-2015-0250",
        "cve_type": "java"
    }, {
        "cve_severity": "high",
        "cve_product": "batik",
        "cve_product_version": "1.7",
        "cve_id": "CVE-2017-5662",
        "cve_type": "java"
    }, {
        "cve_severity": "medium",
        "cve_product": "xstream",
        "cve_product_version": "1.4.8",
        "cve_id": "CVE-2016-3674",
        "cve_type": "java"
    }, {
        "cve_severity": "medium",
        "cve_product": "xstream",
        "cve_product_version": "1.4.8",
        "cve_id": "CVE-2017-7957",
        "cve_type": "java"
    }, {
        "cve_severity": "medium",
        "cve_product": "axis",
        "cve_product_version": "1.4",
        "cve_id": "CVE-2014-3596",
        "cve_type": "java"
    }, {
        "cve_severity": "medium",
        "cve_product": "jquery",
        "cve_product_version": "1.4.2",
        "cve_id": "CVE-2011-4969", 
        "cve_type": "js"
    }]

```


## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/4depcheck/issues) or ping me on Twitter (@3grander).
