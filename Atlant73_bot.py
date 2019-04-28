import telebot
from random import randint
from telebot.types import Message

token = '835391223:AAGjG_WBnaoAUuI3Mj0quG7RWkD-Kby54HM'
bot = telebot.TeleBot(token)
dict_id = dict()
users_set = set()
file = open('users.txt', 'r')
STICKER_ID = 'CAADAgADXwMAAgw7AAEKTh8jAAH9Q-gAAQI'

with open('id.txt', 'r') as f:
    for now in f.read().split('\n'):
        if now == '':
            continue
        new = now.split(':')
        dict_id[int(new[0])] = int(now[1])


with open('users.txt', 'r') as f:
    for now in f.read().split('\n'):
        if now == '':
            continue
        users_set.add(now + '\n')


@bot.message_handler(commands=['start', 'go', 'help', 'price',
                               'contacts', 'team', 'dnevnik_kachka_73', 'doc', 'gym', 'aerobic_room',
                               'individual_sessions', 'Developer'])
def get_commands_message(message: Message):
    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.text} \n')

    if message.text == '/help':
        bot.send_message(message.from_user.id, '/price - Цены на услуги Атлант \n \n'
                                               '/team - Наша команда \n \n'
                                               '/dnevnik_kachka_73 - Все о проекте Дневник Качка \n \n'
                                               '/doc - узнай кто состоит в этом боте \n \n'
                                               '/contacts - Контактная информация \n \n'
                                               '/Developer - Разработчик \n \n')
    elif message.text == '/price':
        bot.send_message(message.from_user.id, '/gym - Тренажерный зал \n \n'
                                               '/aerobic_room - Аэробный зал \n \n'
                                               '/individual_sessions - индивидуальные занятия \n \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/gym':
        bot.send_message(message.from_user.id, 'Утро с 7:00 до 15:00 - 170 рублей \n \n'
                                               'Вечер с 15:01 до 22:00 - 200 рублей \n \n'
                                               'Выходные - 170 рублей \n \n'
                                               'Абонемент "УТРО" - 1500 РУБЛЕЙ \n \n'
                                               'Абонемент "БЕЗЛИМИТНЫЙ" - 1800 РУБЛЕЙ \n \n'
                                               '/price - Вернуться назад \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/aerobic_room':
        bot.send_message(message.from_user.id, 'Групповые тренировки 1 занятие - 200 рублей \n \n'
                                               'Абонемент на групповые тренировки 12 занятий (на месяц) '
                                               '- 1800 рублей \n \n'
                                               '/price - Вернуться назад \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/individual_sessions':
        bot.send_message(message.from_user.id, 'Дети (до 18 лет), сплит-тренировки 1 + 1 - 650 рублей \n \n'
                                               'Взрослые (с 18 лет) - 800 рублей \n \n'
                                               'Абонемент на индивидуальные занятия - 7000 рублей (12 занятий) \n \n'
                                               '/price - Вернуться назад \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/contacts':
        bot.send_message(message.from_user.id, 'Адрес: ул. Кирова, 26, Батайск, Ростовская обл., Россия, 346880 \n \n'
                                               'Телефон: +7 928 165-39-39 \n \n'
                                               'Instagram: \n \n'
                                               '@atlant__fitness \n \n'
                                               '@dnevnik_kachka_73 \n \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/Developer':
        bot.send_message(message.from_user.id, 'Этот бот создан исключительно на энтузиазме и с целью улучшения сервиса ' 
                                               'Атланта. Если у Вас есть предложения для улучшения бота или вы просто '
                                               'хотите написать комент то просто напишите боту и он автоматически '
                                               'перешлет анонимно Разработчику текс, который был написал. А так же вы '
                                               'можете написать в соц. Сети указаные ниже. Жду Ваших предложений и '
                                               'критики. Если хочешь собственного бота то напиши Разработчику и он '
                                               'воплатить твою мечту в реальность. Живите долго и Качайтесь! \n \n'
                                               'Telegram - @Kosten_73 \n \n'
                                               'Instagram - @rudenko_73 \n \n'
                                               'Вконтакте - @kosten_73 \n \n'
                                               'номер телефона - +7(903)472-99-36 \n \n'
                                               'пожертвования - 5469520013632617 \n \n \n'
                                               '/help - Возврат в основное меню \n \n')
    elif message.text == '/team':
        bot.send_message(message.from_user.id, 'Разработчик ещё не владеет этой информацией \n \n'
                                               '/help - Возврат в основное меню')
    elif message.text == '/dnevnik_kachka_73':
        bot.send_message(message.from_user.id, 'Дневник Качка (ДК) - это Государственная организация, имеющаая '
                                               'разделенный на доли участников уставный капитал и самостоятельно '
                                               'отвечающая по своим обязательятвам.\n \n '
                                               'Как и у РФ есть конституция, так и у ДК есть свой священный документ, '
                                               'который имеет юридическую силу в качковской суде. "Кодекс Качка" - '
                                               'это Кодекс которым должен руководствоваться каждый уважающий себя Качок'
                                               '. В скором времени выйдет книга "Кодекс качка". Если хотите вступить '
                                               'в данную организацию, то подайте заявку Генеральному директору - '
                                               '@Kosten_73 \n \n'
                                               '/help - Возврат в основное меню \n \n ')
    elif message.text == '/doc':
        if message.from_user.id == 321354512:
            bot.send_message(321354512, file.read())
            bot.send_message(321354512, '/help - Возврат в основное меню')
        else:
            bot.send_message(message.from_user.id, 'У вас нет прав получать данные об составе этого бота, '
                                                   'только участники Проекта /dnevnik_kachka_73 имеют доступ к этой '
                                                   'информации \n \n'
                                                   '/help - Возврат в основное меню')
    elif message.text == '/start' or '/go':
        if message.from_user.last_name == None:
            message.from_user.last_name = ''
        if message.from_user.id not in dict_id:
            dict_id[int(message.from_user.id)] = len(dict_id) + 1
            with open('id.txt', 'a') as f:
                f.write(str(message.from_user.id))
                f.write(': ')
                f.write(str(len(dict_id)))
                f.write('\n')

        my_set = {f'{message.from_user.id} @{message.from_user.username} {message.from_user.first_name} '
                  f'{message.from_user.last_name} \n'}
        my_set1 = f'{message.from_user.id} @{message.from_user.username} {message.from_user.first_name} ' \
            f'{message.from_user.last_name} \n'

        if False == (my_set <= users_set):
            users_set.add(f'{message.from_user.id} @{message.from_user.username} {message.from_user.first_name} '
                          f'{message.from_user.last_name} \n')
            with open('users.txt', 'a') as f:
                f.write(my_set1)
        bot.send_message(message.from_user.id, f'Приветствую {message.from_user.last_name} '
        f'{message.from_user.first_name} Качок Атланта! \n'
        'Я бот созданный Гл. Качком Атланта! \n'
        f'Вы вступили под № {dict_id[message.from_user.id]} \n'
        f'Всего нас {len(dict_id)} \n \n'
        'Для начала работы нажмите - /help')


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def get_text_messeges(message: Message):
    bot.reply_to(message, 'можете написать все что захотите и Гл.Качок узнает об этом'
                          ' (ваши молитвы будут услышаны)')
    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.text} \n'), message.text


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    bot.send_message(message.from_user.id, 'Думал я не умею отправлять стикеры АХАХАХАХ '
                                           'я могу так хоть до конца своей батарейки этим заниматься)')
    if message.from_user.id != 321354512:
        bot.send_message(321354512, f'{message.from_user.id} @{message.from_user.username} '
        f'{message.from_user.first_name} {message.from_user.last_name} {message.sticker.file_id} \n')


bot.polling()
