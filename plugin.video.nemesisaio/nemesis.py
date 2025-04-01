#########################################
############ CODE BY @NEMZZY668###########
#########################################
import urllib
import os
import re
import sys
import base64
import json
import time
import requests
import importlib
import whostreams
import updater
import pyxbmct
import six
from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, xbmcvfs
from six.moves.urllib.parse import parse_qs, quote_plus, urlparse, parse_qsl
from six import PY2
from resources.libs.modules import workers
from resources.libs.modules import miniresolver
# from resources.libs.common_addon import Addon
from bs4 import BeautifulSoup
from datetime import datetime
import random
import resolveurl
messagetext = 'https://pastebin.com/raw/6CwvUdHB'
translatePath = xbmc.translatePath if PY2 else xbmcvfs.translatePath
addon_id = 'plugin.video.nemesisaio'
selfAddon = xbmcaddon.Addon(id=addon_id)
AddonTitle = '[COLOR yellow][B]NemesisAio[/B][/COLOR]'
AddonXML = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'addon.xml'))
addonPath = os.path.join(os.path.join(translatePath(
    'special://home'), 'addons'), 'plugin.video.nemesisaio')
fanarts = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'fanart.jpg'))
fanart = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'fanart.jpg'))
icon = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'icon.gif'))
Addonicon = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'icon.gif'))
AddonIcon = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'icon.gif'))
Background_Image = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/background.jpg'))
Listbg = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/listbg.png'))
List_Back = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/list.png'))
FourK = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/4k.png'))
ChatBG = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/chatbg.jpg'))
FHD = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/1080.png'))
HD = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/HD.png'))
SD = translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'images/SD.png'))
dp = xbmcgui.DialogProgress()
dialog = xbmcgui.Dialog()
adultpass = selfAddon.getSetting('password')
chatname = selfAddon.getSetting('chatname')
tmdbapi = '5135334daa33251bc407e5f24cb1c6a5'
youtubeapi = 'AIzaSyBkMDGtGKhPCdFek0kZiN5dy9K2AG0D7zc'
ImgFolder = '/resources/Images/'
finalsources = []
##########################
# IMAGES
##########################
MoviesImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Movies.gif'))
TvShowsImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Tv-Shows.gif'))
SportsImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Sports.gif'))
MusicImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Music.gif'))
CartoonsImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Cartoons.gif'))
KidsImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Kids.gif'))
AnimeImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Anime.gif'))
WebcamsImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Webcams.gif'))
GamingImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Gaming.gif'))
DocImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Documentaries.gif'))
XXXImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'xxx.gif'))
MaintenanceImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Maintenance.gif'))
NextPageImg = translatePath(os.path.join(
    'special://home/addons/' + addon_id + ImgFolder, 'Next-Page.gif'))

user_agent_list = [
    ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
     "Chrome/77.0.3865.90 Safari/537.36"),
    ("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
     "Chrome/79.0.3945.130 Safari/537.36"),
]


def get_headers():
    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random.choice(user_agent_list),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Sec-Ch-Ua": "Microsoft Edge;v=131, Chromium;v=131, Not_A Brand;v=24"
    }
    return headers


def SET_VIEW():
    xbmc_version = xbmc.getInfoLabel("System.BuildVersion")
    version = float(xbmc_version[:4])
    if version >= 11.0 and version <= 11.9:
        codename = 'Eden'
    elif version >= 12.0 and version <= 12.9:
        codename = 'Frodo'
    elif version >= 13.0 and version <= 13.9:
        codename = 'Gotham'
    elif version >= 14.0 and version <= 14.9:
        codename = 'Helix'
    elif version >= 15.0 and version <= 15.9:
        codename = 'Isengard'
    elif version >= 16.0 and version <= 16.9:
        codename = 'Jarvis'
    elif version >= 17.0 and version <= 17.9:
        codename = 'Krypton'
    elif version >= 18.0 and version <= 18.9:
        codename = 'Leia'
    else:
        codename = "Decline"
    if codename == "Jarvis":
        xbmc.executebuiltin('Container.SetViewMode(50)')
    elif codename == "Krypton":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    elif codename == "Leia":
        xbmc.executebuiltin('Container.SetViewMode(55)')
    else:
        xbmc.executebuiltin('Container.SetViewMode(50)')


def showText(heading, text):

    try:
        id = 10147
        xbmc.executebuiltin('ActivateWindow(%d)' % id)
        xbmc.sleep(500)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                xbmc.sleep(10)
                retry -= 1
                win.getControl(1).setLabel(heading)
                win.getControl(5).setText(text)
                quit()
                return
            except:
                pass
    except:
        pass


def popup():

    try:
        message = requests.get(messagetext).text
        if len(message) > 1:
            path = xbmcaddon.Addon().getAddonInfo('path')
            comparefile = os.path.join(os.path.join(path, ''), 'popup.txt')
            r = open(comparefile)
            compfile = r.read()
            if str(len(compfile)) == str(len(message)):
                pass
            else:
                showText(
                    '[B][COLOR pink]NemesisAio Latest News[/B][/COLOR]', message)
                text_file = open(comparefile, "w")
                text_file.write(message)
                text_file.close()
    except:
        pass


popup()


def GetMenu():
    try:
        currentversioncheck = requests.get(
            'https://raw.githubusercontent.com/nemesis668/repository.streamarmy18-19/main/addons.xml').text
        currentversion = re.findall(
            '<addon id="plugin.video.nemesisaio".*?version="(.*?)"', currentversioncheck, flags=re.DOTALL)[0]
        with open(AddonXML) as F:
            yourversion = re.findall(
                '<addon id="plugin.video.nemesisaio".*?version="(.*?)"', F.read(), flags=re.DOTALL)[0]
        if currentversion == yourversion:
            addStandardLink('[COLOR lime][B]Addon Up To Date[/B][/COLOR]', 'MOVIES', 9999,
                            Addonicon, fanart, description='Your Running The Latest Version Of NemesisAio')
        else:
            addStandardLink('[COLOR orange][B]Addon Out Of Date : [COLOR yellow]Click Here To Update[/B][/COLOR]',
                            'MOVIES', 2000, Addonicon, fanart, description='We Need To Update Your Addon')
    except:
        pass
    addStandardLink('[COLOR orange][B]Join A Watch Party[/B][/COLOR]', 'MOVIES',
                    3001, Addonicon, fanart, description='Lets Watch With Friends')
    addStandardLink('[COLOR aqua][B]Join NemesisAio Chat Room[/B][/COLOR]',
                    'CHAT', 4000, MoviesImg, fanart, description='Chat With Other Users')
    addDir('[COLOR yellow][B]Movies[/B][/COLOR]', 'MOVIES', 1, MoviesImg,
           fanart, description='Grab The Popcorn And Watch A Film')
    addDir('[COLOR yellow][B]Tv Shows[/B][/COLOR]', 'TVSHOWS', 1,
           TvShowsImg, fanart, description='Lets Watch Our Fav Tv Show')
    # addDir('[COLOR yellow][B]LordJD Youtube Channel[/B][/COLOR]','LORDJD',1,Addonicon,fanart,description='LordJD\'s Youtube Channel Direct')
    addStandardLink('[COLOR yellow][B]Live Sports & Replays[/B][/COLOR]', 'SPORTS',
                    66, SportsImg, fanart, description='Sports Time, Come On You Reds #YNWA')
    addDir('[COLOR yellow][B]Music & Radio[/B][/COLOR]', 'MUSIC', 1,
           MusicImg, fanart, description='Dance Around Like No One Is Watching')
    addDir('[COLOR yellow][B]Documentaries[/B][/COLOR]', 'DOCS', 1,
           DocImg, fanart, description='We All Like A Good Documentary')
    addDir('[COLOR yellow][B]Cartoons[/B][/COLOR]', 'https://thekisscartoon.com/',
           63, CartoonsImg, fanart, description='Thats All Folks')
    addDir('[COLOR yellow][B]Kids[/B][/COLOR]', 'KIDS', 1,
           KidsImg, fanart, description='Grow Their Imagination')
    addStandardLink('[COLOR yellow][B]Anime[/B][/COLOR]', 'null', 42,
                    AnimeImg, fanart, description='For The Big Kids In The House')
    addDir('[COLOR yellow][B]Webcams[/B][/COLOR]', 'WEBCAMS', 1,
           WebcamsImg, fanart, description='Eye Spy With My Little Eye')
    # addDir('[COLOR yellow][B]Gaming Videos[/B][/COLOR]','GAMING',1,GamingImg,fanart,description='We All Love To Game Really')
    addStandardLink('[COLOR yellow][B]XXX[/B][/COLOR]', 'rul',
                    67, XXXImg, fanart, description='Got The Wet Wipes')
    addDir('[COLOR red][B]Settings & Maintenance[/B][/COLOR]', 'rul',
           999, MaintenanceImg, fanart, description='The Techinical Stuff')
    # addStandardLink('[COLOR red][B]Test Window[/B][/COLOR]','rul',43,MaintenanceImg,Background_Image,description='The Techinical Stuff')
    xbmc.executebuiltin('Container.SetViewMode(55)')


