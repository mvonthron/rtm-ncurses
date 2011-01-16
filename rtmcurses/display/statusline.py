# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class StatusLine:
  
  def __init__(self):
    """
    Create status bar

    The status bar lists available channels
    """
    self = curses.newwin(1, curses.COLS, curses.LINES-2, 0)

    self.bkgdset(ord(' '), curses.color_pair(2))
    self.insertln()
    self.addstr(0, 1, '(connected) [1] overview [2] work [3] system')
  
    self.refresh()
