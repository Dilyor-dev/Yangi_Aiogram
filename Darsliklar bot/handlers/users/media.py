from loader import dp
from aiogram.types import ContentTypes,Message
from pathlib import Path

manzil = Path().joinpath('Mediafiles')
manzil.mkdir(parents=True,exist_ok=True)

@dp.message_handler(content_types=ContentTypes.VIDEO)
async def send_video(v:Message):
    await v.video.download(destination=manzil)
    await v.reply('Video yuklab olindi')

@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def dowload_doc(d:Message):
    await d.document.download(destination=manzil)
    file_idd = d.document.file_id
    await d.answer(file_idd)

@dp.message_handler(commands='document')
async def send_doc(doc:Message):
    id = 'BQACAgIAAxkBAAIBeGFcKJfJYdyE0acLqeiBEH_wFiY-AAJpEAACYrnhShKg_fAVFP_LIQQ'
    await doc.reply_document(id,caption='Bu document id orqali yuklandi!')

@dp.message_handler(content_types=ContentTypes.STICKER)
async def send_sticker(s:Message):
    await s.sticker.download(destination=manzil)
    await s.reply('Stickr yuklab olindi')