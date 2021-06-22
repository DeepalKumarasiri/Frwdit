#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 1813445))
    API_HASH = os.environ.get("API_HASH", "8f45dabd56be5ad1619df16af9eca560")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1814556125:AAECWxWpUYXCRIb18CbhLuWkDh9_4zktv38") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "♨️ **Join our Groups** 👇\n━🇱🇰━◤ **iruPC.net** ◢━🇱🇰━\n ☯️ **@iruPC**\n ☯️ **@MoIndex**\n ☯️ **@Top_Movie_Links**\n━🇱🇰━◤ **iruPC.net** ◢━🇱🇰━")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@hmofficialfilmparadise")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1177233175")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQA8GfmFX3qB0OgAfsWU5UoNI6yQgEVpT4d1yEqKg-lFYHaUpUJf30ygWjjsU_nuOSSXyWJ4BAjQ_0IRYoI0bXcbhzr6CnMQoXmMN9vmqMX1fwQgRTUqrT2qc75SI8KEj4V1USwevA0y3YZkAbDlJacASiZ2PdFT1aunDUg41sGs46_7LzhkviSHNrxE_1MtlzMeDm1DeQB7x_gtIBOiPohUeV8XPyIWtLUVLGNyci-dL_p3rFNmymB6HOB7LrKbP52vvQAVZWEsVdkV328gNB6ETNY4FZ1WxAI-7WZdfuuBFFgujTH4utu0HcYnOqI2WhK9SgHpfcSDUHcFVWSqxB8wU2K9uQA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001404974777))
    REPLACE_USER_NAME = os.environ.get("REPLACE_USER_NAME", "@WMR_")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
