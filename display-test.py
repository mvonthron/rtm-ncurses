#!/usr/bin/env python

import threading
import time
import curses.wrapper
import locale
import logging

from rtmcurses.display.display import Display
from rtmcurses.parsers import SystemParser


def main(stdscr):
  logging.basicConfig(level=logging.DEBUG)
  
  locale.setlocale(locale.LC_ALL, '')
  code = locale.getpreferredencoding()
  
  display = Display(stdscr)
  #display.contentwin.writetask()
  #display.contentwin.writetask2()
  
  while not display.inputline.stopflag:
    input = display.inputline.listen()
    if input == "/quit":
      display.inputline.stop()
      
    elif input.startswith("set prefix "):
      display.inputline.set_prefix(input.lstrip("set prefix "))
      
    #~ elif input.startswith('/'):
      #~ SystemParser.parser(input, display)
      
    elif input == "/next":
      display.next()
    
    elif input == "/add":
      logging.debug("pre add view :\n  %s - %s" % (display.views, display.positions))
      logging.debug("  view: %d, %d  pad: %d, %d" % (display.contentwin.view_width, display.contentwin.view_height, display.contentwin.pad_width, display.contentwin.pad_height))
      
      display.addView('system', buffer="Window 1\n  system")
      
      logging.debug("post add view :\n  %s - %s" % (display.views, display.positions))
      logging.debug("  view: %d, %d  pad: %d, %d" % (display.contentwin.view_width, display.contentwin.view_height, display.contentwin.pad_width, display.contentwin.pad_height))
      
      
      display.addView('overview', buffer="Window 2\n overview")
      
      logging.debug("post add view :\n  %s - %s" % (display.views, display.positions))
      logging.debug("  view: %d, %d  pad: %d, %d" % (display.contentwin.view_width, display.contentwin.view_height, display.contentwin.pad_width, display.contentwin.pad_height))

    elif input == "/prev":
      display.prev()
      
    elif input == "/clear":
      display.clear()
    
    else:
      display.contentwin.println(input)


if __name__ == '__main__':
  curses.wrapper(main)
