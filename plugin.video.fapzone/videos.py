#############################################################
#################### START ADDON IMPORTS ####################
from kodi_six import xbmc, xbmcaddon, xbmcplugin, xbmcgui, xbmcvfs
from six.moves.urllib.parse import parse_qs, quote_plus, urlparse, parse_qsl
from six import PY2
import os
import re
import sys
# import Main
import requests
import pyxbmct
from bs4 import BeautifulSoup
dialog = xbmcgui.Dialog()
translatePath = xbmc.translatePath if PY2 else xbmcvfs.translatePath
#############################################################
#################### SET ADDON ID ###########################
_addon_id_ = 'plugin.video.fapzone'
_self_ = xbmcaddon.Addon(id=_addon_id_)
base_domain = 'https://eporner.com'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
headers = {'User-Agent': ua}
#############################################################
#################### SET ADDON THEME DIRECTORY ##############
_theme_ = _self_.getSetting('Theme')
_images_ = '/resources/' + _theme_
#############################################################
#################### SET ADDON THEME IMAGES #################
Background_Image = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'BG2.jpg'))
# Background_Logo	= translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'model.gif'))
# Background_Logo1	= translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'welcome.gif'))
Listbg = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'listbg.png'))
Addon_Image = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'model.gif'))
Addon_Icon = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'Addon_Icon.png'))
# Stripper = translatePath(os.path.join('special://home/addons/' + _addon_id_ + _images_, 'stripper.gif'))
ButtonbF = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'b2.png'))
ButtonbNF = translatePath(os.path.join(
    'special://home/addons/' + _addon_id_ + _images_, 'b1.png'))
########## Function To Call That Starts The Window ##########


def videowindow(ta):
    global data
    global List
    data = ta
    window = video_window('fapzone')
    window.doModal()
    del window


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
    text = text.lstrip(' ')
    text = text.lstrip('	')
    return text


def passed(self, title):
    # global Media_Title
    # global Media_Link
    global Item_Title
    global Item_Link
    global Item_Desc
    global Item_Icon
    Item_Title = []
    Item_Link = []
    Item_Desc = []
    Item_Icon = []
    title = title.upper()
    Item_Title.append('[COLOR gold]Main ' + title + ' List[/COLOR]')
    Item_Link.append('')
    Item_Desc.append('')
    Item_Icon.append(Addon_Image)
    self.List.addItem('[COLOR yellow]' + title + ' List[/COLOR]')
    self.textbox.setText('')
    self.Show_Logo.setImage(Addon_Image)
    c = requests.get(data, headers=headers).text
    soup = BeautifulSoup(c, 'html5lib')
    content = soup.find_all('div', class_={'mb'})
    for items in content:
        try:
            title = items.img['alt']
            url = items.a['href']
            if not base_domain in url:
                url = base_domain+url
            try:
                icon = items.img['data-src']
            except:
                icon = items.img['src']
            Item_Title.append(title)
            Item_Link.append(url)
            Item_Icon.append(icon)
            self.List.addItem(title)
            Item_Desc.append('')
        except:
            pass
    try:
        np = re.compile(
            '''<link\s+rel=['"]next['"]\s+href=['"](.*?)['"]''').findall(c)[0]
        nextpage = 'NEXT:' + np
        npicon = 'https://i.imgur.com/3eNoY0p.png'
        nptitle = '[COLOR red]Next Page[/COLOR]'
        Item_Title.append(nptitle)
        Item_Link.append(nextpage)
        Item_Icon.append(npicon)
        self.List.addItem(nptitle)
        Item_Desc.append('')
    except:
        pass