def GetContent(name, url, iconimage, fanart):
    if 'MOVIES' in url:
        # CHECKSCRAPERS()
        addDir('[COLOR lime][B]Search Movies[/B][/COLOR]', 'SEARCH', 4,
               MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        addDir('[COLOR yellow][B]Top Movies[/B][/COLOR]', 'TOP MOVIES', 4,
               MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        addDir('[COLOR yellow][B]People Watching[/B][/COLOR]', 'NOW PLAYING',
               4, MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        addDir('[COLOR yellow][B]In Cinemas[/B][/COLOR]', 'CINEMA', 4,
               MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        addDir('[COLOR yellow][B]Upcoming Movie Trailers[/B][/COLOR]', 'PLRDnnvx-4xZ1W6tj38Fun0sZPnTaf1JgW',
               5, MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        CheckForLists('MOVIES')
    elif 'TVSHOWS' in url:
        addDir('[COLOR lime][B]Search Tv Shows[/B][/COLOR]', 'TVHUNT', 4,
               MoviesImg, fanart, description='Grab The Popcorn And Watch A Film')
        addDir('[COLOR yellow][B]Popular Shows[/B][/COLOR]', 'TOP TV', 4,
               TvShowsImg, fanart, description='Lets Watch Our Favourite Show')
        addDir('[COLOR yellow][B]Airing Today[/B][/COLOR]', 'AIRING TODAY',
               4, TvShowsImg, fanart, description='Whats On Today')
        # addDir('[COLOR yellow][B]Whats On This Week[/B][/COLOR]','https://projectfreetv.xyz/tvshows',9,TvShowsImg,fanart,description='Whats On Today')
        # addDir('[COLOR yellow][B]24 / 7 Tv Shows[/B][/COLOR]','https://www.arconaitv.us/index.php#shows',13,TvShowsImg,fanart,description='Lets Binge Watch')
    elif 'SPORTS' in url:
        CheckForLists('SPORTS')
        addDir('[COLOR lime][B]Direct Links[COLOR red]|[COLOR yellow]Footie ( Soccer )[/B][/COLOR]',
               'http://streamarmy.co.uk/football_games.xml', 2, SportsImg, fanart, description='[COLOR yellow]Lets Watch Sports[/COLOR]')
        # addDir('[COLOR lime][B]6 Stream [COLOR red]|[COLOR yellow]NFL/NCAFF/MLB/NHL/F1/UFC/Boxing[/B][/COLOR]','http://6stream.xyz/',52,SportsImg,fanart,description='[COLOR yellow]Lets Watch Sports[/COLOR]')
        # addDir("[COLOR lime][B]Daily Events [COLOR red]|[COLOR yellow]Footie/F1/UFC/Boxing[/B][/COLOR]",'http://hhdstreams.club/',38,SportsImg,fanart,'[COLOR yellow]Lets Watch Sports[/COLOR]')
        addDir('[COLOR lime][B]Soccer Streams[COLOR red]|[COLOR yellow]Footie ( Soccer )[/B][/COLOR]',
               'FOOTIE', 40, SportsImg, fanart, description='[COLOR yellow]Lets Watch Sports[/COLOR]')
        # addDir('[COLOR lime][B]Soccer24HD [COLOR red]|[COLOR yellow]Footie[/B][/COLOR]','https://ww.soccer24hd.com/',55,SportsImg,fanart,description='[COLOR yellow]Lets Watch Sports[/COLOR]')
        # addDir('[COLOR lime][B]Daddy Sports [COLOR red]|[COLOR yellow]Footie/NFL/NCAFF/MLB/NHL/F1/UFC/Boxing[/B][/COLOR]','null',50,SportsImg,fanart,description='[COLOR yellow]Lets Watch Sports[/COLOR]')
        # addDir("[COLOR yellow][B]NFL Replays[/B][/COLOR]",'PLM3kzHl4rphJz9yoIiO55tLgEZvffzZ4k',5,SportsImg,fanart,'[COLOR yellow]Lets Watch Sports[/COLOR]')
        addStandardLink('[COLOR lime][B]Fight Club Replays [COLOR red]|[COLOR yellow]UFC/Boxing/WWE/MMA[/B][/COLOR]',
                        'null', 49, SportsImg, fanart, description='All Your Fight Replays')
        # addDir("[COLOR lime][B]Live[COLOR yellow] Golf[/B][/COLOR]",'https://www.reddit.com/r/PuttStreams.json',11,SportsImg,fanart,'[COLOR yellow]Lets Watch Sports[/COLOR]')
    elif 'MUSIC' in url:
        addDir('[COLOR lime][B]Search A Song[/B][/COLOR]', 'SEARCH SONG',
               20, MoviesImg, fanart, description='Search For A Song You Fancy')
        addDir('[COLOR lime][B]Search An Artist[/B][/COLOR]', 'SEARCH ARTIST',
               20, MoviesImg, fanart, description='Search For An Artists Playlist')
        addDir('[COLOR yellow][B]Radio Stations From Around The World[/B][/COLOR]',
               'https://www.internet-radio.com/stations/', 15, MusicImg, fanart, description='Music From Around The World')
        addDir('[COLOR yellow][B]Music Videos[/B][/COLOR]', 'MUSIC VIDEOS', 19,
               MusicImg, fanart, description='Music Videos From Youtube Playlists')
        addDir('[COLOR yellow][B]Karaoke[/B][/COLOR]', 'KARAOKE', 19,
               MusicImg, fanart, description='Music Videos From Youtube Playlists')
        addDir('[COLOR yellow][B]Musical Movies[/B][/COLOR]', 'MUSICAL MOVIES',
               4, MoviesImg, fanart, description='Watch A Film & Dance')
    elif 'KIDS' in url:
        CheckForLists('KIDS')
    elif 'WEBCAMS' in url:
        addDir('[COLOR yellow][B]Webcams By Country[/B][/COLOR]',
               'https://webcamera24.com/countries/', 70, MoviesImg, fanart, description='Lets Be Nosy')
        # addDir('[COLOR yellow][B]Webcams By Catergorie[/B][/COLOR]','https://webcamera24.com/categories/',25,MoviesImg,fanart,description='Lets Be Nosy')
        addDir('[COLOR yellow][B]Popular Webcams[/B][/COLOR]',
               'https://webcamera24.com/popular/', 25, MoviesImg, fanart, description='Lets Be Nosy')
    elif 'DOCS' in url:
        addDir('[COLOR yellow][B]Watch Documentaries[/B][/COLOR]', 'https://watchdocumentaries.com/',
               57, MoviesImg, fanart, description='Documentaries From Watch Documentaries')
        addDir('[COLOR yellow][B]Documentary Heaven[/B][/COLOR]', 'https://documentaryheaven.com/',
               60, MoviesImg, fanart, description='Documentaries From Documentary Heaven')
    elif 'LORDJD' in url:
        addDir('[B][COLOR yellow]Relaxing Sleep[/B][/COLOR]',
               'PLXfGbqQ23uwWBLjTPjkEqeWcwCpUUX-DW', 5, icon, fanarts, '')
        addDir('[B][COLOR yellow]Relaxing Rain[/B][/COLOR]',
               'PLXfGbqQ23uwUhR_yJISRbzOUwHZsjmq4Q', 5, icon, fanarts, '')
        addDir('[B][COLOR yellow]JD Tops[/B][/COLOR]',
               'PLTP6NPJUtpeLyy031160xplw_Z52aD8Vs', 5, icon, fanarts, '')


def GetContentReddit(name, url, iconimage, fanart, description):
    if 'FOOTIE' in url:
        tempurl = 'https://pastebin.com/raw/az72myGt'
        getlink = requests.get(tempurl).text
        url = getlink
    found = 0
    base_domain = 'https://www.reddit.com'
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    link = requests.get(url, headers=Headers).text
    data = json.loads(link)
    get = data['data']['children']
    for i in get:
        name = i['data']['title']
        name = strip_non_ascii(name)
        name = str(name)
        name = CLEANUP(name)
        url = i['data']['permalink']
        url = strip_non_ascii(url)
        url = str(url)
        if 'GMT' in name:
            name = name.replace('[', '').replace(']', ' | ')
            if not base_domain in url:
                url = base_domain + url + '.json'
            found += 1
            addDir('[B][COLOR yellow]' + name + '[/B][/COLOR]',
                   url, 12, icon, fanarts, 'Lets Watch The Game')
        elif 'Game Thread:' in name:
            if not base_domain in url:
                url = base_domain + url + '.json'
            found += 1
            addDir('[B][COLOR yellow]' + name + '[/B][/COLOR]',
                   url, 12, icon, fanarts, 'Lets Watch The Game')
        elif 'Event Thread:' in name:
            if not base_domain in url:
                url = base_domain + url + '.json'
            found += 1
            addDir('[B][COLOR yellow]' + name + '[/B][/COLOR]',
                   url, 12, icon, fanarts, 'Lets Watch The Game')
        elif 'vs' in name:
            if not base_domain in url:
                url = base_domain + url + '.json'
            found += 1
            addDir('[B][COLOR yellow]' + name + '[/B][/COLOR]',
                   url, 12, icon, fanarts, 'Lets Watch The Game')
    if found == 0:
        addLink('[B][COLOR yellow]No Event On ATM[/B][/COLOR]',
                url, 9999, icon, fanarts, 'No Live Events ATM')


def TheMagic(url):
    urls = []
    badmatch = ['prntscr.com', 'facebook.com',
                'discord.gg', 'reddit', 'twitch.tv', 'elixx']
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua,
               'Referer': url}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    table = soup.select('table table-flush')
    table = str(table)
    pattern = r'''href=['"]([^'"]+)['"]'''
    poteniallink = re.findall(pattern, table, flags=re.DOTALL)
    if not poteniallink:
        try:
            table = soup.select('tbody')[0]
        except Exception:
            dialog.notification(
                AddonTitle, '[COLOR yellow]No Links Available, Game either finished or try 30 mins before Kick Off[/COLOR]', icon, 5000)
            quit()
        table = str(table)
        poteniallink = re.findall(pattern, table, flags=re.DOTALL)
    dp.create(AddonTitle, "[COLOR yellow]Going Hunting For Links[/COLOR]")
    dp.update(0)
    for links in set(poteniallink):
        if links.startswith('http') and not any(x in links for x in badmatch):
            urls.append(links)
    if len(urls) == 0:
        dialog.notification(
            AddonTitle, '[COLOR yellow]No Links Available, Game either finished or try 30 mins before Kick Off[/COLOR]', icon, 5000)
        quit()
    else:
        ThreadLinks(urls)


def ThreadLinks(urls):
    import threading
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    badmatch = ['prntscr.com', 'facebook.com', 'discord.gg', 'reddit', 'twitch.tv',
                'elixx', 'google', 'widgets', 'youtube', '.png', '.jpg', 'widget']
    playables = set()
    pattern_m3u8 = re.compile(r'''['"]([^'"]+m3u8.*?)['"]''')
    pattern_iframe = re.compile(r'''<iframe.+?src=['"]([^'"]+).*?['"]''')
    dp.create(AddonTitle, "[COLOR yellow]Searching For Links[/COLOR]")
    dp.update(0)
    checked = 0
    potential = len(urls)

    def fetch_url(url, _iframe=False):
        headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                    'Referer': url}
        try:
            urlHandler = requests.get(
                url, headers={'User-Agent': ua, 'Referer': url}, timeout=5).text
            if pattern_m3u8.search(urlHandler):
                for m3u8 in pattern_m3u8.findall(urlHandler):
                    playables.add('%s|Referer=%s&User-Agent=%s' %
                                  (m3u8, url, ua)) if m3u8.startswith('http') else None
            if pattern_iframe.search(urlHandler) and not _iframe:
                for iframe in pattern_iframe.findall(urlHandler):
                    if iframe.startswith('http') and not any(x in iframe for x in badmatch):
                        if 'wstream' in iframe or 'wigistream' in iframe:
                            try:
                                link2 = requests.get(
                                    iframe, headers=headers2).text
                                packer = re.compile(
                                    '(eval\(function\(p,a,c,k,e,(?:r|d).*)')
                                packed = packer.findall(link2)[0]
                                unpacked = jsunpack.unpack(packed)
                                source = re.compile('''['"](http[^'"]+)['"]''')
                                stream = source.findall(unpacked)[0]
                                stream = (
                                    '%s|verifypeer=false&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' % stream)
                                playables.add(stream)
                            except:
                                pass
                        else:
                            fetch_url(iframe, _iframe=True)
        except BaseException:
            pass

    for url in urls:
        threads = []
        t = threading.Thread(target=fetch_url, args=(url,))
        threads.append(t)
        t.start()

    while True:
        if dp.iscanceled():
            break
        running = [t for t in threads if t.is_alive()]
        if not running:
            break
        msg = "[COLOR yellow]Potential Links = [COLOR lime]%s | [COLOR yellow]Should Play = [COLOR lime]%s[/COLOR]" % (
            potential, str(len(playables)))
        dp.update(100, msg)
        time.sleep(0.5)
        if PY2:
            if threading.active_count() < 3:
                dp.update(
                    100, '', "[COLOR orange]Searching Done (.)Boobies(.) :-D[/COLOR]")
            elif threading.active_count() < 15:
                dp.update(
                    100, '', "[COLOR orange]Searching Almost Done...[/COLOR]")
            elif threading.active_count() < 25:
                dp.update(
                    100, '', "[COLOR orange]Searching Almost Done..[/COLOR]")
            elif threading.active_count() < 50:
                dp.update(
                    100, '', "[COLOR orange]Searching Almost Done.[/COLOR]")
        else:
            if threading.active_count() < 3:
                dp.update(
                    100, msg + "\n"+"[COLOR orange]Searching Done (.)Boobies(.) :-D[/COLOR]")
            elif threading.active_count() < 15:
                dp.update(100, msg + "\n" +
                          "[COLOR orange]Searching Almost Done...[/COLOR]")
            elif threading.active_count() < 25:
                dp.update(100, msg + "\n" +
                          "[COLOR orange]Searching Almost Done..[/COLOR]")
            elif threading.active_count() < 50:
                dp.update(100, msg + "\n" +
                          "[COLOR orange]Searching Almost Done.[/COLOR]")

    if playables:
        for title, url in enumerate(playables.copy()):
            addLink('[B][COLOR yellow]Link [COLOR lime]%s[/B][/COLOR]' %
                    (int(title) + 1), url, 1000, icon, fanarts, '')
    else:
        addLink('[B][COLOR yellow]No Links Available, Check Closer To Start Time[/B][/COLOR]',
                'url', 999999, icon, fanarts, name)
    dp.close()

#


def OpenFanime():
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.fanime)")


def OpenFightclub():
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.FightClub)")


def OpenSportie():
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.sportie)")


def OpenXXX():
    xbmc.executebuiltin("Container.Update(plugin://plugin.video.xxx-o-dus)")


def CheckForLists(url):
    BaseUrl = base64.b64decode(b'aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L3k4bll1VVBQ')
    link = requests.get(BaseUrl).text
    match = re.findall('<list>(.*?)</list>', link, flags=re.DOTALL)
    for items in match:
        if 'MOVIES' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<movies>(.*?)</movies>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = MoviesImg
                if 'YOUTUBE:' in url2:
                    url2 = url2.replace('YOUTUBE:', '')
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 5, icon,
                           fanart, description='Grab The Popcorn Lets Watch A Film')
                else:
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 2, icon,
                           fanart, description='Grab The Popcorn And Watch A Film')
            except:
                pass
        elif 'TVSHOWS' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<tvshows>(.*?)</tvshows>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = TvShowsImg
                if 'YOUTUBE:' in url2:
                    url2 = url2.replace('YOUTUBE:', '')
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 5,
                           icon, fanart, description='Lets Watch Our Favourite Shows')
                else:
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 7,
                           icon, fanart, description='Lets Watch Our Favourite Shows')
            except:
                pass
        elif 'DEV' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<dev>(.*?)</dev>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = Addonicon
                addLink('[COLOR red][B]'+title+'[/B][/COLOR]', url2,
                        1000, icon, fanart, description='Dev Stuff')
            except:
                pass
        elif 'KIDS' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<kids>(.*?)</kids>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = MoviesImg
                if 'YOUTUBE:' in url2:
                    url2 = url2.replace('YOUTUBE:', '')
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 5,
                           icon, fanart, description='Have Some Fun With The Kids')
                else:
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 2, icon,
                           fanart, description='Grab The Popcorn And Watch A Film')
            except:
                pass
        elif 'GAMING' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<gaming>(.*?)</gaming>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = MoviesImg
                if 'YOUTUBE:' in url2:
                    url2 = url2.replace('YOUTUBE:', '')
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 5,
                           icon, fanart, description='Have Some Fun With The Kids')
                else:
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 2, icon,
                           fanart, description='Grab The Popcorn And Watch A Film')
            except:
                pass
        elif 'SPORTS' in url:
            try:
                title = re.findall('<title>(.*?)</title>',
                                   items, flags=re.DOTALL)[0]
                url2 = re.findall('<sports>(.*?)</sports>',
                                  items, flags=re.DOTALL)[0]
                icon = re.findall('<icon>(.*?)</icon>',
                                  items, flags=re.DOTALL)[0]
                if not icon:
                    icon = MoviesImg
                if 'YOUTUBE:' in url2:
                    url2 = url2.replace('YOUTUBE:', '')
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 5,
                           icon, fanart, description='Have Some Fun With The Kids')
                else:
                    addDir('[COLOR yellow][B]'+title+'[/B][/COLOR]', url2, 2, icon,
                           fanart, description='Grab The Popcorn And Watch A Film')
            except:
                pass


