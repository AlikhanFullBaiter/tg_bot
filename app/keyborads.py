from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup



select_language = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Қазақша'),
                                                 KeyboardButton(text = 'Русский'),
                                                 KeyboardButton(text = 'English')]],
                                      resize_keyboard=True, input_field_placeholder= 'Тілді таңдаңыз...Выберите язык...Choose a language...')



russian_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Чат «Информационная безопасность РК»' , url='')],
    [InlineKeyboardButton(text='Канал IT SecJobs', url='')],
    [InlineKeyboardButton(text='Канал ИНФОБЕЗ', url='')],
    [InlineKeyboardButton(text='Чат «Испытание на соответствие информационной безопасности»', url='')],
    [InlineKeyboardButton(text='Чат ЕШДИ', url='')],
    [InlineKeyboardButton(text='Чат-бот ЕШДИ', url='')],
    [InlineKeyboardButton(text='Чат ТОИТ', url='')],
    [InlineKeyboardButton(text='Чат ОЦИБ', url='')]
])



kazkah_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='«Қазақстан Республикасының ақпараттық қауіпсіздігі» чаты', url='')],
    [InlineKeyboardButton(text='IT SecJobs арнасы', url='')],
    [InlineKeyboardButton(text='ИНФОБЕЗ арнасы', url='')],
    [InlineKeyboardButton(text='«Ақпарат қауіпсіздігіне сәйкестік сынағы» чаты', url='')],
    [InlineKeyboardButton(text='ЕШДИ чаты', url='')],
    [InlineKeyboardButton(text='ЕШДИ чат-боты', url='')],
    [InlineKeyboardButton(text='ТОИТ чаты', url='')],
    [InlineKeyboardButton(text='ОЦИБ чаты', url='')]
])



english_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Chat «Information Security of the Republic of Kazakhstan»', url='')],
    [InlineKeyboardButton(text='IT SecJobs Channel', url='')],
    [InlineKeyboardButton(text='INFOBEZ channel', url='')],
    [InlineKeyboardButton(text='Chat “Information Security Compliance Test”', url='')],
    [InlineKeyboardButton(text='Chat ESHDI', url='')],
    [InlineKeyboardButton(text='Chatbot ESHDI', url='')],
    [InlineKeyboardButton(text='Chat TOIT', url='')],
    [InlineKeyboardButton(text='Chat OTSIB', url='')]
])