def List_Selected(self):

    # dialog.ok("Link",str(Media_Link))
    global Media_Link
    global Media_Title
    global Item_Title
    global Item_Link
    global Item_Desc
    global Item_Icon
    # dialog.ok("LS SELCT",str(Media_Link))
    if 'PLAY:' in Media_Link:
        # dateimport.CHECKDIRS()
        # dateimport.DateCheck()
        # liz = xbmcgui.ListItem(name)
        Media_Link = Media_Link.replace('PLAY:', '')
        liz = xbmcgui.ListItem(Media_Title)
        liz.setArt({"thumb": Media_Icon})
        liz.setInfo('video', {'Plot': Media_Title})
        liz.setPath(Media_Link)
        # Show_List  =  xbmcgui.ListItem(Media_Title)
        xbmc.Player().play(Media_Link, liz, False)
    elif 'NEXT:' in Media_Link:
        Media_Link = Media_Link.replace('NEXT:', '')
        # global Media_Title
        # global Media_Link
        # global Item_Title
        # global Item_Link
        # global Item_Desc
        # global Item_Icon
        Item_Title = []
        Item_Link = []
        Item_Desc = []
        Item_Icon = []
        self.List.reset()
        self.List.setVisible(True)
        title = 'FapZone'
        title = title.upper()
        Item_Title.append('[COLOR gold]Main ' + title + ' List[/COLOR]')
        Item_Link.append('')
        Item_Desc.append('')
        Item_Icon.append(Addon_Image)
        self.List.addItem('[COLOR yellow]' + title + ' List[/COLOR]')
        self.textbox.setText('')
        self.Show_Logo.setImage(Addon_Image)
        c = requests.get(Media_Link, headers=headers).text
        soup = BeautifulSoup(c, 'html5lib')
        content = soup.find_all('div', class_={'mb'})
        for items in content:
            try:
                title = items.img['alt']
                url = items.a['href']
                if not base_domain in url:
                    url = base_domain+url
                try:
                    icon = items.img['data-src']
                except:
                    icon = items.img['src']
                Item_Title.append(title)
                Item_Link.append(url)
                Item_Icon.append(icon)
                self.List.addItem(title)
                Item_Desc.append('')
            except:
                pass
        try:
            np = re.compile(
                '''<link\s+rel=['"]next['"]\s+href=['"](.*?)['"]''').findall(c)[0]
            nextpage = 'NEXT:' + np
            npicon = 'https://i.imgur.com/3eNoY0p.png'
            nptitle = '[COLOR red]Next Page[/COLOR]'
            Item_Title.append(nptitle)
            Item_Link.append(nextpage)
            Item_Icon.append(npicon)
            self.List.addItem(nptitle)
            Item_Desc.append('')
        except:
            pass
    else:
        # global Media_Title
        # global Media_Link
        # global Item_Title
        # global Item_Link
        # global Item_Desc
        # global Item_Icon
        self.List.reset()
        self.List.setVisible(True)
        Item_Title = []
        Item_Link = []
        Item_Desc = []
        Item_Icon = []
        c = requests.get(Media_Link, headers=headers).text
        soup = BeautifulSoup(c, 'html5lib')
        r = soup.find('div', class_={'dloaddivcol'})
        for links in r.find_all('a'):
            link = links['href']
            title = links.text
            title = title.replace('Download', '')
            url = 'PLAY:https://www.eporner.com' + link
            # title = 'Play Video at Quality : ' + quality
            Item_Title.append(title)
            Item_Link.append(url)
            Item_Icon.append(Media_Icon)
            self.List.addItem(title)
            Item_Desc.append('')
#############################################################
######### Class Containing the GUi Code / Controls ##########


class video_window(pyxbmct.AddonFullWindow):
    xbmc.executebuiltin("Dialog.Close(busydialog)")

    def __init__(self, title='fapzone'):
        super(video_window, self).__init__(title)
        self.setGeometry(1280, 720, 100, 50)
        Background = pyxbmct.Image(Background_Image)
        self.placeControl(Background, -10, -1, 123, 52)
        self.set_info_controls()
        self.set_active_controls()
        self.set_navigation()
        self.connect(pyxbmct.ACTION_NAV_BACK, self.close)
        self.connect(self.List, lambda: List_Selected(self))
        # self.connect(self.button1, lambda:nflone(self))
        self.setFocus(self.List)
        passed(self, title)
        self.setFocus(self.List)

    def set_info_controls(self):
        self.Hello = pyxbmct.Label(
            '', textColor='0xFFFFD700', font='font60', alignment=pyxbmct.ALIGN_CENTER)
        self.placeControl(self.Hello, -4, 1, 1, 50)
        self.List = pyxbmct.List(
            buttonFocusTexture=Listbg, _space=9, _itemTextYOffset=-4, textColor='0xFF013d11')
        self.placeControl(self.List, 20, 0, 100, 33)
        self.textbox = pyxbmct.TextBox(textColor='0xFFFFD700')
        self.placeControl(self.textbox, 95, 18, 30, 30)
        self.Show_Logo = pyxbmct.Image('')
        self.placeControl(self.Show_Logo, -6, 41, 36, 8)
        self.connectEventList(
            [pyxbmct.ACTION_MOVE_DOWN,
             pyxbmct.ACTION_MOVE_UP,
             pyxbmct.ACTION_MOUSE_WHEEL_DOWN,
             pyxbmct.ACTION_MOUSE_WHEEL_UP,
             pyxbmct.ACTION_MOUSE_MOVE],
            self.List_update)

    def set_active_controls(self):
        pass
        # self.button11 = pyxbmct.Button('',   noFocusTexture=Addon_Icon, focusTexture=Addon_Icon)
        # self.placeControl(self.button11, -4, 42,  20, 8)
        # self.button12 = pyxbmct.Button('',   noFocusTexture=Background_Logo1, focusTexture=Background_Logo1)
        # self.placeControl(self.button12, -4, 16,  25, 26)
        # self.button13 = pyxbmct.Button('',   noFocusTexture=Stripper, focusTexture=Stripper)
        # self.placeControl(self.button13, 0, 1,  106, 13)

    def set_navigation(self):
        # set the navigation for if user presses Right when eliment if focused
        pass

    def List_update(self):
        global Media_Title
        global Media_Link
        global Media_Desc
        global Media_Icon
        try:
            if self.getFocus() == self.List:
                position = self.List.getSelectedPosition()
                Media_Title = Item_Title[position]
                Media_Link = Item_Link[position]
                Media_Desc = Item_Desc[position]
                self.textbox.setText(Media_Desc)
                self.textbox.autoScroll(1000, 1000, 1000)
                if Item_Icon[position] is not None:
                    Media_Icon = Item_Icon[position]
                    self.Show_Logo.setImage(Media_Icon)
                else:
                    Media_Icon = 'http://via.placeholder.com/300x220/13b7ff/FFFFFF?text=' + Media_Title
                    self.Show_Logo.setImage(Media_Icon)
        except (RuntimeError, SystemError):
            pass
