# repository.streamarmy18-19-Deobfuscated

## A full fork of https://github.com/nemesis668/repository.streamarmy18-19
## All obfuscated files de-obfuscated for your perusal.
## Original Obfuscated files renamed to file_py.obf


This repo is to demonstrate the pinsystem requirements and other possibly malicious
code from StreamArmy repo addons.

This includes the nemzzy service (script.module.nemzzy) is a script that is part of the
StreamArmy addons and is run as a service inside Kodi.
This script installs and loads a windows dll or android .so - ( possibly admaven )
https://www.ad-maven.com

These files function is not known at this time.

The service will run at Kodi's start and then again every time one of the StreamArmy Addons is used.
Every time it is run it checks if the dll or .so file is installed, or needs updating then it
runs the library and attaches it to the Kodi Process

The suspicious dlls and libraries are contained in nemzzy's addon and available for your inspection here
The XXX-O-DUS plugin has some code added to override some menu options.
The new menu has some additional functionality and improved version information.
There is a cache clean function that for now, only clears the thumbcache but will
do more, in the fullness of time.

Enjoy!

https://github.com/nemesis668/repository.streamarmy18-19/tree/main/script.module.nemzzy/lib

The original addon script source for script.module.nemzzy can be inspected here:
https://github.com/nemesis668/repository.streamarmy18-19/tree/main/script.module.nemzzy
The key files are obfuscated however.

NOTE:
    At the time of writing I had spent several hours on a windows virtual machine
    figuring out what is happening inside the nemzzy service script
    I have not conclusively determined what the dll does nor managed to intercept
    any internet traffic initiated by the dll.
    What I do know is that the dll's are started by the service, attached to the Kodi
    process and then terminated when Kodi closes.
