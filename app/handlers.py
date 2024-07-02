
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Filter

import app.keyborads as kb

router = Router()

class TextIn(Filter):
    def __init__(self, *texts):
        self.texts = texts

    async def __call__(self, message: Message) -> bool:
        return message.text in self.texts

@router.message(CommandStart())
async def cmd_start(message: Message):
    welcome_message_text = (
        "Қош келдіңіз! Добро пожаловать! Welcome!\n"
        "Тілді таңдаңыз | Выберите язык | Select a language"
    )
    await message.answer(welcome_message_text,
                         reply_markup=kb.select_language)


@router.message(TextIn( 'Выбор языка', 'Тіл таңдау', 'Choose a language'))
async def choose_language(message : Message):
    welcome_message_text = (
        "Қош келдіңіз! Добро пожаловать! Welcome!\n"
        "Тілді таңдаңыз | Выберите язык | Select a language"
    )
    await message.answer(welcome_message_text,
                         reply_markup=kb.select_language)


@router.message(F.text == 'Русский')
async def cmd_russian_welcome(message: Message):
    russian_welcome_message_text = (
        "Добрый день! Этот бот хранит список телеграмм чатов и каналов, выберите действие:"
    )
    await message.answer(russian_welcome_message_text,
                         reply_markup=kb.russian_menu)


@router.message(F.text == 'Список чатов и каналов')
async def list_chat_russian(message: Message):
    russian_choose_chat = (
        "Выберите чат или канал:"
    )
    await message.answer(russian_choose_chat,
                         reply_markup=kb.russian_select_chat_or_cahnnel)




@router.message(F.text == 'Қазақша' )
async def cmd_kazakh_welcome(message: Message):
    kazakh_welcome_message_text = (
        "Қайырлы күн! Бұл бот телеграмм чаттары мен арналарының тізімін сақтайды, әрекетті таңдаңыз::"
    )
    await message.answer(kazakh_welcome_message_text,
                         reply_markup= kb.kazakh_menu)

@router.message(F.text == 'Чаттар мен арналар тізімі')
async def list_chat_kazakh(message: Message):
    kazakh_choose = (
        "Чатты немесе арнаны таңдаңыз: "
    )
    await message.answer(kazakh_choose,
                         reply_markup=kb.kazkah_select_chat_or_cahnnel)


@router.message(F.text == 'English')
async def cmd_english_welcome(message: Message):
    english_welcome_message_text = (
        "Good afternoon This bot stores a list of telegram chats and channels, select an action:"
    )
    await message.answer(english_welcome_message_text,
                         reply_markup=kb.english_menu)

@router.message(F.text == 'List of chats and channels')
async def list_chat_english(message: Message):
    english_choose = (
        "Select a chat or channel:"
    )
    await message.answer(english_choose,
                         reply_markup=kb.english_select_chat_or_cahnnel)