def GetListContent(name, url, iconimage):
    url3 = url
    link = requests.get(url).text
    if 'noledynasty' in url:
        match = re.findall('<item>(.*?)</item>', link, flags=re.DOTALL)
        for items in match:
            try:
                links = re.findall('<link>(.+?)</link>',
                                   items, flags=re.DOTALL)
                if len(links) == 1:
                    title = re.findall('<title>(.*?)</title>',
                                       items, flags=re.DOTALL)[0]
                    title = title.encode("utf8") if PY2 else title
                    url = re.findall('<link>(.*?)</link>',
                                     items, flags=re.DOTALL)[0]
                    try:
                        icon = re.findall(
                            '<thumbnail>(.*?)</thumbnail>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        icon = Addonicon
                    try:
                        fanart = re.findall(
                            '<fanart>(.*?)</fanart>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        fanart = fanarts
                    try:
                        description = re.findall(
                            '<description>(.*?)</description>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        description = 'No Desc'
                    description = description.encode(
                        "utf8") if PY2 else description
                    addLink('[COLOR yellow][B]'+title+'[/B][/COLOR]',
                            url, 1000, icon, fanart, description)
                elif len(links) > 1:
                    title = re.findall('<title>(.+?)</title>',
                                       items, flags=re.DOTALL)[0]
                    title = title.encode("utf8") if PY2 else title
                    try:
                        icon = re.findall(
                            '<thumbnail>(.+?)</thumbnail>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        icon = Addonicon
                    try:
                        fanart = re.findall(
                            '<fanart>(.+?)</fanart>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        fanart = fanarts
                    try:
                        description = re.findall(
                            '<description>(.+?)</description>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        description = 'No Desc'
                    description = description.encode(
                        "utf8") if PY2 else description
                    addDir(title, url3, 3, icon, fanart, description)
            except:
                pass
    else:
        match = re.findall('<content>(.*?)</content>', link, flags=re.DOTALL)
        for items in match:
            try:
                links = re.findall('<link>(.+?)</link>',
                                   items, flags=re.DOTALL)
                if len(links) == 1:
                    title = re.findall('<title>(.*?)</title>',
                                       items, flags=re.DOTALL)[0]
                    title = title.encode("utf8") if PY2 else title
                    url = re.findall('<link>(.*?)</link>',
                                     items, flags=re.DOTALL)[0]
                    try:
                        icon = re.findall(
                            '<image>(.*?)</image>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        icon = Addonicon
                    try:
                        fanart = re.findall(
                            '<poster>(.*?)</poster>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        fanart = fanarts
                    try:
                        description = re.findall(
                            '<description>(.*?)</description>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        description = 'No Desc'
                    description = description.encode(
                        "utf8") if PY2 else description
                    addLink('[COLOR yellow][B]'+title+'[/B][/COLOR]',
                            url, 1000, icon, fanart, description)
                elif len(links) > 1:
                    title = re.findall('<title>(.+?)</title>',
                                       items, flags=re.DOTALL)[0]
                    title = title.encode("utf8") if PY2 else title
                    try:
                        icon = re.findall(
                            '<image>(.+?)</image>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        icon = Addonicon
                    try:
                        fanart = re.findall(
                            '<poster>(.+?)</poster>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        fanart = fanarts
                    try:
                        description = re.findall(
                            '<description>(.+?)</description>', items, flags=re.DOTALL)[0]
                    except IndexError:
                        description = 'No Desc'
                    description = description.encode(
                        "utf8") if PY2 else description
                    addDir(title, url3, 3, icon, fanart, description)
            except:
                pass


def TMDBSCRAPE(url):
    if 'TOP MOVIES' in url:
        url = (
            'https://api.themoviedb.org/3/movie/popular?api_key=%s&language=en-US&page=1' % tmdbapi)
    elif 'NOW PLAYING' in url:
        url = ('https://api.themoviedb.org/3/movie/now_playing?api_key=%s&language=en-US&page=1' % tmdbapi)
    elif 'CINEMA' in url:
        url = ('https://api.themoviedb.org/3/discover/movie?api_key=%s&with_release_type=2|3&region=US' % tmdbapi)
    elif 'TOP TV' in url:
        url = (
            'https://api.themoviedb.org/3/tv/popular?api_key=%s&language=en-US&page=1' % tmdbapi)
    elif 'AIRING TODAY' in url:
        url = (
            'https://api.themoviedb.org/3/tv/airing_today?api_key=%s&language=en-US&page=1' % tmdbapi)
    elif 'MUSICAL MOVIES' in url:
        url = ('https://api.themoviedb.org/3/discover/movie?api_key=%s&language=en-US&with_genres=10402&page=1' % tmdbapi)
    elif 'SEARCH' in url:
        string = ''
        keyboard = xbmc.Keyboard(
            string, '[COLOR white][B]Search Which Movie?[/B][/COLOR]')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText()
            if len(string) > 1:
                term = string.lower()
        else:
            quit()
        url = ('https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s' %
               (tmdbapi, term))
    elif 'TVHUNT' in url:
        string = ''
        keyboard = xbmc.Keyboard(
            string, '[COLOR white][B]Search Which Movie?[/B][/COLOR]')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText()
            if len(string) > 1:
                term = string.lower()
        else:
            quit()
        url = ('https://api.themoviedb.org/3/search/tv?api_key=%s&query=%s' %
               (tmdbapi, term))
    else:
        url = url
    data = requests.get(url).json()
    try:
        movies = data['results']
    except:
        dialog.notification(
            AddonTitle, '[COLOR yellow]End Of Results, Or TMDB Not Responding[/COLOR]', Addonicon, 5000)
        quit()
    for info in movies:
        # try:
        imgpath = 'https://image.tmdb.org/t/p/original'
        try:
            title = info['title']
        except KeyError:
            title = info['name']
        icon = info['poster_path']
        movieid = info['id']
        if not icon:
            icon = Addonicon
        else:
            icon = imgpath + icon
        fanart = info['backdrop_path']
        if not fanart:
            fanart = fanarts
        else:
            fanart = imgpath + fanart
        description = info['overview']
        try:
            date = info['release_date']
            date = date.split('-')[0]
        except KeyError:
            date = ''
        movieid = str(movieid)
        title = strip_non_ascii(title)
        description = strip_non_ascii(description)
        if date == '':
            addDir('[COLOR yellow]' + title + "[/COLOR]", movieid,
                   7, icon, fanart, title+' | '+description)
        else:
            addStandardLink("[COLOR gold]" + date + ' | [COLOR yellow]' + title +
                            "[/COLOR]", 'MOVIE||'+title+'##'+movieid, 6, icon, fanart, description)
        # except : pass
    try:
        nextpage = url.split('page=')[-1]
        currentpage = url.split('page=')[0]
        nextpagenumber = int(nextpage) + 1
        nextpageurl = currentpage+'page='+str(nextpagenumber)
        addDir("[COLOR red][B]Next Page[/B][/COLOR]", nextpageurl,
               4, NextPageImg, fanart, 'Get More Results')
    except:
        pass


def TMDBSEASONS(url, fanart, description):
    # dialog.ok("URL",str(url))
    showname = description.split('|')[0]
    url2 = url
    url = ('https://api.themoviedb.org/3/tv/%s?api_key=%s' % (url, tmdbapi))
    # xbmc.log("API URL ::: %s" %url , level=xbmc.LOGINFO)
    link = requests.get(url).json()
    data = link['seasons']
    imgpath = 'https://image.tmdb.org/t/p/original'
    for i in data:
        if PY2:
            name = i['name'].encode('utf-8')
        else:
            name = i['name']
        icon = i['poster_path']
        if not icon:
            icon = Addonicon
        else:
            icon = ('%s%s' % (imgpath, icon))
        if PY2:
            desc = i['overview'].encode('utf-8')
        else:
            desc = i['overview']
        if not desc:
            desc = 'No Description'
        desc = ('%s | %s' % (url2, desc))
        seasonnumber = name.replace('Season ', '').replace('Series ', '')
        getepisodes = ('https://api.themoviedb.org/3/tv/%s/season/%s?api_key=%s' %
                       (url2, seasonnumber, tmdbapi))
        if not 'specials' in name.lower():
            addDir('[COLOR yellow][B]%s[/B][/COLOR]' % name, getepisodes,
                   8, icon, fanart, ('%s # %s|' % (showname, desc)))


def TMDBEPISODES(name, url, fanart, description):
    def get_string_between(s, start, end):
        try:
            return s.split(start)[1].split(end)[0]
        except IndexError:
            return None
    showid = get_string_between(description, '#', '|')
    showname = description.split('#')[0]
    showname = showname.strip()
    link = requests.get(url).json()
    data = link['episodes']
    imgpath = 'https://image.tmdb.org/t/p/original'
    for i in data:
        name = i['name']
        try:
            airdate = i['air_date']
        except KeyError:
            airdate = ''
        seasonno = i['season_number']
        if len(str(seasonno)) == 1:
            seasonno = '0'+str(seasonno)
        seasonno = str(seasonno)
        epino = i['episode_number']
        if len(str(epino)) == 1:
            epino = '0'+str(epino)
        epino = str(epino)
        poster = i['still_path']
        if not poster:
            icon = Addonicon
        else:
            icon = imgpath + poster
        # showid = i['id']
        desc = i['overview']
        desc = strip_non_ascii(desc)
        name = strip_non_ascii(name)
        searchterm = ('%s S-%s|E%s' % (showname, seasonno, epino))
        try:
            addStandardLink('[COLOR gold]' + 'S%s E%s | ' % (seasonno, epino) + '[COLOR yellow][B]'+name+'[/B][/COLOR]',
                            searchterm+'##'+str(showid), 6, icon, fanart, description=desc + '\n\nAired : '+airdate)
        except:
            pass


def YoutubeScrape(url):
    try:
        if not 'https' in url:
            url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2CcontentDetails&maxResults=50&playlistId=' + \
                url + '&key=' + youtubeapi
        data = requests.get(url).json()
        try:
            nextpage = data['nextPageToken']
        except:
            pass
        grab = data['items']
        for i in grab:
            try:
                title = i['snippet']['title']
                title = strip_non_ascii(title)
                description = i['snippet']['description']
                icon = i['snippet']['thumbnails']['default']['url']
                icon = icon.replace('default', 'hqdefault')
                url1 = i['contentDetails']['videoId']
                fanart = icon
                url2 = ('plugin://plugin.video.youtube/play/?video_id=%s' % url1)

                addLink("[COLOR yellow][B]" + str(title) + "[/B][/COLOR]",
                        str(url2), 1000, icon, fanart, description)
            except:
                pass
        try:
            if '&pageToken=' in url:
                npurl = url.split("&pageToken=", 1)[0]
                npurl1 = npurl + '&pageToken=' + nextpage
                xbmc.log(npurl)
                npicon = translatePath(os.path.join(
                    'special://home/addons/' + addon_id, 'icon.png'))
                addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                       npurl1, 5, NextPageImg, fanart)
            else:
                npurl = url + '&pageToken=' + nextpage
                npicon = translatePath(os.path.join(
                    'special://home/addons/' + addon_id, 'icon.png'))
                addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                       npurl, 5, NextPageImg, fanart)
        except:
            pass
    except:
        pass


def Indexer(name, url, iconimage, fanart, description):
    Notice = xbmc.LOGNOTICE if PY2 else xbmc.LOGINFO

    def runSource(call, type, name, year, IMDBNO):
        get_sources = []
        get_sources = call.Index(type, name, year, IMDBNO)
        try:
            finalsources.extend(get_sources)
        except:
            pass
    dialog = xbmcgui.Dialog()
    if 'MOVIE||' in url:
        type = 'MOVIE'
        url = url.replace('MOVIE||', '')
        MovieID = url.split('##')[1]
        url = url.split('##')[0]
        url2 = ('https://api.themoviedb.org/3/movie/%s?api_key=%s&append_to_response=videos' %
                (MovieID, tmdbapi))
        link = requests.get(url2).json()
        try:
            IMDBNO = link['imdb_id']
        except:
            IMDBNO = ''
    else:
        type = 'TV'
        SHOWID = url.split('##')[1]
        # dialog.ok("SGO",str(SHOWID))
        url2 = ('https://api.themoviedb.org/3/tv/%s/external_ids?api_key=%s&language=en-US' %
                (SHOWID, tmdbapi))
        link = requests.get(url2).json()
        try:
            IMDBNO = link['imdb_id']
        except:
            IMDBNO = ''
        # dialog.ok("IMSB",str(IMDBNO))
        url = url.split('##')[0]
    date = name
    threads = []
    j = 0
    totalscrapers = 0
    url = url.replace('[COLOR yellow]', '').replace(
        '[/COLOR]', '').replace('[COLOR gold]', '')
    date = date.replace('[COLOR yellow]', '').replace(
        '[/COLOR]', '').replace('[COLOR gold]', '').replace('|', '').strip()
    date = date.replace(url, '')
    name = re.sub(r'([^\s\w]|_)+', '', name)
    name = re.sub(r' +', ' ', name)
    Search = url
    FilmTitle = url
    global finalsources
    finalsources = []
    threads = []
    j = 0
    totalscrapers = 0
    from scrapers import sources
    _sources = sources()
    import threading
    get_sources = []
    for indexer in _sources:
        threads = []
        t = threading.Thread(target=runSource, args=(
            indexer[1], type, Search, date, IMDBNO))
        threads.append(t)
        # t.start()
        [t.start() for i in threads]
        # threads.append(workers.Thread(runSource, indexer[1], type, Search, date, IMDBNO))
    dp.create(
        AddonTitle, "[B][COLOR yellow]Searching For [COLOR white]%s[/B][/COLOR]" % Search.title())
    time.sleep(1.5)
    # [t.start() for i in threads]
    for n in range(0, 45):
        if dp.iscanceled():
            break
        alive = [x.is_alive() for x in threads if x.is_alive() == True]
        if PY2:
            dp.update(int((100 / float(len(threads))) * len([x for x in threads if x.is_alive() == False])), 'Elapsed: %s' % (
                n), 'Remaining Scrapers: %s' % len(alive), 'Links Found: %s' % len(finalsources))
        else:
            dp.update(int((100 / float(len(threads))) * len([x for x in threads if x.is_alive() == False])), 'Elapsed: %s' % (
                n) + '\n' + 'Remaining Scrapers: %s' % len(alive) + '\n' + 'Links Found: %s' % len(finalsources))
        if len(alive) == 0:
            time.sleep(2)
            break
        time.sleep(1)
    dp.close()
    streamurl = []
    streamname = []
    _finalsources = sorted(finalsources, key=lambda k: k['quality'])
    for i in _finalsources:
        try:
            if (i['Debrid']) == True:
                (i['title']) = '[COLOR yellow]' + (i['title']) + '[/COLOR]'
            elif (i['Direct']) == True:
                (i['title']) = '[COLOR pink]' + (i['title']) + '[/COLOR]'
            else:
                (i['title']) = '[COLOR white]' + (i['title']) + '[/COLOR]'
            streamurl.append(i['url'])
            streamname.append(i['title'])
        except Exception as c:
            xbmc.log("ERROR NEMESAIO ::: %s" % c, level=Notice)
    GuiDisplay(FilmTitle, streamname, streamurl,
               iconimage, fanart, description, value='0')


def CacheChecker(name, data, iconimage, fanart, description):
    import traceback
    try:
        HeaderName = name
        RDenabled = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
            'RealDebridResolver_token'))
        PMenabled = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
            'PremiumizeMeResolver_token'))

        Return = []
        Hashes = []
        Cached = []
        names = []
        goodlinks = []
        qualityz = []

        def CheckPremiumize(items):
            cachedtrue = 0
            PremToken = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
                'PremiumizeMeResolver_token'))
            ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                  "Authorization": "Bearer %s" % PremToken}
            Baseurl = 'https://www.premiumize.me/api/cache/check'
            data = {'items[]': Hashes}
            link = requests.post(Baseurl, data=data, headers=ua).json()
            for index, value in enumerate(link.get("response", [False])):
                if value:
                    Cached.append(list(Hashes)[index])
            for name, link in items:
                for cleared in Cached:
                    try:
                        if cleared[0] in link:
                            if 'uhd' in name.lower():
                                quality = '1'
                            elif '3d' in name.lower():
                                quality = '1'
                            elif 'fhd' in name.lower():
                                quality = '2'
                            elif 'hd' in name.lower():
                                quality = '3'
                            elif 'sd' in name.lower():
                                quality = '4'
                            qualityz.append((name, link, quality))
                        else:
                            continue
                    except:
                        pass

        def CheckRD(items):
            RDenabled = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
                'RealDebridResolver_token'))

            def RefreshToken():
                client_id = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
                    'RealDebridResolver_client_id'))
                client_secret = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
                    'RealDebridResolver_client_secret'))
                refresh = (xbmcaddon.Addon('script.module.resolveurl').getSetting(
                    'RealDebridResolver_refresh'))
                Auth_url = 'https://api.real-debrid.com/oauth/v2/token'
                data = {'client_id': client_id,
                        'client_secret': client_secret,
                        'code': refresh,
                        'grant_type': 'http://oauth.net/grant_type/device/1.0'}
                GetNew = requests.post(Auth_url, data=data)
                Api = json.loads(GetNew.text)
                if 'access_token' in Api:
                    token = Api['access_token']
                if 'refresh_token' in Api:
                    refresh = Api['refresh_token']
                (xbmcaddon.Addon('script.module.resolveurl').setSetting(
                    'RealDebridResolver_token', token))
                (xbmcaddon.Addon('script.module.resolveurl').setSetting(
                    'RealDebridResolver_refresh', refresh))
                CheckRD(items)
            RDURL = 'https://api.real-debrid.com/rest/1.0/torrents/instantAvailability%s&auth_token=' + RDenabled
            hash_string = ''
            for hash in Hashes:
                try:
                    hash_string = hash_string+'/'+hash[0]
                except:
                    pass
            TOTAL = (RDURL % hash_string.lower() + RDenabled)
            # xbmc.log("HASHES ::: %s" %TOTAL , level=xbmc.LOGNOTICE)
            link = requests.get(RDURL % hash_string).json()
            # xbmc.log("RD RESPONSE ::: %s" %link , level=xbmc.LOGNOTICE)
            if 'bad_token' in str(link):
                RefreshToken()
            for index, value in enumerate(link):
                try:
                    cachedTrue = link[value]['rd']
                    if cachedTrue:
                        Cached.append(value)
                except:
                    pass
            for name, link in items:
                for cleared in Cached:
                    try:
                        if cleared in link:
                            if 'uhd' in name.lower():
                                quality = '1'
                            elif '3d' in name.lower():
                                quality = '1'
                            elif 'fhd' in name.lower():
                                quality = '2'
                            elif 'hd' in name.lower():
                                quality = '3'
                            elif 'sd' in name.lower():
                                quality = '4'
                            qualityz.append((name, link, quality))
                        else:
                            continue
                    except:
                        pass
        for name, link in data:
            if 'magnet' not in link:
                if 'uhd' in name.lower():
                    quality = '1'
                elif '3d' in name.lower():
                    quality = '1'
                elif 'fhd' in name.lower():
                    quality = '2'
                elif 'hd' in name.lower():
                    quality = '3'
                elif 'sd' in name.lower():
                    quality = '4'
                qualityz.append((name, link, quality))
            else:
                GetHashes = re.findall(r'''btih:(.*?)&''', link)
                Hashes.append(GetHashes)
        if len(PMenabled) > 2:
            CheckPremiumize(data)
        elif len(RDenabled) > 2:
            CheckRD(data)
        valuez = '1'
        final = sorted(qualityz, key=lambda k: k[2])
        for j in final:
            names.append(j[0])
            goodlinks.append(j[1])
        GuiDisplay(HeaderName, names, goodlinks,
                   iconimage, fanart, description, valuez)
    except Exception as c:
        xbmc.log("ERROR ::: {0}".format(
            traceback.format_exc()), level=xbmc.LOGNOTICE)


