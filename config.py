#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 1469098))
    API_HASH = os.environ.get("API_HASH", "f7d877ef7d619f858d8dc27ac7a121e5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1814556125:AAECWxWpUYXCRIb18CbhLuWkDh9_4zktv38") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "♨️ **Join our Groups** 👇\n━🇱🇰━◤ **iruPC.net** ◢━🇱🇰━\n ☯️ **@iruPC**\n ☯️ **@MoIndex**\n ☯️ **@Top_Movie_Links**\n━🇱🇰━◤ **iruPC.net** ◢━🇱🇰━")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@anonyirupc")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1177233175")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQCQe1CkIDHWooV4l2qpm1Fwrx55ALrYNph9UZ0ZNwnYzCpkg9TVm9vSs0drnl70ras3kI1fREU1ea69yjxXOu0lRUUnflf_QbTdOisIK9Fq64qxgyntxjsZWga-lE6lxs9F6MciOT3sPe02ZCxAhQunRsLMs2n54ibZG_lsEOwvTu0iYk4bDxxiccfr4WOzXrgOqHMZ52zK-HjNadybtti3Rm-sO126iwU1-ftYm7c2_8pCBgPDwzqhLkhEDKnLKJvdxDCIUpnnu7PN5YWLKL3b4_wPEV4IH1rMAW74_40H3c7ym2CRQg2yCt_WdNd-As_PWGwb9nom2bPEAzciNTK7RisnFwA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001359244042))
    REPLACE_USER_NAME = os.environ.get("REPLACE_USER_NAME", "@WMR_")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
