# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses

from titleline import TitleLine
from contentwindow import ContentWindow
from statusline import StatusLine
from inputline import InputLine

from rtmcurses import configuration

"""
Display controller of RTM-ncurses
"""
class Display(object):
  
  def __init__(self, stdscr):
    self._stdscr = stdscr
    self.init_colors()
    
    # curses windows creation
    self.titleline  = TitleLine()
    self.contentwin = ContentWindow()
    self.statusline = StatusLine()
    self.inputline  = InputLine()
    self.inputline.set_prefix("channel")
    
    #
    self.positions   = []
    self.views       = {}
    self.curr_viewid = 0
    self.nb_views    = 1
    
  
  def init_colors(self):
    curses.start_color()
    curses.use_default_colors()
    
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)


  #
  # view management methods
  #
  def addView(self, name, buffer="", pos=None):
    """Add a view to the display.
    if pos is none: placed at the end
    """
    pass

  def removeView(self, name):
    if isinstance(name, str):
      pass # remove from name
    elif isinstance(name, int):
      pass # remove from pos
    else:
      raise Exception()
    
  def swapViews(self, view1, view2):
    pass
    
  def switchToView(self, name):
    pass

  def next(self):
    """switch to next view: manage contentwin as well as status, etc."""
    if self.curr_viewid != self.nb_views-1:
      self.switchToView(self.curr_viewid + 1)
    else:
      # already at last view
      pass

  def prev(self):
    """switch to previous view"""
    if self.curr_viewid > 0:
      self.switchToView(self.curr_viewid - 1)
    else:
      pass
  
  def setName(self, new_name, view=None):
    """change name of the current views, affects views list as well as prefix on input bar"""
    self.inputline.set_prefix(new_name)
    
  #
  # content management methods
  #
  def clear(self, view=None):
    """clear content in targeted view, current if arg is omitted"""
    pass
    
  def println(self, content="", view=None):
    """print content into view, current if arg is omitted"""
    pass
