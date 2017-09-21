#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.dom.minidom


def getElementByName(element, tag, name):
    return [e for e in element.getElementsByTagName(tag) if e.getAttribute("name") == name]

root_element = xml.dom.minidom.parse("domain-registry.xml").documentElement
domain = root_element.getElementsByTagName("domain")[0]

print "DOMAIN_DIR:", domain.getAttribute("location")
print "----------------------------------------"

root_element = xml.dom.minidom.parse("registry.xml").documentElement
product = root_element.getElementsByTagName("product")[0]
release = product.getElementsByTagName("release")[0]
version = ".".join([release.getAttribute("level"), release.getAttribute(
    "ServicePackLevel"), release.getAttribute("PatchLevel")])
print "WEBLOGIC_VERSION:", version

e = getElementByName(element=release, tag="component", name="WebLogic Server")
installdir = e[0].getAttribute("InstallDir")
print "WEBLOGIC_INSTALL_DIR:", installdir
