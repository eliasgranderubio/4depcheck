# 4depcheck
[![Python](https://img.shields.io/badge/python-3.5%2C%203.6-blue.svg)](https://github.com/eliasgranderubio/4depcheck)
[![Docker Pulls](https://img.shields.io/docker/pulls/3grander/4depcheck.svg)](https://hub.docker.com/r/3grander/4depcheck/)
[![License](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/eliasgranderubio/4depcheck)

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
    $ docker run -v /tmp/4depcheck:/tmp/4depcheck \
                 -v $ABSOLUTE_PATH_TO_YOUR_PROJECT:$ABSOLUTE_PATH_TO_YOUR_PROJECT \
                 3grander/4depcheck:0.1.0 $PROJECT_NAME $ABSOLUTE_PATH_TO_YOUR_PROJECT
```
If you has not set the environment variables, you only need replace the variables in the previous docker command as you need.

The expected output for the previous query will be shown in the stdout and it will be stored in `/tmp/4depcheck/$PROJECT_NAME.json`. An example for this output is shown below:

```
    [{   
        "cve_severity": "medium",
        "cve_product": "cxf",
        "cve_product_version": "3.1.6",
        "cve_id": "CVE-2017-3156",
        "cve_type": "java",
        "cve_product_file_path": "/opt/modules/system/org/apache/cxf/main/cxf-core-3.1.6.jar"
    }, {     
        "cve_severity": "high",
        "cve_product": "netty",
        "cve_product_version": "4.0.33",
        "cve_id": "CVE-2016-4970",
        "cve_type": "java",
        "cve_product_file_path": "/opt/modules/system/io/netty/main/netty-all-4.0.33.Final.jar"
    }, {
        "cve_severity": "high",
        "cve_product": "xalan-java", 
        "cve_product_version": "2.7.1", 
        "cve_id": "CVE-2014-0107",
        "cve_type": "java", 
        "cve_product_file_path": "/usr/plugins/xslt-debugger/lib/rt/xalan.jar"
    }, {
        "cve_severity": "high",
        "cve_product": "xalan-java",
        "cve_product_version": "2.7.1",
        "cve_id": "CVE-2014-0107",
        "cve_type": "java",
        "cve_product_file_path": "/usr/plugins/xslt-debugger/lib/rt/serializer.jar" 
    }, {
        "cve_severity": "medium",
        "cve_product": "axis",
        "cve_product_version": "1.4",
        "cve_id": "CVE-2014-3596",
        "cve_type": "java",
        "cve_product_file_path": "/usr/plugins/tasks/lib/axis-1.4.jar"
    }, {
        "cve_severity": "medium",
        "cve_product": "jquery",
        "cve_product_version": "1.4.2",
        "cve_id": "CVE-2011-4969", 
        "cve_type": "js",
        "cve_product_file_path": "/usr/js/jquery-1.4.2/jquery.js"
    }]

```


## Bugs and Feedback
For bugs, questions and discussions please use the [Github Issues](https://github.com/eliasgranderubio/4depcheck/issues) or ping me on Twitter (@3grander).
