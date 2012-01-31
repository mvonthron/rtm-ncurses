#!/usr/bin/env python

import threading
import time
import signal
import curses.wrapper
import curses.ascii
import locale
import logging
import sys
import webbrowser

from rtmcurses.display.display import Display
from rtmcurses.parsers import *
from rtmcurses.rtmapi import Rtm
from rtmcurses import configuration as conf

def main(stdscr):
    logging.basicConfig(level=logging.DEBUG)

    locale.setlocale(locale.LC_ALL, '')
    code = locale.getpreferredencoding()

    display = Display(stdscr)

    signal.signal(signal.SIGWINCH, display.resize)  
    systemParser = SystemParser(display)
    keyParser    = KeyboardShortcutParser(display)
    
    display.statusline.set_status("connecting")

    api = Rtm(conf.rtm_api_key, conf.rtm_shared_secret, "delete", conf.rtm_token)
    

    if not api.token_valid():
        # manage token retrieval
        url, frob = api.authenticate_desktop()
        # open webbrowser, wait until user authorized application
        webbrowser.open(url)
        raw_input("Continue?")
        # get the token for the frob
        api.retrieve_token(frob)
        # print out new token, should be used to initialize the Rtm object next time
        # (a real application should store the token somewhere)
        print "New token: %s" % api.token
    
    display.statusline.set_status("fetching lists")
    result = api.rtm.lists.getList()
    for l in result.lists:
        display.addView(l.name.lower())

    display.statusline.set_status("idle")

    display.removeView(0)
    display.first()
    
    for i in range(15):
        display.addView("testlen %d" % i)

    while not display.inputline.stopflag:
        input = display.inputline.listen()

        if keyParser.canHandle(input):
            input = keyParser.handle(input)

        if systemParser.canHandle(input):
            systemParser.handle(input)

        else:
            display.write(input)

if __name__ == '__main__':
    curses.wrapper(main)
