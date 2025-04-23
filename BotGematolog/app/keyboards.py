from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

back_to_main_menu = InlineKeyboardButton(text='Главное меню', callback_data='back')

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Информация'), KeyboardButton(text='Консультация')]
],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню.')

online = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Онлайн Консультация', url='https://t.me/hematologist_Sokolova/255')]
])

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Гены системы крови', callback_data='gens'),
     InlineKeyboardButton(text='Анемии', callback_data='anemys')
     ],
    [InlineKeyboardButton(text='Микроэлементы', callback_data='micro_elem'),
     InlineKeyboardButton(text='Тромбоциты', url='https://t.me/hematologist_Sokolova/160 ')
     ],
    [InlineKeyboardButton(text='Лейкоциты', callback_data='leykocits'),
     InlineKeyboardButton(text='Порфирия', url='https://t.me/hematologist_Sokolova/250 ')
     ],
    [InlineKeyboardButton(text='АФС', callback_data='afs'),
     InlineKeyboardButton(text='ЭКО и система крови', url='https://t.me/hematologist_Sokolova/206 ')
     ],
    [InlineKeyboardButton(text='КОК и тромбофилия', url='https://t.me/hematologist_Sokolova/113 ')],
    [InlineKeyboardButton(text='Наследственная тромбофилия', callback_data='trombofilia')],
    [InlineKeyboardButton(text='Железодефицитная анемия и дефицит железа', callback_data='anemy')],
    [InlineKeyboardButton(text='Повышенный уровень ферритина', callback_data='ferritin')],
    [InlineKeyboardButton(text='Фолиеводефицитная и витамин B12 дефицитная анемия',
                          url='https://t.me/hematologist_Sokolova/59 ')],
    [InlineKeyboardButton(text='Правила сдачи анализов крови', url='https://t.me/hematologist_Sokolova/37 ')],
    [InlineKeyboardButton(text='Ретрохориальные гематомы во время беременности',
                          url='https://t.me/hematologist_Sokolova/167 ')],
    [InlineKeyboardButton(text='Анализы крови и беременность', callback_data='analisys')],
    [InlineKeyboardButton(text='Детская гематология', callback_data='child')]
])

kb_anemy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Железо и питание', url='https://t.me/hematologist_Sokolova/156 '),
     InlineKeyboardButton(text='6 мифов об анемии', url='https://t.me/hematologist_Sokolova/106 ')
     ],
    [InlineKeyboardButton(text='Внутримышечные инъекции препаратов железа',
                          url='https://t.me/hematologist_Sokolova/196 ')],
    [InlineKeyboardButton(text='Препараты для восполнения дефицита железа',
                          url='https://t.me/hematologist_Sokolova/65 ')],
    [InlineKeyboardButton(text='Почему важно лечить железодефецитную анемию?',
                          url='https://t.me/hematologist_Sokolova/36 ')],
    [InlineKeyboardButton(text='Терапия ЖДА', url='https://t.me/hematologist_Sokolova/11 ')],
    [back_to_main_menu]
])

kb_ferritin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Что делать, если ферритин повышен?', url='https://t.me/hematologist_Sokolova/171')],
    [InlineKeyboardButton(text='Повышенный ферритин: стоит ли беспокоиться?',
                          url='https://t.me/hematologist_Sokolova/128 ')],
    [back_to_main_menu]
])

kb_gens = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мутация PAI-1', url='https://t.me/hematologist_Sokolova/191 '),
     InlineKeyboardButton(text='Генетика и фолатный цикл', url='https://t.me/hematologist_Sokolova/146 ')
     ],
    [back_to_main_menu]
])

kb_anemys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Талассемия и беременность', url='https://t.me/hematologist_Sokolova/259 '),
     InlineKeyboardButton(text='Хроническая анемия', url='https://t.me/hematologist_Sokolova/58')
     ],
    [InlineKeyboardButton(text='Анемия у женщин', url='https://t.me/hematologist_Sokolova/54 ')],
    [InlineKeyboardButton(text='Можно ли вылечить анемию навсегда?', url='https://t.me/hematologist_Sokolova/45 ')],
    [InlineKeyboardButton(text='Виды анемии: классификация «на пальцах»',
                          url='https://t.me/hematologist_Sokolova/29 ')],
    [InlineKeyboardButton(text='Причины возникновения дефицитной анемии', url='https://t.me/hematologist_Sokolova/32 ')],
    [back_to_main_menu]
])

kb_micro_elem = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Цинк', url='https://t.me/hematologist_Sokolova/176 '),
     InlineKeyboardButton(text='Ферритин: Как сдать анализ', url='https://t.me/hematologist_Sokolova/46 ')
     ],
    [InlineKeyboardButton(text='Препараты фолиевой кислоты', url='https://t.me/hematologist_Sokolova/139 ')],
    [InlineKeyboardButton(text='B12 дефицитная анемия', url='https://t.me/hematologist_Sokolova/50')],
    [InlineKeyboardButton(text='Фолиевая кислота (витамин В9)', url='https://t.me/hematologist_Sokolova/134 ')],
    [back_to_main_menu]
])

kb_leykocits = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лейкопения', url='https://t.me/hematologist_Sokolova/217 '),
     InlineKeyboardButton(text='Лейкоцитоз', url='https://t.me/hematologist_Sokolova/211 ')
     ],
    [back_to_main_menu]
])

kb_trombofilia = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назначили клексан, но страшно колоть', url='https://t.me/hematologist_Sokolova/79 ')],
    [InlineKeyboardButton(text='Диагностика и лечение тромбофилии у беременных',
                          url='https://t.me/hematologist_Sokolova/74 ')],
    [InlineKeyboardButton(text='Тромбофилия: Критерии диагностики у беременных',
                          url='https://t.me/hematologist_Sokolova/69 ')],
    [InlineKeyboardButton(text='Тромбофилия у беременных', url='https://t.me/hematologist_Sokolova/64 ')],
    [back_to_main_menu]
])

kb_afs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Антифосфолипидный синдром (АФС)', url='https://t.me/hematologist_Sokolova/85 ')],
    [InlineKeyboardButton(text='АФС: Планирование беременности', url='https://t.me/hematologist_Sokolova/109 ')],
    [InlineKeyboardButton(text='АФС: Осложнения при беременности', url='https://t.me/hematologist_Sokolova/94 ')],
    [InlineKeyboardButton(
        text='Применение ГКС при АФС во время беременности',
        url='https://t.me/hematologist_Sokolova/93 '
    )],
    [InlineKeyboardButton(text='Антинуклеарный фактор (АНФ)', url='https://t.me/hematologist_Sokolova/152 ')],
    [back_to_main_menu]
])

kb_analisys = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Анализ крови и беременность', url='https://t.me/hematologist_Sokolova/240 ')],
    [InlineKeyboardButton(text='HLA-типирование и невынашивание', url='https://t.me/hematologist_Sokolova/236 ')],
    [InlineKeyboardButton(text='Д-димер', url='https://t.me/hematologist_Sokolova/186 ')],
    [back_to_main_menu]
])

kb_child = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Авраменко Анастасия Викторовна', url='https://t.me/hematologist_Sokolova/222 ')],
    [InlineKeyboardButton(text='Какие клетки содержит общий анализ крови?',
                          url='https://t.me/hematologist_Sokolova/243 ')],
    [InlineKeyboardButton(text='Особенности в неонатальном скрининге', url='https://t.me/hematologist_Sokolova/230 ')],
    [back_to_main_menu]
])