## Background

[Cisco's DNA Center](https://www.cisco.com/c/en/us/products/cloud-systems-management/dna-center/index.html) is a centralized network control and management dashboard for Cisco DNA, an intent-based networking solution.

This project provides a sample PHP application and client libraries to access the Center as a Platform REST APIs for the [Python](https://www.python.org) language. The included sample application performs the following functions:

* Authenticates with DNA Center
* Retrieves a count of the number of networking devices listed in the inventory
* Displays a high level summary of the networkings devices listed in the inventory

By default the sample application has disabled SSL certificate checking when connecting to DNA Center, but this can be re-enabled if desired.

## Requirements

The following package must be installed prior to running the sample application:

Python 3.4+

## Setup

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

## Run

The sample test program can be run using the following command

```
./test_python.py -i <ipaddress> -u <username> network
```