def ChatRoom():
    reservednames = ["nemzzy", "nemzzzy", "nemzzyy", "nemesis",
                     "nemzzy668", "manc", "_manc", "_manc_", "lordjd", "jdlord"]
    if chatname == '':
        dialog.ok(
            AddonTitle, "Before Using Chat Room Please Create A Username which will be displayed to others")
        string = ''
        keyboard = xbmc.Keyboard(
            string, '[COLOR white][B]Enter Your Display Name[/B][/COLOR]')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText()
            NameEntered = keyboard.getText()
            if not any(x in string.lower() for x in reservednames):
                if len(string) > 1:
                    selfAddon.setSetting(id='chatname', value=string)

                    dialog.notification(
                        AddonTitle, '[COLOR yellow]Username Set, Please Re-Enter Chat[/COLOR]', Addonicon, 5000)

                    quit()
                else:
                    quit()
            else:
                dialog.ok(
                    AddonTitle, "You have tried to use a name reserved for Stream Army Team Members, Please enter the password to continue")
                string = ''
                keyboard = xbmc.Keyboard(
                    string, '[COLOR white][B]Enter Password[/B][/COLOR]')
                keyboard.doModal()
                if keyboard.isConfirmed():
                    string = keyboard.getText()
                    if string.lower() == 'manclovescock':
                        selfAddon.setSetting(id='chatname', value=NameEntered)
                        selfAddon.setSetting(id='adminchatpass', value=string)
                        dialog.notification(
                            AddonTitle, '[COLOR yellow]Password Accepted, Re Enter Chat[/COLOR]', Addonicon, 5000)
                        quit()
                    else:
                        dialog.ok(
                            AddonTitle, "Wrong Password, Please Choose A Different Chat Name")
                        selfAddon.setSetting(id='chatname', value='')
                        xbmc.executebuiltin('Container.Refresh')
                else:
                    quit()
    if any(x in chatname.lower() for x in reservednames):
        checkadmin = selfAddon.getSetting('adminchatpass')
        if checkadmin.lower() == 'manclovescock':
            pass
        else:
            dialog.ok(
                AddonTitle, "You have tried to use a name reserved for Stream Army Team Members, Please enter the password to continue")
            string = ''
            keyboard = xbmc.Keyboard(
                string, '[COLOR white][B]Enter Password[/B][/COLOR]')
            keyboard.doModal()
            if keyboard.isConfirmed():
                string = keyboard.getText()
                if string.lower() == 'manclovescock':
                    # selfAddon.setSetting(id='chatname', value=string)
                    selfAddon.setSetting(
                        id='adminchatpass', value=string.lower())
                else:
                    dialog.ok(
                        AddonTitle, "Wrong Password, Please Choose A Different Chat Name")
                    selfAddon.setSetting(id='chatname', value='')
                    xbmc.executebuiltin('Container.Refresh')
            else:
                quit()

    def SendMessage(self, messagetext):
        if len(messagetext) >= 100:
            dialog.notification(
                AddonTitle, '[COLOR yellow]Please Keep Each Message To Less Than 100 Chars[/COLOR]', Addonicon, 5000)
            quit()
        messagetext = messagetext.replace(' ', '%20')
        apiurl = ('http://streamarmy.co.uk/AioChat/addmsg.php?user=%s&msg=%s' %
                  (chatname, messagetext))
        send = requests.get(apiurl).text
        dialog.notification(
            AddonTitle, '[COLOR yellow]%s[/COLOR]' % send, Addonicon, 2500)
        self.message.setText('')
        ChatRoom()
        self.close()

    def Refresh(self):
        ChatRoom()
        self.close()

    def GetMsgs(self):
        reservednames = ["nemzzy", "nemzzzy", "nemzzyy", "nemesis",
                         "nemzzy668", "manc", "_manc", "_manc_", "lordjd", "jdlord"]
        url = 'http://streamarmy.co.uk/AioChat/getmsg.php'
        try:
            c = requests.get(url).json()
            for i in c:
                Name = i['items']['Name']
                Message = i['items']['Message']
                Time = i['items']['Time']
                if any(x in Name.lower() for x in reservednames):
                    Msg = (
                        '[COLOR yellow]%s : [COLOR red]%s -  [COLOR white]%s[/COLOR]' % (Time, Name, Message))
                else:
                    Msg = (
                        '[COLOR yellow]%s : [COLOR green]%s -  [COLOR white]%s[/COLOR]' % (Time, Name, Message))
                self.List.addItem(Msg)
        except Exception:
            Msg = (
                '[COLOR yellow]No Messages ATM , Chat Gets Auto Deleted Every 72 Hours, Type Something To Add To Chat[/COLOR]')
            self.List.addItem(Msg)

    class Main(pyxbmct.AddonFullWindow):
        def __init__(self, title='NemesisAioChat'):
            super(Main, self).__init__(title)
            self.setGeometry(1280, 720, 100, 50)
            Background = pyxbmct.Image(ChatBG)
            self.placeControl(Background, -10, -1, 123, 52)

            self.message = pyxbmct.Edit(
                'Enter Message : ', textColor='0xFFFFFFFF')
            self.sendbutton = pyxbmct.Button(
                'SEND', focusTexture=None, noFocusTexture=None)
            self.quitbutton = pyxbmct.Button(
                'QUIT', focusTexture=None, noFocusTexture=None)
            self.refreshbutton = pyxbmct.Button(
                'REFRESH', focusTexture=None, noFocusTexture=None)
            self.placeControl(self.sendbutton, 98, 33, 10, 5)
            self.placeControl(self.message, 98, 8, 10, 24)
            self.placeControl(self.refreshbutton, 98, 38, 10, 5)
            self.placeControl(self.quitbutton, 98, 43, 10, 5)
            self.set_active_controls()
            self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
            self.connect(self.sendbutton, lambda: SendMessage(
                self, self.message.getText()))
            self.connect(self.refreshbutton, lambda: Refresh(self))
            self.connect(self.quitbutton, self.close)
            self.List = pyxbmct.List(buttonFocusTexture=Listbg, _space=11,
                                     _itemTextYOffset=-7, _itemTextXOffset=-1, textColor='0xFFFFFFFF')
            self.placeControl(self.List, 5, 9, 80, 32)
            self.setFocus(self.message)
            GetMsgs(self)
            self.set_navigation()

        def set_active_controls(self):
            self.connectEventList(
                [pyxbmct.ACTION_MOVE_DOWN,
                 pyxbmct.ACTION_MOVE_UP,
                 pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
                 pyxbmct.ACTION_MOUSE_WHEEL_UP,
                 pyxbmct.ACTION_MOUSE_MOVE],
                self.List_update)

        def set_navigation(self):
            self.message.controlRight(self.sendbutton)
            self.sendbutton.controlRight(self.refreshbutton)
            self.refreshbutton.controlRight(self.quitbutton)
            self.message.controlUp(self.List)
            self.sendbutton.controlUp(self.List)
            self.refreshbutton.controlUp(self.List)
            self.quitbutton.controlUp(self.List)
            self.List.controlDown(self.message)
            self.List.controlLeft(self.message)
            self.List.controlRight(self.message)
            self.List.controlDown(self.message)
            self.refreshbutton.controlLeft(self.sendbutton)
            self.sendbutton.controlLeft(self.message)
            self.quitbutton.controlLeft(self.refreshbutton)

        def List_update(self):
            global Media_Link
            Media_Link = []
            global Media_Title
            try:
                if self.getFocus() == self.List:
                    position = self.List.getSelectedPosition()
                    Media_Title = Item_Title[position]
                    Media_Link = Item_Link[position]
            except:
                pass

        def setAnimation(self, control):
            control.setAnimations([('WindowOpen', 'effect=slide start=2000 end=0 time=1000',),
                                   ('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
    window = Main('NemesisAioChat')
    window.doModal()
    del window


def GuiDisplay(title, name, url, iconimage, fanart, description, value):
    if not '[B]' in title:
        HeaderName = ('[B]%s[/B]' % title)
    else:
        HeaderName = title
    title = title.replace('[B]', '').replace('[/B]', '')
    description2 = description
    description = ('[B]%s[/B]' % description)
    combined = list(zip(name, url))

    def passed(self, name, url, iconimage, fanart, description):
        global Item_Title
        global Item_Link
        Item_Title = []
        Item_Link = []
        Item_Desc = []
        Item_Icon = []
        torrent = 0
        direct = 0
        Resolver = 0
        for titles, urls in combined:
            if 'magnet' in urls:
                torrent += 1
            elif 'DIRECT' in titles:
                direct += 1
            else:
                Resolver += 1
        self.List.addItem('[COLOR deepskyblue][B]' + title +
                          ' Links | [COLOR yellow]%s[COLOR deepskyblue] Torrents | [COLOR yellow]%s [COLOR deepskyblue]Direct Links |[COLOR yellow] %s [COLOR deepskyblue]Resolver Links[/B][/COLOR]' % (torrent, direct, Resolver))
        Item_Title.append('[COLOR deepskyblue]' + title+' Links[/COLOR]')
        Item_Link.append('')
        # if value == '0':
        # self.List.addItem('[B][COLOR lime]CLICK TO REMOVE UN-CACHED TORRENTS[/B][/COLOR]')
        # Item_Title.append('[B][COLOR deepskyblue]'+ title+' Links[/B][/COLOR]')
        # Item_Link.append('UNCACHED')
        self.List.addItem(
            '[COLOR fuchsia][B]Start A Watch Party For %s[/B][/COLOR]' % title)
        Item_Title.append('[COLOR fuchsia]' + title+' Links[/COLOR]')
        Item_Link.append('WATCHPARTY')
        for titles, urls in combined:
            Item_Link.append(urls)
            Item_Title.append(titles)
            self.List.addItem(titles)

    def Selector(self, name, url, iconimage, description):
        if 'UNCACHED' in url:
            CacheChecker(name, combined, iconimage, fanart, description2)
            self.close()
        elif 'WATCHPARTY' in url:
            streamurl = []
            streamname = []
            for titles, urls in combined:
                streamurl.append(urls)
                streamname.append(titles)
            dialog = xbmcgui.Dialog()
            select = dialog.select(
                'Choose A Party Link For %s' % name, streamname)
            if select < 0:
                quit()
            StartParty(name, streamurl[select], iconimage, description)
        else:
            Player(name, url, iconimage, description)

    class Main(pyxbmct.AddonFullWindow):
        def __init__(self, title='NemesisAio'):
            super(Main, self).__init__(title)
            self.setGeometry(1280, 720, 100, 50)
            Background = pyxbmct.Image(fanart)
            self.placeControl(Background, -10, -1, 123, 52)
            self.List_BackGround = pyxbmct.Image(List_Back)
            self.placeControl(self.List_BackGround, 0, 0, 100, 50)
            self.Icon_Image = pyxbmct.Image(iconimage)
            self.placeControl(self.Icon_Image, 29, 8, 30, 7)
            self.Quality = pyxbmct.Image('')
            self.placeControl(self.Quality, 50, 15, 9, 4)
            self.textbox = pyxbmct.TextBox(textColor='0xFFFFFFFF')
            self.placeControl(self.textbox, 60, 0, 20, 24)
            self.textbox.setText(description)
            self.textbox.autoScroll(2500, 2500, 2500)
            self.MovieTitle = pyxbmct.Label(
                HeaderName, textColor='0xFFFFFFFF', font='font18', alignment=pyxbmct.ALIGN_CENTER)
            self.placeControl(self.MovieTitle, 20, 7, 10, 10)
            self.set_active_controls()
            self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
            self.List = pyxbmct.List(buttonFocusTexture=Listbg, _space=11,
                                     _itemTextYOffset=-7, _itemTextXOffset=-1, textColor='0xFFFFFFFF')
            self.placeControl(self.List, 15, 24, 70, 25)
            self.connect(self.List, lambda: Selector(
                self, HeaderName, str(Media_Link), iconimage, description))
            passed(self, name, url, iconimage, fanart, description)
            self.setFocus(self.List)

        def set_active_controls(self):
            self.connectEventList(
                [pyxbmct.ACTION_MOVE_DOWN,
                 pyxbmct.ACTION_MOVE_UP,
                 pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
                 pyxbmct.ACTION_MOUSE_WHEEL_UP,
                 pyxbmct.ACTION_MOUSE_MOVE],
                self.List_update)

        def List_update(self):
            global Media_Link
            Media_Link = []
            global Media_Title
            try:
                if self.getFocus() == self.List:
                    position = self.List.getSelectedPosition()
                    Media_Title = Item_Title[position]
                    Media_Link = Item_Link[position]
                    if 'UHD' in Media_Title:
                        self.Quality.setImage(FourK)
                    elif 'FHD' in Media_Title or '1080' in Media_Title:
                        self.Quality.setImage(FHD)
                    elif 'HD' in Media_Title or '720' in Media_Title:
                        self.Quality.setImage(HD)
                    else:
                        self.Quality.setImage(SD)
            except:
                pass

        def setAnimation(self, control):
            control.setAnimations([('WindowOpen', 'effect=slide start=2000 end=0 time=1000',),
                                   ('WindowClose', 'effect=slide start=100 end=1400 time=500',)])
    window = Main('NemesisAio')
    window.doModal()
    del window
# def runSource(call, type, name,year,IMDBNO,torrents=''):
    # xbmc.log("name ::: %s" %name , level=xbmc.LOGINFO)
    # xbmc.log("year ::: %s" %year , level=xbmc.LOGINFO)
    # xbmc.log("call ::: %s" %call , level=xbmc.LOGINFO)
    # xbmc.log("imdb ::: %s" %IMDBNO , level=xbmc.LOGINFO)
    # get_sources = []
    # get_sources = call.Index(type, name, year, IMDBNO, torrents)
    # finalsources.extend(get_sources)


def WhatsOnTv(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    link = requests.get(
        'https://www.projectfreetv.fun/tv-today/', headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    movie_containers = soup.findAll(class_='tvschedule')
    for info in movie_containers:
        day = info.h4.text
        date = info.span.text
        datestr = ('%s %s' % (day, date))
        links = info.findAll(class_='tvschedule_content')
        addLink("[COLOR lime][B]" + datestr + "[/B][/COLOR]", 'fff',
                9999, icon, fanart, description=('Whats On Tv %s' % datestr))
        for link in links:
            url = link.h6.find('a')['href']
            if not 'https' in url:
                url = 'https:'+url
            url = 'https:' + url if url.startswith('//') else url
            url = strip_non_ascii(url)
            title = link.h6.find('a')['title']
            title = strip_non_ascii(title)
            addLink("[COLOR yellow][B]" + title + "[/B][/COLOR]",
                    url, 10, icon, fanart, description)
    # xbmc.executebuiltin('Container.SetViewMode(55)')


def ResolveWhatsOnTv(name, url, iconimage):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    movie_containers = soup.findAll(class_='tblimg')
    found = 0
    streamurl = []
    streamname = []
    for info in movie_containers:
        found += 1
        url = info['href']
        title = ('Link %s' % str(found))
        streamurl.append(url)
        streamname.append(title)
    dialog = xbmcgui.Dialog()
    select = dialog.select(name, streamname)
    if select < 0:
        quit()
    PLAYLINK(name, streamurl[select], iconimage)


def Twenty7(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find_all('div', class_={'col-xs-6 col-m-4 col-l-2'})
    basedomain = 'https://www.arconaitv.us/'
    for i in data:
        title = i.img['alt']
        description = i.a['title']
        url = i.a['href']
        image = i.img['src']
        if not basedomain in url:
            url = basedomain+url
        if not basedomain in image:
            image = basedomain+image
        addLink("[COLOR yellow][B]" + title + "[/B][/COLOR]",
                url, 14, image, fanart, description)


def ResolveTwenty7(name, url, iconimage):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    import jsunpack
    if jsunpack.detect(link):
        page_data = jsunpack.unhunt(link)
        r = re.search(r"src:\s*'([^']+)", page_data)
        strurl = ''
        if r:
            strurl = r.group(1)
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    play = ('%s|Referer=%s&User-Agent=%s' % (strurl, url, ua))
    PLAYLINK(name, play, iconimage)


def RadioWorld(url):
    addDir("[COLOR lime][B]Search A Song Or Station[/B][/COLOR]", url, 18, MusicImg, fanart,
           'Search For A Radio Station, Or See If Any Radio Station Is Playing A Song You Want')
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    movie_containers = soup.findAll('dl')
    basedomain = 'https://www.internet-radio.com'
    for data in movie_containers:
        title = data.a.text.title()
        url = data.a['href']
        if not basedomain in url:
            url = basedomain+url
        desc = data.dd.text
        addDir("[COLOR yellow][B]" + title +
               "[/B][/COLOR]", url, 16, icon, fanart, desc)


def RadioWorldContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    movie_containers = soup.findAll('tr')
    basedomain = 'https://www.internet-radio.com'
    for data in movie_containers:
        title = data.h4.text
        title = strip_non_ascii(title)
        url = data.a['href']
        currentlyplaying = data.b.text
        currentlyplaying = strip_non_ascii(currentlyplaying)
        if not basedomain in url:
            url = basedomain+url
        desc = ('[COLOR lime][B]Currently Playing : %s [/B][/COLOR]' %
                currentlyplaying)
        addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                url, 17, icon, fanart, desc)
    try:
        nextpage = soup.find('li', class_={'next'})
        nextpage = nextpage.a['href']
        if not basedomain in nextpage:
            nextpage = basedomain+nextpage
        addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
               nextpage, 16, NextPageImg, fanart)
    except:
        pass


def RadioWorldContentResolve(name, url, iconimage):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    play = re.findall('File1=(.*?)\s', link, flags=re.DOTALL)[0]
    if 'listen.pls' in play:
        link2 = requests.get(play, headers=headers).text
        play = re.findall('File1=(.*?)\s', link2, flags=re.DOTALL)[0]
    PLAYLINK(name, play, iconimage)


def RadioWorldSearch():
    string = ''
    keyboard = xbmc.Keyboard(
        string, '[COLOR white][B]Enter Artist, Song Or Station Below[/B][/COLOR]')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string) > 1:
            term = string.lower()
            term = term.replace(' ', '+')
            url = ('https://www.internet-radio.com/search/?radio=%s' % term)
            RadioWorldContent(url)
        else:
            quit()
    else:
        quit()


def MusicSearch(url):
    if 'SEARCH SONG' in url:
        title = 'Song Name'
    elif 'SEARCH ARTIST' in url:
        title = 'Artist Name'
    string = ''
    keyboard = xbmc.Keyboard(
        string, '[COLOR white][B]Enter %s You\'d Like Us To Search For[/B][/COLOR]' % title)
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string) > 1:
            term = string.lower()
            term = term.replace(' ', '+')
        else:
            quit()
    else:
        quit()
    if 'SEARCH SONG' in url:
        url = ('https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q=%s&key=%s' %
               (term, youtubeapi))
        SearchYoutube(url)
    elif 'SEARCH ARTIST' in url:
        url = 'SEARCH||'+term
        MusicVideos(url)


def MusicVideos(url):
    if 'MUSIC VIDEOS' in url:
        url = ('https://www.googleapis.com/youtube/v3/search?part=snippet&q=music+videos&type=playlist&key=%s&maxResults=50' % youtubeapi)
    elif 'KARAOKE' in url:
        url = ('https://www.googleapis.com/youtube/v3/search?part=snippet&q=karaoke+videos&type=playlist&key=%s&maxResults=50' % youtubeapi)
    elif 'SEARCH||' in url:
        url = url.split('||')[1]
        url = ('https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&type=playlist&key=%s&maxResults=50' % (url, youtubeapi))
    else:
        url = url
    link = requests.get(url).json()
    try:
        nextpage = link['nextPageToken']
    except:
        pass
    data = link['items']
    for i in data:
        title = i['snippet']['title']
        title = strip_non_ascii(title)
        icon = i['snippet']['thumbnails']['default']['url']
        icon = icon.replace('default', 'hqdefault')
        description = i['snippet']['description']
        description = strip_non_ascii(description)
        playlistid = i['id']['playlistId']
        addDir("[COLOR yellow][B]"+title+"[/B][/COLOR]",
               playlistid, 5, icon, icon, description)
    try:
        if '&pageToken=' in url:
            npurl = url.split("&pageToken=", 1)[0]
            npurl1 = npurl + '&pageToken=' + nextpage
            xbmc.log(npurl)
            npicon = translatePath(os.path.join(
                'special://home/addons/' + addon_id, 'icon.png'))
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   npurl1, 19, NextPageImg, fanart)
        else:
            npurl = url + '&pageToken=' + nextpage
            npicon = translatePath(os.path.join(
                'special://home/addons/' + addon_id, 'icon.png'))
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   npurl, 19, NextPageImg, fanart)
    except:
        pass


