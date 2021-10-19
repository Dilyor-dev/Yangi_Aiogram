from aiogram import Dispatcher

from loader import dp
from . admins import Admin
from . shaxsiy import Shaxsiy
from . group import Group
if __name__ == "filters":
    dp.filters_factory.bind(Admin)
    dp.filters_factory.bind(Shaxsiy)
    dp.filters_factory.bind(Group)