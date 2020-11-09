#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#basic version

import asyncio
import os
import sqlite3
import time

from sample_config import Config
from translation import Translation

import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait


@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_MSG,
    )
   

@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_MSG,
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_MSG,
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["test"]))
async def test(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.TEST_MSG,
        reply_markup=InlineKeyboardMarkup(
       [
         [
         InlineKeyboardButton('📍SUPPORT CHANNEL📍', url='https://t.me/MaxxBots'),
         InlineKeyboardButton('👲 FEEDBACK 👲', url='https://t.me/MaxxWizard_Bot')
         ],
         [
         InlineKeyboardButton('👤LEECH GROUP👤', url='https://t.me/MaxxLeechPro'),
         InlineKeyboardButton('🗣️HELP GROUP🗣️', url='https://t.me/MaxxBotChat')
         ]
       ]
      )
    )
    return


@pyrogram.Client.on_message(pyrogram.Filters.document | Filters.video | Filters.photo)
async def old(client, message):
    await client.edit_message_reply_markup(
        chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=InlineKeyboardMarkup(
            [
            [InlineKeyboardButton('👥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣 👥', url='https://t.me/joinchat/R02KIFkSJaW9vyyGZmhHiQ')],
            [InlineKeyboardButton('👲 𝗟𝗘𝗘𝗖𝗛 𝗚𝗥𝗢𝗨𝗣 👲 ', url='https://t.me/joinchat/AAAAAFarWaHcm9oVv-OyAA')]
            ]  
        )
    )
    
  
        
    
                          
