import telebot
from telebot import types  # для указание типов
from time import sleep


bot = telebot.TeleBot("МЕСТО ДЛЯ ВАШЕГО ТОКИНА")


def generate_keyboard(*buttons) -> types.ReplyKeyboardMarkup:
    """Перебираем кортеж с текстами для кнопок и генерируем кнопки"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for txt_button in buttons:
        btn = types.KeyboardButton(txt_button)
        markup.add(btn)
    return markup


@bot.message_handler(commands=['start'])  # создаем команду
def start(message):
    img1 = open('images/1.jpg', 'rb')
    bot.send_chat_action(message.chat.id, 'typing', timeout=3)
    bot.send_photo(message.chat.id, photo=img1, caption="Привет, {0.first_name} великая наездница!\n"
                                                        "Меня зовут Ксейдан Риорсон, нам необходимо спасти Наварру,"
                                                        "но вдвоем мы не справимся, поэтому я решил прибегнуть к помощи моих друзей из Хогвартса. ".format(
                         message.from_user))

    bot.send_chat_action(message.chat.id, 'typing', timeout=3)
    sleep(4)
    img2 = open('images/2.jpg', 'rb')
    bot.send_photo(message.chat.id,photo=img2,
                     caption='Для борьбы нам необходимо достать магический кристалл из лабиринта Хогвартса.\n'
                             'Но путь к кристаллу непрост и таит в себе массу испытаний и тайн.\nГарри сказал, '
                             'что только ты сможешь с этим справиться, пройти все испытания Кубка огня и добыть его.')

    bot.send_chat_action(message.chat.id, 'typing', timeout=3)
    sleep(4)
    img3 = open('images/3.jpg', 'rb')
    bot.send_photo(message.chat.id,photo=img3,
                     caption='Не переживай, ты будешь не одна и на твоем нелегком пути тебе поможет верная Андарна.\n'
                             'Готова к этому путешествию?',
                     reply_markup=generate_keyboard("Полетели!"))


@bot.message_handler(content_types=['voice'])
def func(message: types.Message):
    """Получение айди ГС"""
    print(message.voice.file_id)



@bot.message_handler(content_types=['text'])
def func(message: types.Message):
    """Обработчик нажатий на кнопки"""
    if message.text == 'Полетели!':
        img4 = open('images/4.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img4,
                         caption='Злобные Вейнители объединились с Волан-де-Мортом и тщательно охраняют лабиринт от '
                              'чужаков.\nЭто испытание будет не простым.\nДля того, чтобы добраться вглубь лабиринта к '
                              'заветному кристаллу тебе нужно будет уничтожить 4 крестража.\nВраги хитры, поэтому '
                              'поместили в них души твоих близких друзей.\nУничтожив все крестражи ты не только сможешь '
                              'победить злодеев, но и освободить своих подруг из заточения.\nТы точно готова к первому испытанию?',
                         reply_markup=generate_keyboard("Антенны вверх!"))

    elif message.text == 'Антенны вверх!':
        img5 = open('images/5.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(3)
        bot.send_photo(message.chat.id,photo=img5,
                         caption='Ты с осторожностью заходишь в лабиринт проходишь два пролета и натыкаешься на странный портал,\n'
                                 'который утягивает тебя в неизвестность.',reply_markup=types.ReplyKeyboardRemove())

        img6 = open('images/6.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(4)
        bot.send_photo(message.chat.id,photo=img6,
                         caption='Меньше, чем за долю секунды ты переместилась из жуткого лабиринта на тихую заснеженную улочку рождественского Хогсмида.\n'
                                 'В конце улицы заметила сияние, приглядевшись ты осознала, что это тот самый первый крестраж твоих врагов.\n'
                                 'Ты подошла поближе, чтобы лучше его разглядеть и была удивлена, увидев мятного карася.')

        img7 = open('images/7.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(4)
        bot.send_photo(message.chat.id,photo=img7,
                         caption='Подойдя поближе ты заметила рядом небольшой грязный дневник.\n'
                                 'Раскрыв его ты увидела лишь '
                              'пустые страницы, спустя мгновение на нем начали появляться кровавые буквы и '
                              'принялась читать проявившийся текст...\n' 
                              'Хочешь уничтожить наши крестражи, всадница?\n'
                              'Не так быстро.\n'
                              'Посмотрим, как хорошо ты'
                              'знаешь подруг, которые заточены в мои предметы.\n'
                                 'Я дам небольшие подсказки и тебе '
                              'нужно будет догадаться о ком из твоих подруг идет речь.\n'
                                 'Приступим…\n'
                                 '\n'
                              'Перелистнув страницу перед тобой предстал текст:',
                         reply_markup=generate_keyboard("Открыть текст!"))

    elif message.text == 'Открыть текст!':
        bot.send_message(message.chat.id,
                         text='Я тот человек:\n'
'- С которым ты гуляла ночью под снегопадом и горланила песни Сплин и Би-2 на всю улицу ☃️\n'
'- Который помогал тебе искать шапку в кальянной 👒\n'
'- С которым ты бегала ночью по крематорию и била палкой в гонг пугая охранников 🎯\n'+
'- Который был с тобой и в горе и в радости, и в Сибири и на Кавказе 🏞\n'
'- Который с тобой пел песенки со стриптезершами и текильщицами 🎊\n'
'- Который сумел выбесить тебя одной небольшой коробкой с нитками 🧶\n'
'- Который всегда тебя встречает на вокзале с бутылкой боржоми 🍼\n'
'- Который переезжал с тобой всю ночь со всеми вещами благодаря Семёновне 👵🏻\n'+
'- Который помогал тебе избавиться от улья на балконе 🐝\n'
'- Который всегда поддерживает любые твои идеи и согласен на любые приключения 🎢\n',
                         reply_markup=generate_keyboard("Полина", "Алёна", "Таня", "Кристина"))

    elif message.text == 'Таня':
        img9 = open('images/9.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img9,
                         caption='Поздравляю, ты справилась с первым испытанием!',
                         reply_markup=generate_keyboard('Продолжаем путешествие-->'))
        video_tanya = open('images/tanya.mp4','rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_video(message.chat.id, video=video_tanya)


        # bot.send_voice(message.chat.id, voice="") + айди объекта, и мы сможем дать войс!

    elif message.text in ("Полина", "Алёна", "Кристина"):
        img1_1 = open('images/1.1.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img1_1,
                         caption='Ты шо, уху ела? Подумай еще :(!',
                         reply_markup=generate_keyboard("Полина", "Алёна", "Таня", "Кристина"))

    elif message.text == 'Продолжаем путешествие-->':
        img10 = open('images/10.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img10,
                         caption='Как только ты справилась с этой загадкой, портал вновь появился и унес тебя в неизвестном направлении.\n'
                                 'Тебя ослепила яркая вспышка, придя в себя ты поняла, что оказалась в библиотеке квадранта песцов.\n'
                                 'Оглядевшись по сторонам ты продвинулась вглубь библиотеки и неожиданно между стеллажей наткнулась на Пухлю.\n'
                                 'Она совсем не двигалась, ты попыталась дотронуться до нее, но это действие ни к чему не привело.\n'
                                 'Осознав безвыходность положения ты начала осматривать соседние ящики и в одном из них заметила маленький сверток пергамента.',
                         reply_markup=generate_keyboard('Сверток...'))

    elif message.text == 'Сверток...':
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_message(message.chat.id,
                         text='Развернув его перед твоими глазами открылась вторая подсказка.\n'
'Я тот человек:\n'
'- С которым ты в пижаме лежала на асфальте под летним дождем 🌦\n'
'- Которого ты лечила пивом от головой боли 🍻\n'
'- С которым ты была в самые радостные моменты, и в самые грустные 🎭\n'
'- С которым ты 4 раза ездила в травму 🏥\n'
'- Которому ты сорвала пион на газоне у оперного театра рядом с ментами 🌺\n'
'- С которым ты смотрела «Гадалку» и «Тайны человечества», кушая малосольные огурцы твоей бабушки прямо с банки 🥒\n'
'- С которым ты купалась и загорала в море на 9 мая, а на нас смотрели, как на дур 🤪\n'
'- Которому ты хотела показать короткую дорогу, а это оказался тупик и я чуть не обкакалась 😹\n'
'О ком идет речь?\n',reply_markup=generate_keyboard('Алена?','Кристина?','Таня?','Полина?'))
    elif message.text == 'Кристина?':
        img12 = open('images/12.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img12,
                         caption='Поздравляю, ты успешно прошла второе испытание!',
                         reply_markup=types.ReplyKeyboardRemove())
        video_kris = open('images/kristina.mp4', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(2)
        bot.send_video(message.chat.id, video=video_kris)
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(56)
        img13 = open('images/13.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=img13,
                       caption='В эту секунду Пухля ожил и радостно завиляв хвостом побежал в твою сторону.\n'
                               'Вас разделяло пара метров, но тут между вами вновь появился портал и засосал тебя в неизвестность.'
                               'Приземлившись ты оказалась в темном помещении, первое, что тебе бросилось в глаза огромная неоновая вывеска ”POSH”.\n'
                               'Вокруг громко играла музыка и ты услышала знакомый мотив "Soy Yo".\n'
                               'Спустившись вниз по лестнице пару пролетов ты наткнулась на холодильник.\n'
                               'Ты подошла ближе и дернула за ручку, дверь открылась со скрипом.\n'
                               'А внутри находился очередной крестраж.\n'
                               'Им была недавно помытая банка йогурта с запиской.\n'
                               'Ты развернула записку и принялась читать текст...',
                       reply_markup=generate_keyboard('Читать...'))
        vol1 = open(r'images/aud1.mp3','rb')
        bot.send_voice(message.chat.id, voice=vol1)
        # bot.send_voice(message.chat.id, voice="AwACAgIAAxkBAAIHumdHIZUdZNGI_tnH4f1ySqc4d4oSAALGXwACnLA4SviVLpRYwKEpNgQ")


    elif message.text in ('Алена?','Таня?','Полина?'):
        img1_2 = open('images/1.2.jpeg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img1_2,
                         caption='Эх мать, еще раз промахнешься - скину девчОнкам твои ответы) пусть посмотрят, как ты их хорошо знаешь!',
                         reply_markup=generate_keyboard('Алена?','Кристина?','Таня?','Полина?'))

    elif message.text == 'Читать...':
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_message(message.chat.id,
                         text='Я та, с кем ты:\n'+
'🍸 Пила текилу по 10 шотов за ночь, а иногда и в обед на бизнес ланче в Честном ресторане\n'
'🥒 Ела соленные огурчики с лепешкой за последней партой в универе\n'
'🦸‍♂️ Читала рэп с пьяным татарчуком в маске железного человека\n'
'\n'
'Но потом все изменилось и я стала той , с кем ты :\n'
'🧩 Собирала пазлы по вечерам под все части мумии\n'
'🍤 Ела шримп ролл под фильм о масонах\n'
'🐝 Ловила здоровенную осу в декабре\n'
'👩🏼‍💻 Работала за ноутом до глубокой ночи сидя на кухне\n'
'🕯️ Жгла свечи и вязала красные нити\n'
'🧖‍♀️ Ходила в общественные бани\n'
'🐟 Ужинала  селедочкой с картошечкой и джеликой под коньячок (и один раз под дедову самогонку)\n'
'🧑‍🎨 Лепила фигурки из пластилина\n'+'Кто же это?!\n',reply_markup=generate_keyboard('Может это Алена?','Или Кристина?!','Да не, это Танька!','Или вовсе ты сама!?'))

    elif message.text == 'Может это Алена?':
        img15 = open('images/15.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img15,
                         caption='Поздравляю, ты справилась с третьим испытанием!',reply_markup=types.ReplyKeyboardRemove())
        video_alyona = open('images/alyona.mp4', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(2)
        bot.send_video(message.chat.id, video=video_alyona)
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(61)
        img16 = open('images/16.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=img16,
                       caption='В моменте холодильник резко захлопнулся и на его месте вновь появился уже знакомый портал, унося тебя в пустоту.\n'
                               'Спустя пару мгновений твоему взору открылась очередная локация.\n'
                               'Слепило яркое солнце, ветер обдувал твои щеки, осмотревшись вокруг, ты поняла, что это место тебе также очень знакомо...\n'
                               'Ведь ты оказалась вплотную перед стенами крепости Альдибаин.\n'
                               'Подняв голову наверх ты увидела в небе маленькую точку.\n'
                               'Приглядевшись ты узнала в этой точке Андарну, которая поспешила тебе на помощь.\n'
                               'Ты поняла, чтобы найти последний крестраж нужно двигаться вслед за ней.\n'
                               'И ты поспешила вдоль стен крепости.\n'
                               'Внезапно дракон начал терять высоту и спустя какое-то время приземлился у большого камня.\n'
                               'Ты начала ускоряться в его сторону, подбежав ты увидела на камне последний крестраж, им была "Блиц, скорость без границ",'
                               'снизу на камне было высечено большими буквами:',
                       reply_markup=generate_keyboard('Рассмотреть поближе'))




    elif message.text in ('Или Кристина?!','Да не, это Танька!','Или вовсе ты сама!?'):
        img1_3 = open('images/1.3.jpeg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img1_3,
                         caption='Это уже не смешно...КРУЦИО!',
                         reply_markup=generate_keyboard('Может это Алена?','Или Кристина?!','Да не, это Танька!','Или вовсе ты сама!?'))


    elif message.text == 'Рассмотреть поближе':
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_message(message.chat.id, text='Я тот человек:\n'
'🏠 Которому ты сдавала свою съемную квартиру\n'
'🌉 Который прыгал с тобой с моста в озеро\n'
'👋🏻 Который здоровается с твоей мамой "привет"\n'
'⛩️ Который был с тобой в тусовке любителей покататься по ночам на мой др в крематорий\n'
'🚗 Который иногда в морозы возил тебя до универа\n'
'🚔 У которого однажды эвакуировали машину возле твоего дома и мы думали, где же теперь ее искать 😆\n'
'🏊🏻‍♀️ С которым ты в последнюю встречу ездила отдыхать в термы\n'
'Ты уже догадалась, кто я?\n',reply_markup=generate_keyboard('100% - это Таня','90%- это Крис', '70%-Алена','20%-Полина'))


    elif message.text == '20%-Полина':
        img18 = open('images/18.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id,photo=img18,
                         caption='Поздравляю, ты успешно прошла все испытания, уничтожив все 4 крестража и освободив своих подруг!',reply_markup=generate_keyboard('<<Финал истории>>'))
        video_borsh = open('images/borsh.mp4', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(2)
        bot.send_video(message.chat.id, video=video_borsh)




    elif message.text in ('100% - это Таня','90%- это Крис', '70%-Алена'):
        img1_4 = open('images/1.4.png', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id, photo=img1_4,
                       caption='БОООБЕР - КУУУУРВАА!',
                       reply_markup=generate_keyboard('100% - это Таня','90%- это Крис', '70%-Алена','20%-Полина'))

    elif message.text == '<<Финал истории>>':
        img19 = open('images/19.jpg', 'rb')
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        bot.send_photo(message.chat.id, photo=img19,
                       caption='Я знал, что ты - самый правильный выбор в моей жизни, София!\n'
                               'Я накажу тебя так же, как тогда в душевой, когда ты нарушила все правила и полетела ко мне, помнишь? 😏\n'
                                'Ты не только спасла Наварру и своих подруг, но и сделала это в лучший день - в твой день рождения 🤍\n'
                                'Таких светлых, добрых, честных людей очень мало.\n'
                                'Оставайся такой, совершенствуйся, люби и будь любима!\n'
                                'Пусть каждый твой день будет наполнен счастьем, улыбками и хорошим настроением!\n'
                                'Все трудности, которые попадаются на твоем жизненном пути ты пройдёшь так же легко, как уничтожила крестражи!\n'
                                'Это сделает тебя сильнее и увереннее.',
                       reply_markup=types.ReplyKeyboardRemove())
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(6)
        img20 = open('images/20.jpg', 'rb')
        bot.send_photo(message.chat.id, photo=img20,
                       caption='Мы желаем тебе всего того, что желаешь ты себе сама, ведь лучше тебя самой тебя не знает никто.\n'
                               'За одним исключением - мы умножаем это в 100000000000000000 раз.\n'
'Мы очень тебя любим!\n'
                               'Пускай не все мы можем быть с тобой в этот день, обнять тебя и сказать это лично, но всю свою любовь мы посылаем сквозь километры.\n'
'С днем рождения, наша Соня! ❤️',reply_markup=generate_keyboard('От создателя :D'))
        vol2 = open(r'images/aud2.mp3', 'rb')
        bot.send_voice(message.chat.id, voice=vol2)
        # bot.send_voice(message.chat.id, voice="AwACAgIAAxkBAAIH1mdHJXAQp6sHYFkzoLbPDKDzJTAdAAIKYAACnLA4Spr7H3jnwykJNgQ") ЭТО НЕ НУЖНО

    elif message.text == 'От создателя :D':
        bot.send_chat_action(message.chat.id, 'typing', timeout=3)
        sleep(3)
        video_file = open('images/vid1.mp4', 'rb')
        bot.send_video(message.chat.id, video=video_file,caption='С праздником ❤️, жду в гости, с нетерпением🥳',reply_markup=types.ReplyKeyboardRemove())