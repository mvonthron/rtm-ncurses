# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

class Parser(object):
  def canHandle(input):
    pass
  
  def parse(input, display):
    pass


class SystemParser(Parser):
  def canHandle(cmd):
    return cmd.startswith('/')
