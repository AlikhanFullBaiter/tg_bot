from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup



select_language = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Қазақша'),
                                                 KeyboardButton(text = 'Русский'),
                                                 KeyboardButton(text = 'English')]],
                                      resize_keyboard=True, input_field_placeholder= 'Тілді таңдаңыз...Выберите язык...Choose a language...')


russian_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Список чатов и каналов')],
        [KeyboardButton(text='Выбор языка')]

    ],
    resize_keyboard=True , input_field_placeholder= 'Выберите чат или канал ...'
)

kazakh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Чаттар мен арналар тізімі')],
        [KeyboardButton(text='Тіл таңдау')]

    ],
    resize_keyboard=True , input_field_placeholder= 'Чатты немесе арнаны таңдаңыз...'
)



english_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='List of chats and channels')],
        [KeyboardButton(text='Choose a language')]

    ],
    resize_keyboard=True , input_field_placeholder= 'Choose chat or channel: '
)


russian_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Чат «Информационная безопасность РК»',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Канал IT SecJobs',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Канал ИНФОБЕЗ',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Чат «Испытание на соответствие информационной безопасности»',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Чат ЕШДИ',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Чат-бот ЕШДИ',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Чат Тоит',url='https://t.me/+c3o3muRUt8tlYmZi' )],
    [InlineKeyboardButton(text='Чат ОЦИБ',url='https://t.me/+c3o3muRUt8tlYmZi' )],
])



kazkah_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='«Қазақстан Республикасының ақпараттық қауіпсіздігі» чаты',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='IT SecJobs арнасы',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='ИНФОБЕЗ арнасы',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='«Ақпарат қауіпсіздігіне сәйкестік сынағы» чаты',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='ЕШДИ чаты',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='ЕШДИ чат-боты',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='ТОИТ чаты',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='ОЦИБ чаты',url='https://t.me/+c3o3muRUt8tlYmZi')]
])



english_select_chat_or_cahnnel = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Chat «Information Security of the Republic of Kazakhstan»',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='IT SecJobs Channel',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='INFOBEZ channel',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='Chat “Information Security Compliance Test”',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='Chat ESHDI',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='Chatbot ESHDI',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='Chat TOIT',url='https://t.me/+c3o3muRUt8tlYmZi')],
    [InlineKeyboardButton(text='Chat OTSIB',url='https://t.me/+c3o3muRUt8tlYmZi')]
])