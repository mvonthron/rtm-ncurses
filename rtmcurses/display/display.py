# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses

from titleline import TitleLine
from contentwindow import ContentWindow
from statusline import StatusLine
from inputline import InputLine

"""
Display controller of RTM-ncurses
"""
class Display(object):
  
  def __init__(self, stdscr):
    self._stdscr = stdscr
    
    self.init_colors()
    
    # curses windows creation
    self.titleline = TitleLine()
    self.contentwin = ContentWindow()
    self.statusline = StatusLine()
    self.inputline = InputLine()
    self.inputline.listen()
  
  def init_colors(self):
    curses.start_color()
    curses.use_default_colors()
    
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