def SearchYoutube(url):
    link = requests.get(url).json()
    try:
        nextpage = link['nextPageToken']
    except:
        pass
    data = link['items']
    for i in data:
        try:
            title = i['snippet']['title']
            title = strip_non_ascii(title)
            try:
                icon = i['snippet']['thumbnails']['high']['url']
            except:
                icon = iconimage
            try:
                playlistid = i['id']['videoId']
            except:
                playlistid = i['contentDetails']['videoId']
            url2 = ('https://youtube.com/watch?v=' % playlistId)
            # url2 = ('https://www.youtube.com/watch?v=%s' % playlistId)
            # playlistid = 'plugin://plugin.video.youtube/play/?video_id='+playlistid
            addLink('[COLOR yellow][B]' + title + '[/B][/COLOR]',
                    url2, 1000, icon, fanarts, '')
        except:
            pass
    try:
        if '&pageToken=' in url:
            npurl = url.split("&pageToken=", 1)[0]
            npurl1 = npurl + '&pageToken=' + nextpage
            npicon = translatePath(os.path.join(
                'special://home/addons/' + addon_id, 'icon.png'))
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   npurl1, 21, NextPageImg, fanart)
        else:
            npurl = url + '&pageToken=' + nextpage
            npicon = translatePath(os.path.join(
                'special://home/addons/' + addon_id, 'icon.png'))
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   npurl, 21, NextPageImg, fanart)
    except:
        pass


def CartoonSelect(url):
    addDir("[COLOR red][B]Search[/B][/COLOR]", 'SEARCH', 64, icon, fanarts, '')
    addDir("[COLOR yellow][B]Movies[/B][/COLOR]",
           'https://thekisscartoon.com/movies/', 22, icon, fanarts, '')
    addDir("[COLOR yellow][B]Episodes[/B][/COLOR]",
           'https://thekisscartoon.com/filter/?type=tvshows', 22, icon, fanarts, '')
    addDir("[COLOR yellow][B]Trending Cartoons[/B][/COLOR]",
           'https://thekisscartoon.com/trending/?get=tv', 22, icon, fanarts, '')
    addDir("[COLOR yellow][B]Trending Movies[/B][/COLOR]",
           'https://thekisscartoon.com/trending/?get=movies', 22, icon, fanarts, '')


def SearchCartoons():
    string = ''
    keyboard = xbmc.Keyboard(
        string, '[COLOR white][B]What Shall We Search For?[/B][/COLOR]')
    keyboard.doModal()
    if keyboard.isConfirmed():
        string = keyboard.getText()
        if len(string) > 1:
            term = string.lower().replace(' ', '+')
            url = 'https://thekisscartoon.com/?s=%s' % term
            DisplaySearchCartoons(url)
    else:
        quit()


def DisplaySearchCartoons(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua,
               'Referer': 'https://thekisscartoon.com/'}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    data = soup.find_all('article')
    for i in data:
        title = i.img['alt']
        url2 = i.a['href']
        icon = i.img['src']
        if '/tvshows/' in url2:
            addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                    url2, 23, icon, fanarts, '')
        else:
            addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                    url2, 24, icon, fanarts, '')


def Cartoons(url):
    # if 'MOVIES' in url: url = 'https://thekisscartoon.com/movies/'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    if '/movies/' in url or 'get=movies' in url:
        data = soup.findAll('article', class_={'item movies'})
    else:
        data = soup.find_all('article', class_={'item tvshows'})
    for i in data:
        title = i.img['alt']
        try:
            icon = i.img['data-lazy-src']
        except:
            icon = i.img['src']
        url2 = i.a['href']
        if '/tvshows/' in url2:
            addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                    url2, 23, icon, fanarts, '')
        else:
            addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                    url2, 24, icon, fanarts, '')
    try:
        np = soup.find('div', class_={'pagination'})
        pattern = r'''arrow_pag.*?href=['"](.*?)['"].*?'''
        try:
            nextpage = re.findall(pattern, str(np))[1]
        except:
            nextpage = re.findall(pattern, str(np))[0]
        # if not basedomain in nextpage: nextpage = basedomain+nextpage
        addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
               nextpage, 22, NextPageImg, fanart)
    except:
        pass


def CartoonEpi(name, url, icon):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    data = soup.find_all('div', class_={'episodiotitle'})
    streamurl = []
    streamname = []
    for i in data:
        title = i.a.text
        url = i.a['href']
        streamname.append(title)
        streamurl.append(url)
    select = dialog.select(name, streamname)
    if select < 0:
        quit()
    else:
        CartoonLinks(name, streamurl[select], iconimage, description='')


def CartoonLinks(name, url, iconimage, description):
    streamurl = []
    streamname = []
    formatlink = 'https://thekisscartoon.com/ajax-get-link-stream/?server={}&filmId={}'
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    filmid = re.findall(r'''var filmId = ['"](.*?)['"]''', link)[0]
    data = soup.find_all('option')
    linksfound = 0
    for links in data:
        if not 'openload' in links['value']:
            try:
                source = formatlink.format(links['value'], filmid)
                headers.update({'Referer': url})
                link2 = requests.get(source, headers=headers).text
                link3 = requests.get(link2, headers=headers).text
                play = re.findall(
                    r'''videoUrl['"]:['"](.*?)['"],.+?:['"](.*?)['"]''', link3)[0]
                construct = 'https://comedyshow.to{}?s={}'
                headers.update({'Referer': link2})
                link4 = requests.get(construct.format(
                    play[0], play[1]), headers=headers).text
                final = re.findall(r'''(http.*?)$''', link4)[0]
                play = '{}|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36&Referer={}'
                playme = play.format(final, link2)
                linksfound += 1
                title = 'Link %s' % linksfound
                streamname.append(title)
                streamurl.append(playme)
            except:
                pass
    if linksfound == 0:
        dialog.notification(
            AddonTitle, '[COLOR yellow]Sorry No Links Available[/COLOR]', icon, 5000)
        quit()
    else:
        select = dialog.select(name, streamname)
        if select < 0:
            quit()
        else:
            PLAYLINK(name, streamurl[select], iconimage)


def WebCamsMenu_coun(url):
    base_dom = 'https://webcamera24.com'
    link = requests.get(url, headers=get_headers()).text
    soup = BeautifulSoup(link, 'html.parser')
    data = soup.find('ul', class_={'CountriesList_list__VO2Jx'})
    for i in data.find_all('a'):
        name = i['title']
        icon = i.img['src']
        url = i['href']
        if base_dom not in url:
            url = base_dom+url
        # if  base_dom not in icon: icon=base_dom+icon
        addDir("[COLOR yellow][B]"+name+"[/B][/COLOR]", url, 25,
               icon, fanarts, 'Webcams Provided By Webcams24')


def WebCamsMenu(url):
    try:
        base_dom = 'https://webcamera24.com'
        link = requests.get(url, headers=get_headers()).text
        soup = BeautifulSoup(link, 'html.parser')
        data = soup.find_all('div', class_={'WebcamItemBlockView_item__yGQ1X'})
        for i in data:
            name = i.a['title']
            url2 = i.a['href']
            icon = i.img['src']
            if base_dom not in url2:
                url2 = base_dom+url2
            # if base_dom not in icon: icon=base_dom+icon
            addLink("[COLOR yellow][B]"+name+"[/B][/COLOR]", url2,
                    26, icon, fanarts, 'Webcams Provided By Webcama24')
    except:
        dialog.notification(
            AddonTitle, '[COLOR yellow]Cloudflare blocked us, Try Again[/COLOR]', Addonicon, 2500)
        # quit()


def WebCamsContent(name, url, iconimage):
    pattern = r'''embedUrl['"].*?['"](.*?)['"]'''
    link = requests.get(url, headers=get_headers()).text
    source = re.findall(pattern, link)[0]
    PLAYLINK(name, source, iconimage)


def WebcamsResolve(name, url, iconimage):
    try:
        from tools import cfscrape
        cloudflare = cfscrape.create_scraper()
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        headers = {'User-Agent': ua}
        link = cloudflare.get(url, headers=headers).text
        soup = BeautifulSoup(link, 'html.parser')
        data = soup.find('iframe')
        link = data['src']
        # link = 'plugin://plugin.video.youtube/play/?url='+link
        PLAYLINK(name, link, iconimage)
    except:
        dialog.notification(
            AddonTitle, '[COLOR yellow]Cloudflare blocked us, Try Again[/COLOR]', Addonicon, 2500)
        # quit()


def WWEReplaysContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    badresults = ['Hindi Movies', 'Hollywood Movies', 'WWE TV Live Stream',
                  'WWE Network Live 24/7', 'Home', 'Movies', 'More', 'Biographies', 'Shows Highlights']
    link = requests.get('http://www.allwrestling.live/', headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find('ul', id={'menu-main-menu'})
    for links in data.find_all('a'):
        title = links.text
        title = strip_non_ascii(title)
        url = links['href']
        if not any(x in title for x in badresults):
            if 'http://www.allwrestling.live/lucha-underground/lu-ppv/' in url:
                url = 'http://www.allwrestling.live/lucha-underground/'
            addDir("[COLOR yellow][B]"+title+"[/B][/COLOR]", url,
                   29, Addonicon, fanarts, 'Replays From %s' % title)


def CleanWWE(text):
    text = text.replace('Watch', '')
    text = text.replace('Full Show Online Free', '')
    return text


def WWEREPLAYSScrape(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find('div', class_={'nag cf'})
    for subdata in data.find_all('div', class_={'thumb'}):
        title = subdata.a['title']
        title = title.encode("utf8") if PY2 else title
        title = CleanWWE(title)
        url = subdata.a['href']
        icon = subdata.img['src']
        addDir("[COLOR yellow][B]%s[/B][/COLOR]" %
               title, url, 30, icon, fanarts, 'Replays From %s' % title)
    try:
        nextpage = soup.find('a', rel={'next'})['href']
        addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
               nextpage, 29, Addonicon, fanart)
    except:
        pass


def WWEREPLAYSGETLINKS(name, url, iconimage):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    r = soup.find_all('a', {'class': 'small cool-blue vision-button'})
    for links in r:
        try:
            source = links['href']
            title = links.text
            if 'pakfashionstore' in source:
                source = ('%s|%s' % (source, url))
                addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                        source, 41, iconimage, fanarts)
        except:
            pass


def ResolvePakFasion(name, url, iconimage):
    url2 = url.split('|')[0]
    ref = url.split('|')[1]
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua,
               'Referer': ref}
    link = requests.get(url2, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    playable = soup.find('iframe')['src'].replace('\n', '')
    PLAYLINK(name, playable, iconimage)


def AdultCheck():
    PornCats()
    # xbmc.executebuiltin('Container.Refresh')
    # if adultpass == '':
    # Message = '[COLOR yellow][B]This Is Your First Time Entering XXX Area, Please Set A Password To Prevent Under Age Usage[/B][/COLOR]'
    # dialog.ok(AddonTitle,Message)
    # string =''
    # keyboard = xbmc.Keyboard(string, '[COLOR white][B]Please Set Your Password[/B][/COLOR]')
    # keyboard.doModal()
    # if keyboard.isConfirmed():
    # string = keyboard.getText()
    # if len(string)>1:
    # term = string.lower()
    # selfAddon.setSetting(id='password', value=string)
    # dialog.notification(AddonTitle, "[COLOR white][B]Password Saved![/B][/COLOR]", Addonicon, 5000)
    # else:
    # dialog.notification(AddonTitle, "[COLOR white][B]Sorry, No Password Was Entered![/B][/COLOR]", Addonicon, 5000)
    # quit()
    # else:
    # string =''
    # keyboard = xbmc.Keyboard(string, '[COLOR yellow][B]Please Enter The Password You Set[/B][/COLOR]')
    # keyboard.doModal()
    # if keyboard.isConfirmed():
    # string = keyboard.getText()
    # if len(string)>1:
    # term = string.lower()
    # current = selfAddon.getSetting(id='password')
    # if current == string:
    # PornCats()
    # else:
    # dialog.notification(AddonTitle, "[COLOR yellow][B]Sorry, Wrong Password[/B][/COLOR]", Addonicon, 5000)
    # quit()
    # else:
    # dialog.notification(AddonTitle, "[COLOR white][B]Sorry, No Password Was Entered![/B][/COLOR]", Addonicon, 5000)
    # quit()


def PornCats():
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(
        'https://www.porntrex.com/categories/', headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find('div', class_={'list'})
    for content in data.find_all('a'):
        heading = content['title']
        url = content['href']
        videos = content.span.text
        title = ('%s | Videos In This Catergory %s' % (heading, videos))
        addDir("[COLOR yellow][B]"+title+"[/B][/COLOR]",
               url, 32, Addonicon, fanarts, title)


def PornContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find_all('div', class_={'video-preview-screen'})
    nextnum = 1
    for content in data:
        checkpriv = content.find('span', class_={'ico-private'})
        if not checkpriv:
            title = content.img['alt']
            title = strip_non_ascii(title)
            url2 = content.a['href']
            icon = content.li['data-src']
            if not 'https:' in icon:
                icon = 'https:'+icon+'|Referer=https://www.porntrex.com/'
            else:
                icon = icon+'|Referer=https://www.porntrex.com/'
            time = content.find('div', class_={'durations'}).text.strip()
            title = ('[COLOR lime]%s | [COLOR yellow]%s[/COLOR]' %
                     (time, title))
            if not 'https:' in icon:
                icon = 'https:' + icon
            addLink(title, url2, 33, icon, fanarts, title)
        else:
            pass
    try:
        if 'from4=' in url:
            getprev = url.split('from4=')[1]
            getprev = int(getprev)
            new = getprev + 1
            nextp = (
                '?mode=async&function=get_block&block_id=list_videos_common_videos_list_norm&sort_by=post_date&from4=%s' % str(new))
            nextpage = url+nextp
            xbmc.log('NEXT PAGE:::%s' % nextpage)
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   nextpage, 32, NextPageImg, fanart)
        else:
            nextp = '?mode=async&function=get_block&block_id=list_videos_common_videos_list_norm&sort_by=post_date&from4=2'
            nextpage = url+nextp
            xbmc.log('NEXT PAGE:::%s' % nextpage)
            addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
                   nextpage, 32, NextPageImg, fanart)
    except:
        pass


