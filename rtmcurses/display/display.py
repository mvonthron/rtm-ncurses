# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses
from collections import namedtuple

from titleline import TitleLine
from contentwindow import ContentWindow
from statusline import StatusLine
from inputline import InputLine

from rtmcurses import configuration

View = namedtuple('View', 'x, y, buffer')

"""
Display controller of RTM-ncurses
"""
class Display(object):
  
  def __init__(self, stdscr):
    self._stdscr = stdscr
    self.init_colors()
    
    # views
    self.views       = {
      'default': View(0, 0, "Window 0\n default"),
    }
    self.positions   = ['default']
    self.curr_viewid = 0
    self.nb_views    = 1
    
    # screen variables
    self.view_h     = curses.LINES-5
    self.view_width = curses.COLS
    self.pad_height = configuration.max_view_height
    self.pad_width  = self.nb_views*self.view_width
    
    # curses windows creation
    self.titleline  = TitleLine()
    self.contentwin = ContentWindow()
    self.statusline = StatusLine()
    self.inputline  = InputLine()
    self.inputline.set_prefix("channel")
    
  
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
    if name in self.views:
      raise Exception("Invalid name")
    
    self.views[name] = View(self.nb_views*curses.COLS, 0, buffer)
    self.nb_views = len(self.views)
    self.pad_width += self.view_width
    self.contentwin.resize_pad(self.pad_width, self.pad_height)

    if not pos is None and isinstance(pos, int):
      self.positions.insert(pos, name)
    else:
      self.positions.append(name)

    # something cleaner ?
    self.contentwin.fillFromViews(self.views)


  def removeView(self, name):
    """remove view"""
    
    if isinstance(name, str):
      pass # remove from name
    elif isinstance(name, int):
      pass # remove from pos
    else:
      raise Exception()
    
  def swapViews(self, view1, view2):
    """swap views"""
    pass
  
  def switchToView(self, view):
    """switch active view"""
    if isinstance(view, int):
      view = self.positions[view]
      
    if isinstance(view, str):
      self.contentwin.refresh(self.views[view].x, self.views[view].y)
      self.curr_viewid = self.positions.index(view)
    else:
      raise Exception()

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
