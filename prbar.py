#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prbar.py 15.05.2019
#
#  Copyright 2019 rv <rv@rv-System>
#
# My bar Прогресс PavelUser
#
#    Пример:
#    import prbar
#    bar =  prbar.PrBar(maxval =100000,lenbar=50,text='12:05')
#    for n in range(bar.maxval+1):
#       bar.run(n)
#    bar.endpr()


from sys import stdout

class PrBar:

    def __init__(self,maxval=100,mark='#',lenbar=25,text=''):
        self.maxval = maxval
        self.marker = mark
        self.lenbar = lenbar
        self.text = text


    def run(self,val):
        Bar = ''
        pr = val*100//self.maxval
        kl = val*self.lenbar//self.maxval
        for n in range(self.lenbar):
            if n < kl:
                Bar += self.marker
            else:
                Bar +=" "
        S1 = "\r{:3}% [{}] {}/{} {} ".format(pr,Bar,val,self.maxval,self.text)
        stdout.write(S1)
        stdout.flush()
        return

    def endpr(self):
        del (self)
        print
        return


