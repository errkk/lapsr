#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from lib.TextStar import TextStar

display = TextStar('/dev/ttyAMA0')
display.sendCmd('Hello World!')   
