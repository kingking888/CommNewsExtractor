#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# 基于行块分布函数的通用网页正文（及图片）抽取 - Python版本:

import requests as req
import re

DBUG = 0

reBODY = re.compile(r'<body.*?>([\s\S]*?)<\/body>', re.I)
reCOMM = r'<!--.*?-->'
reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG = r'<[\s\S]*?>|[ \t\r\f\v]'

reIMG = re.compile(r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>')


class Extractor(object):
    def __init__(self):
        self.url = ""
        self.blockSize = 3
        self.timeout = 5
        self.saveImage = False
        self.rawPage = ""
        self.ctexts = []
        self.cblocks = []

    def processTags(self):
        self.body = re.sub(reCOMM, "", self.body)
        self.body = re.sub(reTRIM.format("script"), "", re.sub(reTRIM.format("style"), "", self.body))
        # self.body = re.sub(r"[\n]+","\n", re.sub(reTAG, "", self.body))
        self.body = re.sub(reTAG, "", self.body)

    def processBlocks(self):
        self.ctexts = self.body.split("\n")
        self.textLens = [len(text) for text in self.ctexts]

        self.cblocks = [0] * (len(self.ctexts) - self.blockSize - 1)
        lines = len(self.ctexts)
        for i in range(self.blockSize):
            self.cblocks = list(map(lambda x, y: x + y, self.textLens[i: lines - 1 - self.blockSize + i], self.cblocks))

        maxTextLen = max(self.cblocks)

        if DBUG: print(maxTextLen)

        self.start = self.end = self.cblocks.index(maxTextLen)
        while self.start > 0 and self.cblocks[self.start] > min(self.textLens):
            self.start -= 1
        while self.end < lines - self.blockSize and self.cblocks[self.end] > min(self.textLens):
            self.end += 1

        return "".join(self.ctexts[self.start:self.end])

    def processImages(self):
        self.body = reIMG.sub(r'{{\1}}', self.body)

    def getContext(self, html):
        # code, self.rawPage = self.getRawPage()
        self.body = re.findall(reBODY, html)[0]

        # if DBUG: print(code, self.rawPage)

        if self.saveImage:
            self.processImages()
        self.processTags()
        res = self.processBlocks()
        # print("res:{}".format(res))
        return res
        # print(len(self.body.strip("\n")))