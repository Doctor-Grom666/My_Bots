from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICu2gBdm0VN4ocQhIMOUekZDlsK0zeAAIP8TEbyfgRSMhnYJBketccAQADAgADeQADNgQ',
        caption=f'Привет, {message.from_user.first_name}!\nЭто бот канала '
                f'"Гематология без тайн"\n'
                f'Тут можно найти ответы на интересующие вас вопросы '
                f'и записаться на консультацию\n'
                f'Пожалуйста, выберите что Вас интересует в меню ниже 👇',
        reply_markup=kb.main)


@router.message(F.text == 'Консультация')
async def consult(message: Message):
    await message.answer(text='Запись на консультацию по номеру +78612020202 \n'
                              'Информация об онлайн консультации по кнопке ниже',
                         reply_markup=kb.online)


@router.message(F.text == 'Информация')
async def info(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAICu2gBdm0VN4ocQhIMOUekZDlsK0zeAAIP8TEbyfgRSMhnYJBketccAQADAgADeQADNgQ',
        caption='Выберите пункт меню:', reply_markup=kb.main_menu)


@router.callback_query(F.data == 'back')
async def info_back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAICu2gBdm0VN4ocQhIMOUekZDlsK0zeAAIP8TEbyfgRSMhnYJBketccAQADAgADeQADNgQ',
        caption='Выберите пункт меню:'
    ), reply_markup=kb.main_menu)


@router.callback_query(F.data == 'anemy')
async def anemy(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDGWgCJC8KilU-sZLIFTNSofxFsOTCAAI_8jEbzRwRSNinCJQeL-KfAQADAgADeAADNgQ',
        caption='Железодефицитная анемия и дефицит железа:'
    ), reply_markup=kb.kb_anemy)


@router.callback_query(F.data == 'ferritin')
async def ferritin(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDG2gCJGwKsClOnftAqNMKmifUUohMAAJD8jEbzRwRSLKQ5TrRyCxmAQADAgADeQADNgQ',
        caption='Повышенный уровень ферритина:'
    ), reply_markup=kb.kb_ferritin)


@router.callback_query(F.data == 'gens')
async def gens(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDH2gCJNtaEyANlLOMQ0YMFjAAASGEzgACRvIxG80cEUjMEtAC6w0vRwEAAwIAA3kAAzYE',
        caption='Гены системы крови:'
    ), reply_markup=kb.kb_gens)


@router.callback_query(F.data == 'anemys')
async def anemys(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDIWgCJR4JNfkXWwKAa1Nj9WfBzjb7AAJH8jEbzRwRSBc9_ZAhJLfjAQADAgADeAADNgQ',
        caption='Анемии:'
    ), reply_markup=kb.kb_anemys)


@router.callback_query(F.data == 'micro_elem')
async def micro_elem(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDI2gCJT_1-CeDrob1NYZhdO1xGQ-JAAJI8jEbzRwRSPJQV59X6CB1AQADAgADeQADNgQ',
        caption='Микроэлементы:'
    ), reply_markup=kb.kb_micro_elem)


@router.callback_query(F.data == 'leykocits')
async def leykocits(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDJWgCJX2VZpB7971kBZ6M8VDV301JAAJK8jEbzRwRSKi7eRAIfoxaAQADAgADeQADNgQ',
        caption='Лейкоциты:'
    ), reply_markup=kb.kb_leykocits)


@router.callback_query(F.data == 'trombofilia')
async def trombofilia(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDJ2gCJZnRa-ehOR0Ga0pmGig3n5WJAAJL8jEbzRwRSKTP93HZtj8tAQADAgADeQADNgQ',
        caption='Наследственная тромбофилия:'
    ), reply_markup=kb.kb_trombofilia)


@router.callback_query(F.data == 'afs')
async def afs(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDKWgCJdcMgZ7MziGZBtUhE1DtxqBFAAJM8jEbzRwRSKkbpem4jYgYAQADAgADeQADNgQ',
        caption='АФС:'
    ), reply_markup=kb.kb_afs)


@router.callback_query(F.data == 'analisys')
async def analisys(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDK2gCJgABt0gjW6Cc07-W4XSITCjY_gACUfIxG80cEUhvNH4lx2Kq0wEAAwIAA3kAAzYE',
        caption='Анализы крови и беременность:'
    ), reply_markup=kb.kb_analisys)


@router.callback_query(F.data == 'child')
async def child(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_media(InputMediaPhoto(
        media='AgACAgIAAxkBAAIDLWgCJio6a-kPbyzBO7jsrTS3eUSiAAJS8jEbzRwRSB6Sg-vtvnhsAQADAgADeQADNgQ',
        caption='Детская гематология:'
    ), reply_markup=kb.kb_child)