def PornLinksResolve(name, url, iconimage):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    pattern = r'''(https://www.porntrex.com/get_file/.*?)['"].*?:\s+['"](.*?)['"]'''
    findlinks = re.findall(pattern, link, flags=re.DOTALL)
    streamurl = []
    streamname = []
    found = 0
    for url, title in findlinks:
        if '.mp4' in url:
            found += 1
            title = title.replace('_', '')
            title = ('[COLOR yellow]Quality : [COLOR lime]%s[/COLOR]' % title)
            streamname.append(title)
            streamurl.append(url)
    if found == 0:
        dialog.notification(
            AddonTitle, '[COLOR yellow]Sorry No Links Available Right Now[/COLOR]', icon, 5000)
        quit()
    else:
        select = dialog.select(name, streamname)
        if select < 0:
            quit()
        PLAYLINK(name, streamurl[select], iconimage)


def DocumentaryContentTop(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find_all('span', itemprop={'itemListElement'})
    for i in data:
        title = i.a['title']
        url = i.a['href']
        try:
            icon = i.img['src']
        except:
            icon = i.img['data-src']
        addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                url, 36, icon, fanarts, title)


def DocumentaryContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find_all('article', class_={'module'})
    for i in data:
        try:
            title = i.a['title']
        except:
            title = i.img['alt']
        title = strip_non_ascii(title)
        url = i.a['href']
        try:
            icon = i.img['src']
        except:
            icon = i.img['data-src']
        desc = i.p.text
        desc = strip_non_ascii(desc)
        addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]",
                url, 36, icon, fanarts, desc)
    try:
        nextpage = soup.find('link', rel={'next'})['href']
        addDir("[COLOR red][B]Next Page --------->[/B][/COLOR]",
               nextpage, 35, NextPageImg, fanart)
    except:
        pass


