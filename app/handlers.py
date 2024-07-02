
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

import app.keyborads as kb

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_message_text = (
        "Қош келдіңіз! Добро пожаловать! Welcome!\n"
        "Тілді таңдаңыз | Выберите язык | Select a language"
    )
    await message.answer(welcome_message_text,
                         reply_markup = kb.select_language)


@router.message(F.text == 'Русский')
async def cmd_russian(message: Message):
    russian_welcome_message_text = (
        "Добрый день! Это официальный бот Национальной службы реагирования на компьютерные инциденты KZ-CERT.\n"  # текст 
        "Для продолжения выберите один из представленных ниже разделов:"
    )
    await message.answer(russian_welcome_message_text,
                         reply_markup=kb.russian_select_chat_or_cahnnel)


@router.message(F.text == 'Қазақша')
async def cmd_russian(message: Message):
    kazakh_welcome_message_text = (
        "Қайырлы күн! Бұл KZ-CERT компьютерлік инциденттерге әрекет етудің ұлттық қызметінің ресми боты.\n" # текст
        "Жалғастыру үшін төмендегі бөлімдердің бірін таңдаңыз:"
    )
    await message.answer(kazakh_welcome_message_text,
                         reply_markup= kb.kazkah_select_chat_or_cahnnel)



@router.message(F.text == 'English')
async def cmd_russian(message: Message):
    english_welcome_message_text = (
        "Good afternoon! This is the official bot of the National Computer Incident Response Service KZ-CERT.\n"  # текст
        "Please select one of the sections below to continue:"
    )
    await message.answer(english_welcome_message_text,
                         reply_markup=kb.english_select_chat_or_cahnnel)


