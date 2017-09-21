#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.dom.minidom
import collections


def getRootElement(xmlfilename):
    return xml.dom.minidom.parse(xmlfilename).documentElement


def getChildElement(parent, tag, attr={"": ""}):
    es = []
    for e in parent.childNodes:
        if e.nodeName == tag:
            for k, v in attr.items():
                if e.getAttribute(k) == v:
                    es.append(e)
    return es


def getChildData(parent, tag):
    e = getChildElement(parent, tag)
    if e:
        return e[0].childNodes[0].data
    else:
        return None


root = getRootElement("domain-registry.xml")
domain = getChildElement(parent=root, tag="domain")[0]

print "DOMAIN_DIR:", domain.getAttribute("location")
# print "----------------------------------------"

root = getRootElement("registry.xml")
host = getChildElement(parent=root, tag="host")[0]
product = getChildElement(parent=host, tag="product")[0]
release = getChildElement(parent=product, tag="release")[0]
version = ".".join([release.getAttribute("level"), release.getAttribute(
    "ServicePackLevel"), release.getAttribute("PatchLevel")])
print "WEBLOGIC_VERSION:", version

e = getChildElement(parent=release, tag="component", attr={"name": "WebLogic Server"})[0]
installdir = e.getAttribute("InstallDir")
print "WEBLOGIC_INSTALL_DIR:", installdir
# print "----------------------------------------"

root = getRootElement("config.xml")
domain_name = getChildData(parent=root, tag="name")
print "DOMAIN_NAME:", domain_name
servers = getChildElement(parent=root, tag="server")
for s in servers:
    server = collections.OrderedDict()
    server["name"] = getChildData(parent=s, tag="name")
    server["machine"] = getChildData(parent=s, tag="machine")
    server["port"] = getChildData(parent=s, tag="listen-port")
    server["cluster"] = getChildData(parent=s, tag="cluster")
    print "SERVER:"
    for k, v in server.items():
        if v:
            print k, "-->", v
