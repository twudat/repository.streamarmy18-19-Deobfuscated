import requests
import re
import xbmc
import xbmcgui
import time
from random import randint
dialog = xbmcgui.Dialog()
ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
      'AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/65.0.3325.181 Safari/537.36')


class Scraper:
    def __init__(self):
        self.Base = 'https://pastebin.com/raw/y8nYuUPP'
        self.Search = ('/%s-watch-online/')
        self.links = []

    def Index(self, type, term, year, imdb, torrents):
        if type == 'TV':
            pass
        else:
            try:
                link = requests.get(self.Base, headers={
                                    "User-Agent": ua}).content
                matches = re.findall('<list>(.*?)</list>',
                                     link, flags=re.DOTALL)
                for content in matches:
                    if '<movies>' in content:
                        checkurl = re.findall(
                            '<movies>(.*?)</movies>', content, flags=re.DOTALL)
                        for links in checkurl:
                            searchcontent = requests.get(
                                links, headers={"User-Agent": ua}).content
                            lists = re.findall(
                                '<content>(.*?)</content>', searchcontent, flags=re.DOTALL)
                            for expand in lists:
                                if term.lower() in expand.lower():
                                    title = re.findall(
                                        '<title>(.*?)</title>', expand, flags=re.DOTALL)[0]
                                    link = re.findall(
                                        '<link>(.*?)</link>', expand, flags=re.DOTALL)
                                    if link > 1:
                                        for links in link:
                                            if 'trailer' in links.lower():
                                                continue
                                            if 'uhd' in title.lower():
                                                name = 'NemesisAio ( Debrid ) | 4K UHD | ' + title
                                                quality = '0'
                                            elif '4k' in title.lower():
                                                name = 'NemesisAio ( Debrid ) | 4K UHD | ' + title
                                                quality = '0'
                                            elif '1080' in title.lower():
                                                name = 'NemesisAio ( Debrid ) | FHD | ' + title
                                                quality = '6'
                                            elif '720' in title.lower():
                                                name = 'NemesisAio ( Debrid ) | HD | ' + title
                                                quality = '7'
                                            else:
                                                name = 'NemesisAio ( Debrid ) | SD | ' + title
                                                quality = '8'
                                            self.links.append(
                                                {'title': name, 'url': links, 'quality': quality, 'Debrid': True, 'Direct': False})
                                    else:
                                        if 'trailer' in link.lower():
                                            continue
                                        if 'uhd' in title.lower():
                                            name = 'NemesisAio ( Debrid ) | 4K | ' + title
                                            quality = '0'
                                        elif '4k' in title.lower():
                                            name = 'NemesisAio ( Debrid ) | 4K | ' + title
                                            quality = '0'
                                        elif '1080' in title.lower():
                                            name = 'NemesisAio ( Debrid ) | FHD | ' + title
                                            quality = '6'
                                        elif '720' in title.lower():
                                            name = 'NemesisAio ( Debrid ) | HD | ' + title
                                            quality = '7'
                                        else:
                                            name = 'NemesisAio ( Debrid ) | SD | ' + title
                                            quality = '8'
                                        self.links.append(
                                            {'title': name, 'url': links, 'quality': quality, 'Debrid': True, 'Direct': False})
                return self.links
            except Exception as c:
                xbmc.log("ERROR ::: %s" % c, level=xbmc.LOGNOTICE)
