from telegram import Update, InputFile, ReplyKeyboardMarkup, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.parsemode import ParseMode
from pprint import pprint
from .message import *
from .buttons import *
from settings import *
from database.db import *

def start(update: Update, context):
    user_id = update.effective_chat.id

    if user_id != ADMIN_ID:
        status = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id).status
        if status in ["member", "administrator", "creator"]:
            try:
                insert(table="index", user_id=user_id, data={"Stage": "start"})
            except:
                upd(table="index", user_id=user_id, data={"Stage": "start"})

            update.message.reply_text(
                text=start_mes.format(update.effective_chat.full_name),
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(start_but, resize_keyboard=True)
            )
            update.message.reply_text(
                text=start_mes2,
                parse_mode=ParseMode.HTML
            )
        else:
            update.message.reply_text(
                text=non_sub_text,
                parse_mode=ParseMode.MARKDOWN_V2,
                reply_markup=InlineKeyboardMarkup(non_sub_but)
            )

        
    else:
        try:
            insert(table="index", user_id=user_id, data={"Stage": "start"})
        except:
            upd(table="index", user_id=user_id, data={"Stage": "start"})
        update.message.reply_text(
            text=admin_start_mes,
            parse_mode=ParseMode.MARKDOWN_V2,
            reply_markup=ReplyKeyboardMarkup(admin_start_but, resize_keyboard=True)
        )

def button_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    # Har doim callback_query ga javob bering
    query.answer()

    if query.data == 'check':
        check(update, context)

    if query.data == "info":
        context.bot.send_message(chat_id = update.effective_chat.id,text=info_message, parse_mode=ParseMode.HTML)
        context.bot.send_message(chat_id = update.effective_chat.id,text=start_mes2, parse_mode=ParseMode.HTML)
    
    if query.data == "stats":
        len_users = len(get(table="users"))
        len_bases = len(get(table="medias"))
        len_service = 0 
        update.message.reply_text(
            text=stats_mes.format(len_users, len_bases, len_service),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(start_but)
        )
        update.message.reply_text(
            text=start_mes2,
            parse_mode=ParseMode.HTML
        )
        
def check(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    user_id = update.effective_chat.id
    message_id = query.message.message_id
    status = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id).status

    if status in ["member", "administrator", "creator"]:
        try:
            insert(table="index", user_id=user_id, data={"Stage": "start"})
        except:
            upd(table="index", user_id=user_id, data={"Stage": "start"})
        
        # Foydalanuvchi kanalga qo'shilgan bo'lsa
        
        context.bot.delete_message(chat_id=user_id, message_id=message_id)
        context.bot.send_message(chat_id=user_id, text="Siz kanalga muvaffaqiyatli qo'shildingiz.")
    else:
        # Foydalanuvchi kanalga qo'shilmagan bo'lsa
        context.bot.delete_message(chat_id=user_id, message_id=message_id)
        context.bot.send_message(chat_id=user_id, text="Iltimos, avval kanalga qo'shiling.",
                reply_markup=InlineKeyboardMarkup(non_sub_but))

def text(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    mess = update.message.text
    status = context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id).status


    if user_id != ADMIN_ID:
        if status in ["member", "administrator", "creator"]:
        
            if mess.isdigit():
                media = get()
            else:
                pass


        else:
        # Foydalanuvchi kanalga qo'shilmagan bo'lsa
            context.bot.delete_message(chat_id=user_id, message_id=message_id)
            context.bot.send_message(chat_id=user_id, text="Iltimos, avval kanalga qo'shiling.",
                reply_markup=InlineKeyboardMarkup(non_sub_but))
     
