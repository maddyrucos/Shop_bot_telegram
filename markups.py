from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import config

to_menu = InlineKeyboardButton('🏠 Главное меню', callback_data='main_menu')
to_menu_only = InlineKeyboardMarkup(row_width=1).add(to_menu)


# -- Главное меню --

catalog_btn = InlineKeyboardButton('🛍 Каталог', callback_data='catalog')
balance_btn = InlineKeyboardButton('💳 Баланс', callback_data='balance')
comment_btn = InlineKeyboardButton('🗣 Отзывы', callback_data='comment')
main_menu = InlineKeyboardMarkup(row_width=1).add(catalog_btn, balance_btn, comment_btn)


# -- Баланс --

balance_deposit = InlineKeyboardButton('🪙 Пополнить', callback_data='deposit')
balance_menu = InlineKeyboardMarkup(row_width=1).add(balance_deposit, to_menu)

# -- Отзывы --

check_comments = InlineKeyboardButton('👀 Посмотреть отзывы', callback_data = 'check_comments')
add_comment = InlineKeyboardButton('✍️ Оставить отзыв', callback_data='add_comment')
comment_menu = InlineKeyboardMarkup(row_width=1).add(add_comment, check_comments, to_menu)

web_store = InlineKeyboardButton(f'Отзывы на {config.SITE}', url=config.LINK)
check_comments_menu = InlineKeyboardMarkup(row_width=1).add(web_store, to_menu)

# -- Админ меню --

admin_add_to_db = InlineKeyboardButton('Добавить товар', callback_data='add_good')
admin_send = InlineKeyboardButton('Рассылка', callback_data='send_button')
admin_download = InlineKeyboardButton('Скачать БД', callback_data='download')
admin_menu = InlineKeyboardMarkup(row_width=1).add(admin_add_to_db, admin_send, admin_download)

admin_apply_add_good = InlineKeyboardButton('Принять', callback_data='apply_add_good')
admin_decline_add_good = InlineKeyboardButton('Отмена', callback_data='admin')
admin_add_good_menu = InlineKeyboardMarkup(row_width=2).insert(admin_apply_add_good)
admin_add_good_menu.insert(admin_decline_add_good)
