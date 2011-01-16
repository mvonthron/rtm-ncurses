# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class TitleLine:
  def __init__(self):
    """
    Create title bar

    The title bar has a simple decorative and help purpose
    """
    
    self = curses.newwin(1, curses.COLS, 0, 0)

    self.bkgdset(ord(' '), curses.color_pair(2))
    self.insertln()
    self.addstr(0, 1, 'RTMilk')

    self.refresh()