def DocumentaryCats(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    url = 'https://topdocumentaryfilms.com/'
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    data = soup.find('div', class_={'cat-wrap'})
    for a in data.find_all('a'):
        title = a.text
        url = a['href']
        addDir("[COLOR yellow][B]"+title+"[/B][/COLOR]", url, 35,
               Addonicon, fanarts, 'Documentaries about '+title)


def DocumentaryResolve(name, url, iconimage):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html5lib')
    play = soup.find('meta', itemprop={'embedUrl'})['content']
    PLAYLINK(name, play, iconimage)


def AllSportsNole(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    c = requests.get(url, headers=headers).text
    content = re.findall(
        '<div class="page-content">(.*?)<div\s+id="comments"', c, flags=re.DOTALL)[0]
    pattern = r'''/span>\s+(.*?)<a\s+href=['"](.*?)['"].*?</a>(.*?)<.*?>(.*?)<'''
    FindallGames = re.findall(pattern, content, flags=re.DOTALL)
    for title, url, lang, time in FindallGames:
        title = CLEANUP(title)
        title = ('%s |[COLOR lime] %s | [COLOR aqua] %s[/COLOR]' %
                 (title, lang, time))
        addLink("[COLOR yellow][B]"+title+"[/B][/COLOR]", url,
                39, Addonicon, fanarts, 'Lets Watch Some Sports')


def NolesResolver(name, url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    c = requests.get(url, headers=headers).text
    iframe = re.findall(
        '''<iframe.*?src=['"](.*?)['"]''', c, flags=re.DOTALL)[0]
    d = requests.get(iframe, headers=headers).text
    try:
        play = re.findall('''source:\s+['"](.*?)['"]''', d, flags=re.DOTALL)[0]
    except IndexError:
        play = re.findall('''source:['"](.*?)['"]''', d, flags=re.DOTALL)[0]
    # dialog.ok("PLAY",str(play))
    FinalLink = ('%s|Referer=%s' % (play, iframe))
    PLAYLINK(name, FinalLink, iconimage)


def MAINTENANCE_MENU():
    cachePath = translatePath(os.path.join('special://home/cache'))
    thumbPath = translatePath(os.path.join('special://profile/Thumbnails'))
    packcagesPath = translatePath(
        os.path.join('special://home/addons/packages'))
    downloadfolder = translatePath(os.path.join(
        'special://home/userdata/addon_data/plugin.video.nemesisaio/downloads'))
    folder_size = 0
    for (path, dirs, files) in os.walk(thumbPath):
        for file in files:
            filename = os.path.join(path, file)
            folder_size += os.path.getsize(filename)
    result = "[COLOR aqua]Thumbnails Size =[COLOR yellow] %0.1f MB[/COLOR]" % (
        folder_size/(1024*1024.0))
    addStandardLink(result, 'url2', 999, MaintenanceImg, fanart, '')
    folder_size = 0
    for (path, dirs, files) in os.walk(cachePath):
        for file in files:
            filename = os.path.join(path, file)
            folder_size += os.path.getsize(filename)
    result = "[COLOR aqua]Cache Size =[COLOR yellow] %0.1f MB[/COLOR]" % (
        folder_size/(1024*1024.0))
    addStandardLink(result, 'url2', 999, MaintenanceImg, fanart, '')
    folder_size = 0
    for (path, dirs, files) in os.walk(packcagesPath):
        for file in files:
            filename = os.path.join(path, file)
            folder_size += os.path.getsize(filename)
    result = "[COLOR aqua]Packages Size =[COLOR yellow] %0.1f MB[/COLOR]" % (
        folder_size/(1024*1024.0))
    addStandardLink(result, 'url2', 999, MaintenanceImg, fanart, '')
    addStandardLink("[COLOR white]--------------------------[/COLOR]",
                    'url2', 9999, MaintenanceImg, fanart, '')
    addStandardLink("[COLOR yellow]Cleanup[/COLOR]",
                    'url2', 998, MaintenanceImg, fanart, '')
    addStandardLink("[COLOR white]--------------------------[/COLOR]",
                    'url2', 9999, MaintenanceImg, fanart, '')
    addStandardLink('[COLOR yellow]Force Addon Updates[/COLOR]', 'MOVIES',
                    2000, Addonicon, fanart, description='Update Your Addons')
    addStandardLink("[COLOR yellow]Auth Resolve URL Real Debrid[/COLOR]",
                    'plugin://script.module.resolveurl/?mode=auth_rd', 1000, MaintenanceImg, fanart, '')
    addStandardLink("[COLOR yellow]Auth Resolve URL Premiumize ( Better Than RD )[/COLOR]",
                    'plugin://script.module.resolveurl/?mode=auth_pm', 1000, MaintenanceImg, fanart, '')
    addDir("[COLOR red][B]Dev Test Links ( Danger Beware )[/B][/COLOR]",
           'DEV', 997, MaintenanceImg, fanart)
    xbmc.executebuiltin('Container.SetViewMode(55)')


def clearup():
    cachePath = translatePath(os.path.join('special://home/cache'))
    thumbPath = translatePath(os.path.join('special://profile/Thumbnails'))
    packcagesPath = translatePath(
        os.path.join('special://home/addons/packages'))
    i = [(cachePath, 'Cache'), (thumbPath, 'Thumbnails'),
         (packcagesPath, 'Packages')]
    choice = xbmcgui.Dialog().yesno(AddonTitle,
                                    '[COLOR yellow]Use this function to perform some automatic maintenance! Shall we do the housework for you?[/COLOR]', '', yeslabel='Lets Clean', nolabel='No Thankyou')
    if choice:
        dp.create(AddonTitle, '', '', '')
        dp.update(0)
        for r in i:
            dp.update(50, "[COLOR yellow]Clearing %s[/COLOR]" % r[1])
            time.sleep(1)
            for root, dirs, files in os.walk(r[0]):
                for f in files:
                    if (f.endswith('.log')):
                        continue
                    try:
                        os.unlink(os.path.join(root, f))
                    except:
                        pass
            dp.update(100, "[COLOR yellow]%s Cleaned[/COLOR]" % r[1])
            time.sleep(3)
        dp.close()
        dialog.notification(
            AddonTitle, '[COLOR yellow]Maintenance Completed[/COLOR]', icon, 5000)
        xbmc.executebuiltin('Container.Refresh')
    else:
        quit()


def Forceupdate():
    dialog.notification(
        AddonTitle, '[COLOR yellow]Forcing Repo and Add-On Updates[/COLOR]', icon, 5000)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
    xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
    time.sleep(10)
    dialog.ok(
        AddonTitle, "[B][COLOR yellow]Your Addon Should Have Updated Now[/B][/COLOR]")
    xbmc.executebuiltin('Container.Refresh')


def CHECKSCRAPERS():
    scrapersfolder = translatePath(os.path.join(
        'special://home/addons/' + addon_id, 'resources/scrapers'))
    fileList = os.listdir(scrapersfolder)
    for file in fileList:
        if not file.startswith('__') and file.endswith('.py'):
            updater.ScraperCheck(file)


def Player(name, url, iconimage, desc):
    # dialog.ok("IN","PLAYER")
    if 'limetorrents' in url:
        ua = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
              'AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/65.0.3325.181 Safari/537.36')
        playable = requests.get(url, headers={"User-Agent": ua}).text
        url = re.findall(
            '''href=['"](magnet:\?xt=urn:.*?)=''', playable, flags=re.DOTALL)[0]
    # try:
    dialog.notification(
        AddonTitle, '[COLOR yellow]Sourcing Your Media[/COLOR]', Addonicon, 2500)
    if resolveurl.HostedMediaFile(url).valid_url():
        stream_url = resolveurl.HostedMediaFile(url).resolve()
        liz = xbmcgui.ListItem(name)
        liz.setArt({"thumb": iconimage})
        liz.setInfo('video', {'Plot': desc})
        # stream_url = str(stream_url)
        liz.setPath(stream_url)
        xbmc.Player().play(stream_url, liz, False)
    else:
        stream_url = url
        liz = xbmcgui.ListItem(name)
        liz.setArt({"thumb": iconimage})
        liz.setInfo('video', {'Plot': desc})
        liz.setPath(stream_url)
        xbmc.Player().play(stream_url, liz, False)


def PLAYLINK(name, link, iconimage):

    if 'acestream' in link:
        dialog.notification(
            AddonTitle, '[COLOR skyblue]Resolve Acestream Link Now[/COLOR]', icon, 5000)
        url1 = "plugin://program.plexus/?url=" + link + "&mode=1&name=acestream+"
        liz = xbmcgui.ListItem(name, iconImage=iconimage,
                               thumbnailImage=iconimage)
        liz.setPath(url1)
        xbmc.Player().play(url1, liz, False)
        quit()
    elif 'plugin://' in link:
        xbmc.executebuiltin('RunPlugin('+link+')')
    else:
        try:
            dialog.notification(
                AddonTitle, '[COLOR yellow]Hunting Link Now Be Patient[/COLOR]', Addonicon, 2500)
            hmf = resolveurl.HostedMediaFile(url=link)
            if hmf.valid_url():
                link = hmf.resolve()
            else:
                link = miniresolver.Checker(link)
            xbmcplugin.setResolvedUrl(
                int(sys.argv[1]), True, xbmcgui.ListItem(path=link))
            quit()
        except Exception as e:
            dialog.notification(
                AddonTitle, "[B][COLOR yellow]%s[/B][/COLOR]" % str(e), icon, 5000)
            quit()


def CLEANUP(text):
    text = str(text)
    text = text.replace('\\r', '')
    text = text.replace('\\n', '')
    text = text.replace('\\t', '')
    text = text.replace('\\', '')
    text = text.replace('<br />', '\n')
    text = text.replace('<hr />', '')
    text = text.replace('&#039;', "'")
    text = text.replace('&#39;', "'")
    text = text.replace('&quot;', '"')
    text = text.replace('&rsquo;', "'")
    text = text.replace('&amp;', "&")
    text = text.replace('&#8211;', "&")
    text = text.replace('&#8217;', "'")
    text = text.replace('&#038;', "&")
    text = text.replace('&#8211;', "-")
    text = text.replace('&nbsp;', "")
    text = text.replace('&hellip;', "...")
    text = text.replace('&#8220;', "\"")
    text = text.replace('&#8230;', "...")
    text = text.replace('&#8221;', "\"")
    text = text.lstrip(' ')
    text = text.lstrip('	')
    return text


def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            quit()
            return
        except:
            pass


def GETMULTI(name, url, iconimage):
    dialog = xbmcgui.Dialog()
    streamurl = []
    streamname = []
    streamicon = []
    link = requests.get(url).text
    try:
        urls = re.findall('<title>'+re.escape(name) +
                          '</title>(.+?)</content>', link, flags=re.DOTALL)[0]
    except IndexError:
        urls = re.findall('<title>'+re.escape(name) +
                          '</title>(.+?)</item>', link, flags=re.DOTALL)[0]
    try:
        iconimage = re.findall('<image>(.+?)</image>',
                               urls, flags=re.DOTALL)[0]
    except IndexError:
        iconimage = re.findall(
            '<thumbnail>(.+?)</thumbnail>', urls, flags=re.DOTALL)[0]
    try:
        fanart = re.findall('<poster>(.+?)</poster>', urls, flags=re.DOTALL)[0]
    except IndexError:
        fanart = re.findall('<thumbnail>(.+?)</thumbnail>',
                            urls, flags=re.DOTALL)[0]
    try:
        description = re.findall(
            '<description>(.+?)</description>', urls, flags=re.DOTALL)[0]
    except IndexError:
        description = ''
    description = description.encode("utf8") if PY2 else description
    links = re.findall('<link>(.+?)</link>', urls, flags=re.DOTALL)
    i = 1
    for sturl in links:
        sturl2 = sturl
        if '(' in sturl:
            sturl = sturl.split('(')[0]
            caption = str(sturl2.split('(')[1].replace(')', ''))
            addLink(caption, sturl, 1000, iconimage, fanart, description)
        else:
            title = ('[B][COLOR white]Link %s[/COLOR][/B]' % i)
            addLink(title, sturl, 1000, iconimage, fanart, description)
        i = i+1


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def addDir(name, url, mode, iconimage, fanart, description=''):
    u = "%s?url=%s&mode=%s&name=%s&iconimage=%s&fanart=%s&description=%s" % (sys.argv[0], quote_plus(
        url), mode, quote_plus(name), quote_plus(iconimage), quote_plus(fanart), quote_plus(description))
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setArt({"thumb": iconimage})
    liz.setInfo('video', {'Plot': description})
    view = xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def Pin():
    pin = selfAddon.getSetting('pin')
    if pin == '':
        pin = 'EXPIRED'
    if pin == 'EXPIRED':
        selfAddon.setSetting('pinused', 'False')
        dialog.ok(AddonTitle, "[COLOR yellow]NEW SITE NO MORE POP UPS! Please visit [COLOR lime]https://pinsystem.co.uk[COLOR yellow] to generate an Access Token For [COLOR lime]NemesisAio[COLOR yellow] then enter it after clicking ok[/COLOR]")
        string = ''
        keyboard = xbmc.Keyboard(
            string, '[COLOR red]Please Enter Pin Generated From Website(Case Sensitive)[/COLOR]')
        keyboard.doModal()
        if keyboard.isConfirmed():
            string = keyboard.getText()
            if len(string) > 1:
                term = string.title()
                selfAddon.setSetting('pin', term)
                Pin()
            else:
                quit()
        else:
            quit()
    if not 'EXPIRED' in pin:
        pinurlcheck = (
            'https://pinsystem.co.uk/service.php?code=%s&plugin=RnVja1lvdSE' % pin)
        link = requests.get(pinurlcheck, verify=False).text
        if len(link) <= 2 or 'Pin Expired' in link:
            selfAddon.setSetting('pin', 'EXPIRED')
            Pin()
        else:
            registerpin = selfAddon.getSetting('pinused')
            if registerpin == 'False':
                try:
                    requests.get(
                        'https://pinsystem.co.uk/checker.php?code=99999&plugin=NemesisAio').text
                    selfAddon.setSetting('pinused', 'True')
                except:
                    pass
            else:
                pass


def GetFootball():
    from random import choice
    IE_USER_AGENT = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
    OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97'
    IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1'
    ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 9; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    EDGE_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
    CHROME_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4136.7 Safari/537.36'
    SAFARI_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'

    _USER_AGENTS = [FF_USER_AGENT, OPERA_USER_AGENT,
                    EDGE_USER_AGENT, CHROME_USER_AGENT, SAFARI_USER_AGENT]

    RAND_UA = choice(_USER_AGENTS)
    headers = {'User-Agent': RAND_UA}

    url = 'https://goal.soccerstreamlinks.com/'
    link = requests.get(url, headers=headers)
    soup = BeautifulSoup(link.text, 'html.parser')
    r = soup.find_all('tr', class_=['odd', 'even'])
    for data in r:
        teams = data.find_all('abbr')
        home = teams[0].text
        away = teams[1].text
        url2 = data.a['href']
        icon = data.img['src']
        title = ('%s Vs %s' % (home, away))
        addDir("[COLOR yellow][B]%s[/B][/COLOR]" % title, url2, 12, icon,
               fanart, '[COLOR yellow]%s Sponsored By NemesisAio[/COLOR]' % title)


def GetFootballIndex(name, url, iconimage, fanart, description):
    if 'Soccer Streams' in name:
        url = 'https://soccerstreams-100.com/'
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    link = requests.get(url, headers=Headers).text
    soup = BeautifulSoup(link, 'html5lib')
    content = soup.find_all('div', class_={'post-inner'})
    for data in content:
        title = data.find('h2', class_={'post-title'})
        # dialog.ok("Title",str(title))
        title = title.a.text
        title = title.encode("utf8") if PY2 else title
        link = data.find('h2', {'post-title'}).a['href']
        try:
            icon = data.img['data-large-file']
            icon = icon.split('?')[0]
        except KeyError:
            try:
                icon = data.img['src']
            except:
                icon = AddonIcon
        addDir("[COLOR yellow][B]%s[/B][/COLOR]" % title, link, 12, icon,
               fanart, '[COLOR yellow]%s Sponsored By NemesisAio[/COLOR]' % title)


def Ncaaf(url):
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    siteurl = 'http://sports24.club'
    link = requests.get(url, headers=Headers).text
    soup = BeautifulSoup(link, 'html5lib')
    content = soup.find_all('div', class_={'card-body'})
    for data in content:
        try:
            match = data.h4.text
            time = data.p.text.replace('Scheduled:', '').strip()
            icon = data.find('img', class_={'teamlogo'})['src']
            title = ('%s | %s' % (match, time))
            link = data.a['href']
            if not siteurl in link:
                link = siteurl+link
            addLink('[B][COLOR yellow]' + title + '[/B][/COLOR]',
                    link, 46, icon, fanarts, time)
        except:
            pass


def NcaffResolve(name, url, iconimage):
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    siteurl = 'http://sports24.club'
    link = requests.get(url, headers=Headers).text
    pattern = r'''['"]([^'"]+m3u8.*?)['"]'''
    try:
        play = re.findall(pattern, link, flags=re.DOTALL)[0]
    except:
        dialog.notification(
            AddonTitle, '[COLOR yellow]No Links Available ATM![/COLOR]', icon, 2500)
        quit()
    if not siteurl in play and 'http' not in play:
        play = siteurl+play
    play = play + '|Referer='+url + \
        '&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    PLAYLINK(name, play, iconimage)


def FootBites(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    r = soup.find('div', class_={'wp-content'})
    for games in r.find_all('tr'):
        timedate = games.find_all('td')
        time = timedate[0].text
        title = timedate[1].text
        url = games.a['href']
        name = ('%s | %s' % (time, title))
        name = name.encode("utf8") if PY2 else name
        addLink("[COLOR yellow][B]%s[/B][/COLOR]" % name, url, 48,
                Addonicon, fanarts, '[COLOR yellow]Footie Bites[/COLOR]')


def ResolveFootieBites(url):
    dialog.notification(AddonTitle, 'Attempting To Resolve Link',
                        xbmcgui.NOTIFICATION_INFO, 5000)
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    link = requests.get(url, headers=Headers).text
    try:
        DetectCloudflare = re.findall('''cloudflare''', link)[0]
        if DetectCloudflare:
            dialog.ok(
                "Warning", "Cloudflare Challenge Detected, Try Another Link")
            quit()
    except IndexError:
        pass
    soup = BeautifulSoup(link, 'html5lib')
    pattern = '''data-post=['"](.*?)['"]'''
    links = re.findall(pattern, link)[0]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
               'Referer': url,
               'X-Requested-With': 'XMLHttpRequest'}
    data = {'action': 'doo_player_ajax',
            'post': links,
            'nume': '1',
                    'type': 'movie'}
    if 'footybite' in url:
        posturl = 'http://www.footybite.tv/wp-admin/admin-ajax.php'
    elif 'planetstream' in url:
        posturl = 'http://www.planetstream.ws/wp-admin/admin-ajax.php'
    else:
        quit()
    attempts = 0
    while attempts <= 5:
        c = requests.post(posturl, data=data, headers=headers)
        if c.status_code == 200:
            follow = re.findall('''src=['"](.*?)['"]''', c.content)[0]
            link = requests.get(follow, headers=Headers).text
            try:
                stream = re.findall('''['"]([^'"]+m3u8.*?)['"]''', link)[0]
            except IndexError:
                stream = re.findall('''src=['"](.*?)['"]''', link)[0]
            if not stream.startswith('http:'):
                stream = ('http:%s' % stream)
            if 'wstream' in stream:
                try:
                    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                                'Referer': follow}
                    link2 = requests.get(stream, headers=headers2).text
                    packer = re.compile(
                        '(eval\(function\(p,a,c,k,e,(?:r|d).*)')
                    packed = packer.findall(link2)[0]
                    import jsunpack
                    unpacked = jsunpack.unpack(packed)
                    source = re.compile('''['"](http[^'"]+)['"]''')
                    stream = source.findall(unpacked)[0]
                    stream = (
                        '%s|verifypeer=false&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' % stream)
                except:
                    dialog.notification(
                        AddonTitle, 'Link Failed! Try Closer To Event Start!', xbmcgui.NOTIFICATION_INFO, 5000)
                    quit()
                PLAYLINK(name, stream, Addonicon)
            else:
                finalstream = ('%s|Referer=%s' % (stream, follow))
                PLAYLINK(name, finalstream, Addonicon)
        else:
            attempts += 1
            time.sleep(5)
            dialog.notification(
                AddonTitle, 'Got A Busy Error Trying again in 5 Secounds', xbmcgui.NOTIFICATION_INFO, 5000)


def GetDaddy():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    url = 'https://daddylive.me/'
    link = requests.get(url, headers=headers).text
    content = re.findall('<h[3|4]>(.*?)</p>', link, flags=re.DOTALL)
    pattern2 = r'''([0-9]+:[0-9]+.*?)<.*?href=['"](.*?)['"]'''
    for stuff in content:
        event = re.findall('<span.*?>(.*?)<', stuff, flags=re.DOTALL)[0]
        event = event.encode("utf8") if PY2 else event
        event = event.upper()
        addLink("[COLOR lime][B]"+event+"[/B][/COLOR]", 'link',
                999, Addonicon, fanarts, 'Lets Watch Some Sports')
        matchs = re.findall(pattern2, stuff, flags=re.DOTALL)
        for title, link in matchs:
            match = CLEANUP(title)
            match = match.encode("utf8") if PY2 else match
            addLink("[COLOR yellow][B]%s[/B][/COLOR]" % match, link,
                    51, Addonicon, fanarts, 'Lets Watch Some Sports')


def DaddyResolver(name, url, iconimage, fanart):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    link = requests.get(url, headers=headers).text
    iframe = re.findall(
        '''<iframe\s+src=['"]([^'"]+)['"]''', link, flags=re.DOTALL)
    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Referer': url}
    for pot in iframe:
        # try:
        # import jsunpack
        link2 = requests.get(pot, headers=headers2).text
        source = re.findall(
            '''source.*?['"](.*?)['"]''', link2, flags=re.DOTALL)[0]
        dialog.ok("SOURCE", str(source))

        # packer = re.compile('(eval\(function\(p,a,c,k,e,(?:r|d).*)')
        # packed = packer.findall(link2)[0]
        # unpacked = jsunpack.unpack(packed)
        # source = re.compile('''['"](http[^'"]+)['"]''')
        # stream = source.findall(unpacked)[0]
        stream = ('%s|verifypeer=false&User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36' % source)
        xbmc.log('LINKS :::'+str(stream), xbmc.LOGDEBUG)
        xbmc.log('LINKS :::'+str(stream), xbmc.LOGDEBUG)
        xbmc.log('LINKS :::'+str(stream), xbmc.LOGDEBUG)
        # except:
        # dialog.notification(AddonTitle, 'Link Failed! Try Closer To Event Start!', xbmcgui.NOTIFICATION_INFO, 5000)
        # quit()
        PLAYLINK(name, stream, iconimage)


def StartParty(name, url, iconimage, description):
    def encode(key, string):
        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = ''.join(encoded_chars)
        encoded_string = encoded_string.encode(
            'latin') if six.PY3 else encoded_string
        newstring = base64.urlsafe_b64encode(encoded_string).rstrip(b'=')
        return base64.urlsafe_b64encode(encoded_string).rstrip(b'=')
    if PY2:
        choice = xbmcgui.Dialog().yesno(AddonTitle,
                                        '[COLOR yellow]You Are About to Start A Watch Party For %s?[/COLOR]' % name, '', yeslabel='Start Party', nolabel='No Cancel')
    else:
        choice = xbmcgui.Dialog().yesno(AddonTitle,
                                        '[COLOR yellow]You Are About to Start A Watch Party For %s?[/COLOR]' % name, yeslabel='Start Party', nolabel='No Cancel')
    if choice:
        Play = 0
        sleep = xbmc.sleep
        nameencode = name  # encode('NemesisAio',name)
        media = url  # encode('NemesisAio',url)
        mediaicon = iconimage  # encode('NemesisAio',iconimage)
        mediadesc = description  # encode('NemesisAio',description)
        link = requests.get('http://streamarmy.co.uk/WatchParty/watchparty.php?name=%s&media=%s&icon=%s&desc=%s' %
                            (nameencode, media, mediaicon, mediadesc)).json()
        # dialog.ok("LINK",str(link))
        Countdown = 300
        __INTERVALS = 10
        interval = 1
        Start = time.time()
        Expires = time_left = Countdown
        partycode = link['partycode']
        if PY2:
            line1 = ('Watch Party For : %s' % name)
            line2 = ('Party Code : %s' % partycode)
            line3 = ('Expires in: %s seconds' % Countdown)
            line4 = 'Media Will Start If Someone Joins Party'
            dp.create(line1, line4, line2, line3)
            dp.update(100)
        else:
            line1 = ('Watch Party For : %s' % name)
            line2 = ('Party Code : %s' % partycode)
            line3 = ('Expires in: %s seconds' % Countdown)
            line4 = 'Media Will Start If Someone Joins Party'
            dp.create(AddonTitle, line1+'\n'+line4+'\n'+line2+'\n'+line3)
            dp.update(100)
        while time_left > 0:
            if dp.iscanceled():
                link = requests.get(
                    'http://streamarmy.co.uk/WatchParty/delete.php?code=%s' % partycode)
                break
            for _ in range(__INTERVALS):
                if PY2:
                    sleep(interval * 1000 / __INTERVALS)
                else:
                    sleep(int(interval * 1000 / __INTERVALS))
                time_left = Expires - int(time.time() - Start)
                if time_left < 0:
                    time_left = 0
                progress = time_left * 100 / Expires
                if PY2:
                    line3 = 'Expires in: %s seconds' % time_left if not line3 else ''
                    dp.update(progress, line3=line3)

                else:
                    msg = line1+'\n'+line4+'\n'+line2+'\n'+line3
                    dp.update(int(progress), msg)
                WaitForJ = requests.get(
                    'http://streamarmy.co.uk/WatchParty/check.php?code=%s' % partycode).json()
                StartFilm = WaitForJ['joined']
                if StartFilm == '0':
                    pass
                else:
                    time_left = 0
                    Play = 1
        if time_left <= 0:
            link = requests.get(
                'http://streamarmy.co.uk/WatchParty/delete.php?code=%s' % partycode)
        dp.close()
        if Play == 1:
            dialog.notification(
                AddonTitle, '[COLOR yellow]Enjoy Your Watch Party[/COLOR]', Addonicon, 2500)
            # link = requests.get('http://streamarmy.co.uk/WatchParty/delete.php?code=%s' %partycode)
            hmf = resolveurl.HostedMediaFile(url)
            if hmf.valid_url():
                url = hmf.resolve()
            liz = xbmcgui.ListItem(name)
            liz.setArt({"thumb": iconimage})
            liz.setInfo('video', {'Plot': description})
            # stream_url = str(stream_url)
            liz.setPath(url)
            xbmc.Player().play(url, liz, False)

            # time.sleep(10)
            # while xbmc.Player().isPlaying():
            # Status = requests.get('http://streamarmy.co.uk/WatchParty/check.php?code=%s' %partycode).json()
            # CheckPause = Status['pause']
            # if CheckPause == 'True': xbmc.Player().pause()
            # else:
            # time.sleep(2)
            # pass
            # if xbmc.Player().pause():
            # Status = requests.get('http://streamarmy.co.uk/WatchParty/check.php?code=%s' %partycode).json()
            # CheckPause = Status['pause']
            # if CheckPause == 'False': xbmc.Player().play()
            # else:
            # time.sleep(2)
            # pass
        else:
            dialog.notification(
                AddonTitle, '[COLOR yellow]No Party Joiners[/COLOR]', Addonicon, 2500)


def JoinParty():
    global stop
    stop = 0

    def decode(key, string):
        string = base64.urlsafe_b64decode(string + b'===')
        string = string.decode('latin') if six.PY3 else string
        encoded_chars = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
            encoded_chars.append(encoded_c)
        encoded_string = ''.join(encoded_chars)
        return encoded_string
    string = ''
    keyboard = xbmc.Keyboard(
        string, '[COLOR white][B]Please Enter Party Code[/B][/COLOR]')
    keyboard.doModal()
    if keyboard.isConfirmed():
        partycode = keyboard.getText()
        if len(partycode) > 1:
            partycode = partycode.upper()
            CheckCode = requests.get(
                'http://streamarmy.co.uk/WatchParty/check.php?code=%s' % partycode).json()
            Test = CheckCode['response']
            if Test == 'Valid':
                FilmTitle = CheckCode['name']
                FilmLink = CheckCode['media']
                FilmMedia = CheckCode['icon']
                FilmDesc = CheckCode['desc']
                Title = FilmTitle  # Filmdecode('NemesisAio',str(FilmTitle))
                url = FilmLink  # decode('NemesisAio',str(FilmLink))
                iconimage = FilmMedia  # decode('NemesisAio',str(FilmMedia))
                Description = FilmDesc  # decode('NemesisAio',str(FilmDesc))
                TriggerStart = requests.get(
                    'http://streamarmy.co.uk/WatchParty/triggerstart.php?code=%s' % partycode)
                dialog.notification(
                    AddonTitle, '[COLOR yellow]Enjoy Your Watch Party[/COLOR]', Addonicon, 2500)
                hmf = resolveurl.HostedMediaFile(url)
                if hmf.valid_url():
                    url = hmf.resolve()
                liz = xbmcgui.ListItem(Title)
                liz.setArt({"thumb": iconimage})
                liz.setInfo('video', {'Plot': Description})
                # stream_url = str(stream_url)
                liz.setPath(url)
                xbmc.Player().play(url, liz, False)

                # liz = xbmcgui.ListItem(Title,iconImage=iconimage, thumbnailImage=iconimage)
                # liz.setInfo('video', {'Plot': Description})
                # liz.setPath(url)
                # xbmc.Player ().play(url, liz, False)
                # time.sleep(5)
            else:
                dialog.notification(
                    AddonTitle, '[COLOR yellow]Party Code Invalid or Expired[/COLOR]', Addonicon, 2500)
                quit()
    else:
        quit()


def Sixstream(url):

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    headers = {'User-Agent': ua}

    url = 'http://markkystreams.com/'

    badmatch = ['home', 'schedule', 'iptv']

    link = requests.get(url, headers=headers).text

    soup = BeautifulSoup(link, 'html.parser')

    table = soup.find('div', class_={'navbar-collapse collapse'})

    for items in table.find_all("a"):

        name = items.text

        url = items['href']

        if not any(x in name.lower() for x in badmatch):

            addDir("[COLOR yellow][B]"+name+"[/B][/COLOR]", url,
                   53, Addonicon, fanarts, 'Powered By 6 Sports')


def SixContent(url):

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    headers = {'User-Agent': ua}

    link = requests.get(url, headers=headers).text

    soup = BeautifulSoup(link, 'html.parser')

    table = soup.find_all('figure', class_={'image-holder'})

    for items in table:

        name = items.a['title']
        name = name.encode("utf8") if PY2 else name

        source = items.a['href']

        icon = items['data-original']

        addLink("[COLOR yellow][B]%s[/B][/COLOR]" %
                name, source, 54, icon, fanarts, 'Powered By 6 Sports')


def SixResolve(name, url, iconimage):

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    headers = {'User-Agent': ua,

               'Referer': url}

    link = requests.get(url, headers=headers).text

    sourcelink = re.findall(
        r'''source:\s+['"](.*?)['"]''', link, flags=re.DOTALL)[0]

    PlayIt = ('%s|Referer=%s&User-Agent=%s' % (sourcelink, url, ua))

    PLAYLINK(name, PlayIt, iconimage)


def Soccer24HD(url):
    ua = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    r = requests.get(url, headers=ua).text
    soup = BeautifulSoup(r, 'html.parser')
    matches = soup.find_all('div', class_={'hm_gm_tb_inf1'})
    for i in matches:
        Matchurl = i.a['href']
        Logo = i.img['src']
        kickoff = i.find('div', class_={'given_date'})['data-gamestart']
        Lineup = Matchurl.split('/')[-1].replace('.html', '').replace('-', ' ')
        Lineup = Lineup.encode("utf8") if PY2 else Lineup
        addLink("[COLOR yellow][B]%s[/B][/COLOR]" %
                Lineup, Matchurl, 56, Logo, fanarts, 'Powered By Soccer24HD')


def ResolveSoccer24(name, url, iconimage):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    r = requests.get(url, headers=headers).text
    iframe = re.findall(
        r'''iframe.*?src=['"](.*?)['"]''', r, flags=re.DOTALL)[0]
    headers2 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Referer': url}
    headers3 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Referer': iframe}
    r = requests.get(iframe, headers=headers2).text
    iframe2 = re.findall(
        r'''iframe.*?src=['"](.*?)['"]''', r, flags=re.DOTALL)[0]
    r = requests.get(iframe2, headers=headers3).text
    iframe3 = re.findall(
        r'''iframe.*?src=['"](.*?)['"]''', r, flags=re.DOTALL)[0]
    headers4 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Referer': iframe2}
    r = requests.get(iframe3, headers=headers3).text
    videosource = re.findall(
        r'''dash['"]:['"](.*?)['"]''', r, flags=re.DOTALL)[0]
    final = ('%s|User-Agent=Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36&Referer=%s' %
             (videosource, iframe3))
    # xbmc.log('LINKS :::'+str(final),xbmc.LOGINFO)
    PLAYLINK(name, final, iconimage)


def WatchDocs(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    SiteBase = 'https://watchdocumentaries.com'
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    data = soup.find_all('li', class_={'cat-item'})
    for i in data:
        try:
            name = i.a.text
            url2 = i.a['href']
            if SiteBase in url2 and not 'home' in name.lower():
                addDir("[COLOR yellow][B]"+name+"[/B][/COLOR]", url2, 58,
                       Addonicon, fanarts, 'Powered By Watch Documentaries')
        except Exception:
            pass


def WatchDocsContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    table = soup.find_all('div', class_={'post-item-wrap'})
    for i in table:
        name = i.a['title']
        url2 = i.a['href']
        icon = i.img['data-src']
        desc = i.find('div', class_={'entry-content post-excerpt'}).text
        addLink("[COLOR yellow][B]%s[/B][/COLOR]" %
                name, url2, 59, icon, fanarts, desc)
    try:
        np = re.findall('''['"]([^'"]+)['"]>&raquo''', link, re.DOTALL)[0]
        addDir("[COLOR orange][B]Next Page ---->[/B][/COLOR]", np, 58,
               NextPageImg, fanarts, 'Next Page Powered By Watch Documentaries')
    except Exception:
        pass


def ResolveWatchDocs(name, url, iconimage, description):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua,
               'Referer': url}
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    try:
        source = soup.find('iframe')['src']
    except Exception:
        try:
            source = re.findall('''embedurl['"]:['"](https.*?youtube[^'"]+)['"]''', str(
                soup), re.IGNORECASE)[0].replace('\\', '')
        except Exception:
            source = re.findall('''single_video_url['"]:['"](https.*?[^'"]+)['"]''', str(
                soup), re.IGNORECASE)[0].replace('\\', '')
    PLAYLINK(name, source, iconimage)


def DocHeavenCats(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    SiteBase = 'https://documentaryheaven.com/'
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    content = soup.find('aside', id={'categories'})
    for i in content.find_all('li'):
        title = i.text
        url2 = i.a['href']
        if SiteBase not in url2:
            url2 = SiteBase+url2
        addDir("[COLOR yellow][B]"+title+"[/B][/COLOR]", url2, 61,
               Addonicon, fanarts, 'Powered By Documentary Heaven')


def DocHeavenContent(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua}
    SiteBase = 'https://documentaryheaven.com/'
    link = requests.get(url, headers=headers).text
    soup = BeautifulSoup(link, 'html.parser')
    content = soup.find('div', class_={'row'})
    for i in content.find_all('div', class_={'doc-wrap'}):
        title = i.a['title']
        icon = i.img['src']
        if not SiteBase in icon:
            icon = ('%s%s' % (SiteBase, icon))
        url2 = i.a['href']
        desc = i.p.text
        addLink("[COLOR yellow][B]%s[/B][/COLOR]" %
                title, url2, 62, icon, fanarts, desc)
    try:
        np = soup.find('link', rel={'next'})['href']
        addDir("[COLOR orange][B]Next Page --->[/B][/COLOR]", np, 61,
               NextPageImg, fanarts, 'Next Page Powered By Documentary Heaven')
    except Exception:
        pass


def ResolveDocHeaven(name, url, iconimage, description):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    headers = {'User-Agent': ua,
               'Referer': url}
    link = requests.get(url, headers=headers).text
    source = re.findall(
        '''embedUrl".*?['"](.*?)['"]''', link, re.IGNORECASE)[0]
    PLAYLINK(name, source, iconimage)


def addLink(name, url, mode, iconimage, fanart, description='', family=''):

    u = "%s?url=%s&mode=%s&name=%s&iconimage=%s&fanart=%s&description=%s" % (sys.argv[0], quote_plus(
        url), mode, quote_plus(name), quote_plus(iconimage), quote_plus(fanart), quote_plus(description))
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setArt({"thumb": iconimage})
    liz.setInfo('video', {'Plot': description})
    liz.setProperty('IsPlayable', 'true')
    StartParty = "%s?url=%s&mode=%s&name=%s&iconimage=%s&fanart=%s&description=%s" % (sys.argv[0], quote_plus(
        url), '3000', quote_plus(name), quote_plus(iconimage), quote_plus(fanart), quote_plus(description))
    liz.addContextMenuItems(
        [('[COLOR yellow][B]Start A Watch Party For %s[/COLOR]' % name, 'RunPlugin('+StartParty+')')])
    view = xbmcplugin.setContent(int(sys.argv[1]), 'movies')
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok


def addStandardLink(name, url, mode, iconimage, fanart, description, family=''):

    if not description:
        description = ''
    u = "%s?url=%s&mode=%s&name=%s&iconimage=%s&fanart=%s&description=%s" % (sys.argv[0], quote_plus(
        url), mode, quote_plus(name), quote_plus(iconimage), quote_plus(fanart), quote_plus(description))
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setArt({"thumb": iconimage})
    liz.setInfo('video', {'Plot': description})
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok
###########
# DEBUGGER


def DoDialog(url):
    e = str(url)
    firstpart, secondpart = str(e)[:len(e)/2], str(e)[len(e)/2:]
    messeage = str(firstpart) + '\n' + str(secondpart)
    dialog.ok("URL", str(messeage))


##########
Pin()
params = dict(parse_qsl(sys.argv[2].replace("?", "")))
site = params.get("site", "0")
url = params.get("url", "0")
name = params.get("name", "0")
mode = int(params.get("mode", "0"))
iconimage = params.get("iconimage", "0")
fanart = params.get("fanart", "0")
MovieInfo = description = params.get("description", "0")

if mode == 0 or url == "0" or len(url) < 1:
    GetMenu()
elif mode == 1:
    GetContent(name, url, iconimage, fanart)
elif mode == 2:
    GetListContent(name, url, iconimage)
elif mode == 3:
    GETMULTI(name, url, iconimage)
elif mode == 4:
    TMDBSCRAPE(url)
elif mode == 5:
    YoutubeScrape(url)
elif mode == 6:
    Indexer(name, url, iconimage, fanart, description)
elif mode == 7:
    TMDBSEASONS(url, fanart, description)
elif mode == 8:
    TMDBEPISODES(name, url, fanart, description)
elif mode == 9:
    WhatsOnTv(url)
elif mode == 10:
    ResolveWhatsOnTv(name, url, iconimage)
elif mode == 11:
    GetContentReddit(name, url, iconimage, fanart, description)
elif mode == 12:
    TheMagic(url)
elif mode == 13:
    Twenty7(url)
elif mode == 14:
    ResolveTwenty7(name, url, iconimage)
elif mode == 15:
    RadioWorld(url)
elif mode == 16:
    RadioWorldContent(url)
elif mode == 17:
    RadioWorldContentResolve(name, url, iconimage)
elif mode == 18:
    RadioWorldSearch()
elif mode == 19:
    MusicVideos(url)
elif mode == 20:
    MusicSearch(url)
elif mode == 21:
    SearchYoutube(url)
elif mode == 22:
    Cartoons(url)
elif mode == 23:
    CartoonEpi(name, url, icon)
elif mode == 24:
    CartoonLinks(name, url, iconimage, description)
elif mode == 25:
    WebCamsMenu(url)
elif mode == 26:
    WebCamsContent(name, url, iconimage)
elif mode == 27:
    WebcamsResolve(name, url, iconimage)
elif mode == 28:
    WWEReplaysContent(url)
elif mode == 29:
    WWEREPLAYSScrape(url)
elif mode == 30:
    WWEREPLAYSGETLINKS(name, url, iconimage)
elif mode == 31:
    PornCats()
elif mode == 32:
    PornContent(url)
elif mode == 33:
    PornLinksResolve(name, url, iconimage)
elif mode == 34:
    DocumentaryContentTop(url)
elif mode == 35:
    DocumentaryContent(url)
elif mode == 36:
    DocumentaryResolve(name, url, iconimage)
elif mode == 37:
    DocumentaryCats(url)
elif mode == 38:
    AllSportsNole(url)
elif mode == 39:
    NolesResolver(name, url)
elif mode == 40:
    GetFootball()
elif mode == 41:
    ResolvePakFasion(name, url, iconimage)
elif mode == 42:
    OpenFanime()
elif mode == 43:
    GuiDisplay(title, name, url, iconimage, fanart, description)
elif mode == 44:
    GetFootballIndex(name, url, iconimage, fanart, description)
elif mode == 45:
    Ncaaf(url)
elif mode == 46:
    NcaffResolve(name, url, iconimage)
elif mode == 47:
    FootBites(url)
elif mode == 48:
    ResolveFootieBites(url)
elif mode == 49:
    OpenFightclub()
elif mode == 50:
    GetDaddy()
elif mode == 51:
    DaddyResolver(name, url, iconimage, fanart)
elif mode == 52:
    Sixstream(url)
elif mode == 53:
    SixContent(url)
elif mode == 54:
    SixResolve(name, url, iconimage)
elif mode == 55:
    Soccer24HD(url)
elif mode == 56:
    ResolveSoccer24(name, url, iconimage)
elif mode == 57:
    WatchDocs(url)
elif mode == 58:
    WatchDocsContent(url)
elif mode == 59:
    ResolveWatchDocs(name, url, iconimage, description)
elif mode == 60:
    DocHeavenCats(url)
elif mode == 61:
    DocHeavenContent(url)
elif mode == 62:
    ResolveDocHeaven(name, url, iconimage, description)
elif mode == 63:
    CartoonSelect(url)
elif mode == 64:
    SearchCartoons()
elif mode == 65:
    DisplaySearchCartoons(url)
elif mode == 66:
    OpenSportie()
elif mode == 67:
    OpenXXX()

elif mode == 70:
    WebCamsMenu_coun(url)
elif mode == 996:
    AdultCheck()
elif mode == 997:
    CheckForLists(url)
elif mode == 998:
    clearup()
elif mode == 999:
    MAINTENANCE_MENU()
elif mode == 1000:
    PLAYLINK(name, url, iconimage)
elif mode == 1001:
    PLAYLINK2(name, url, iconimage)
elif mode == 2000:
    Forceupdate()
elif mode == 3000:
    StartParty(name, url, iconimage, description)
elif mode == 3001:
    JoinParty()
elif mode == 4000:
    ChatRoom()
if mode == None or url == None or len(url) < 1:
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=False)
else:
    xbmcplugin.endOfDirectory(int(sys.argv[1]), cacheToDisc=True)
############################################################
# DEBUG CODES
############################################################
# dialog.ok("Debug", str (next_page))
# <a href=\"([^"]*)\">Next</a>
# dialog.notification(AddonTitle, 'Sponsoskyblue By @Nemzzy668', xbmcgui.NOTIFICATION_INFO, 5000)
# str.encode(encoding='UTF-8',errors='strict')
# urllib.urlretrieve ('http://thehill.com/sites/default/files/blogs/trumpmcmaster.jpg')
# |
# xbmc.log('LINKS :::'+str(link),xbmc.LOGNOTICE)
