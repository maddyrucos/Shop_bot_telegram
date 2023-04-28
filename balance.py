from database import cur
import markups as mks


#Отображение баланса
async def balance(callback_query):

    cur.execute(f'SELECT balance FROM users WHERE "user_id" == "{callback_query.from_user.id}"') #Из таблицы с пользователем фиксируется баланс пользователя с id
    bal = cur.fetchone()
    bal_text = f'Ваш баланс: {bal[0]}₽'
    await callback_query.message.answer(text = bal_text, reply_markup=mks.balance_menu)
