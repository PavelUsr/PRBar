#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py PavelUser 
#
#  Copyright 2019 rv <rv@rv-System>
#  Запускать в терминале
#
#
import prbar
import time
tst = time.time()
bar =  prbar.PrBar(maxval =100000,lenbar=25,text='')
for n in range(bar.maxval+1):
	bar.text = "{}".format(int(time.time()-tst))
	bar.run(n)

bar.endpr()
print("finih -)")

