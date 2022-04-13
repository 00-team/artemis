HELP_PATTERN = '^help_(join|invite|login)$'

CONTNET_EN = {
    'start': (
        '🌀 Welcome to the Nightcurly Bot\n'
        'if you join our chats and invite 3 ppl into the bot\n'
        'we give you a free 15$ NFT'
    ),
    'help': (
        '-------- Help Title --------\n\n'

        'Explains how users can get a free NFT\n'
        '1. Join all channels\n'
        '2. Invite 3 ppl to the robot\n'
        '3. Log in to the website and give us your wallet\n'
        'After 24 hours, you will participate in the NFT lottery. '
        'We have 3 winners every night in the @XIXNFT channel.\n\n'

        'Join! - To join our chats\n'
        'Invite - To invite your friends\n'
        'Login - To login to the website\n'
        'Type help'
    ),
    'help_keyboard': [
        [{'text': 'Join!', 'callback_data': 'help_join'}],
        [{'text': 'Invite Others', 'callback_data': 'help_invite'}],
        [{'text': 'Login', 'callback_data': 'help_login'}],
    ],
    'help_edit': 'use /help or type help',

    'external_login': 'Login with this button 👇',
    'login_button': 'Login!',
    'login': (
        'Register for the last step on the site and send your wallet\n'
        'After 24 hours, you will participate in the NFT lottery. '
        'We have 3 winners every night in the @XIXNFT channel.'
    ),

    'chats_check_button': 'check ✅',
    'join_chats': 'Subscribe to the channel below 👇',
    'joined_chats': 'you already join all the channels',
    'join_complete': 'Congratulations\nSuccessfully joined the channels 🎉',
    'join_incomplete': (
        'You have not joined the channels yet\n'
        'Join all channels and click the check button'
    ),

    'invite_button': 'To get NFT enter the robot ✅',
    'invites': (
        'Ask three of your friends to join'
        'the bot with your special link. 🔗\n'
        'Your Link: {}\nYour total invites: {}/3'
    ),
    'invite_banner': (
        'The first valid bot that gives free nft as a gift 🎁\n\n'
        'From the Rarible site ⛵️\n\n'
        'Gain multi-dollar nfts in just three steps 💵💰'
    ),
    'enough_invites': (
        'Congratulations, you have successfully'
        'invited three people to the robot 🎉'
    ),
    'success_invite': 'You have succeeded adding someone into the bot 🎉',
}


CONTNET_RU = {
    'start': (
        '🌀Добро пожаловать в Nightcurly Bot\n'
        'если вы присоединитесь к нашим чатам и пригласите 3 человека в бота\n'
        'мы даем вам бесплатно 15 $ NFT'
    ),
    'help': (
        '-------- Название справки --------\n\n'

        'Объясняет, как пользователи могут получить бесплатный NFT\n'
        '1. Присоединяйтесь ко всем каналам\n'
        '2. Пригласить в робота 3 человека\n'
        '3. Войдите на сайт и дайте нам свой кошелек\n'
        'Через 24 часа вы будете участвовать в лотерее NFT. '
        'Каждую ночь на канале @XIXNFT у нас 3 победителя.\n\n'

        'Присоединиться! - Чтобы присоединиться к нашим чатам\n'
        'Пригласить - Пригласить друзей\n'
        'Логин - авторизация на сайте\n'
        'Введите help'
    ),
    'help_keyboard': [
        [{'text': 'Присоединяйтесь', 'callback_data': 'help_join'}],
        [{'text': 'Пригласить', 'callback_data': 'help_invite'}],
        [{'text': 'Логин', 'callback_data': 'help_login'}],
    ],
    'help_edit': 'используйте /help или введите help',

    'external_login': 'Login with this button 👇',
    'login_button': 'Логин!',
    'login': (
        'Зарегистрируйтесь на последний шаг на '
        'сайте и отправьте свой кошелек\n'
        'Через 24 часа вы будете участвовать в лотерее NFT. '
        'Каждую ночь на канале @XIXNFT у нас 3 победителя.'
    ),

    'chats_check_button': 'check ✅',
    'join_chats': 'Подпишитесь на канал ниже 👇',
    'joined_chats': 'you already join all the channels',
    'join_complete': 'Поздравления\nУспешно присоединился к каналу 🎉',
    'join_incomplete': (
        'Вы еще не присоединились к каналам\n'
        'Присоединяйтесь ко всем каналам и нажмите кнопку проверки'
    ),

    'invite_button': 'To get NFT enter the robot ✅',
    'invites': (
        'Попросите трех своих друзей присоединиться '
        'к роботу по вашей специальной ссылке. 🔗\n\n'
        'Ваша ссылка: {}\n\nВсего приглашений: {}/3'
    ),
    'invite_banner': (
        'Первый действующий бот, дающий бесплатный nft в подарок 🎁\n\n'
        'С сайта Рарибл\n\n'
        'Получите многодолларовую NFT всего за три шага 💵💰'
    ),
    'enough_invites': (
        'Поздравляем, вы успешно пригласили '
        'в робота трех человек 🎉'
    ),
    'success_invite': 'Вам удалось добавить кого-то в бота 🎉',
}

TRANSLATED_CONTENT = ['en', 'ru']
CONTNET = {'en': CONTNET_EN, 'ru': CONTNET_RU}

COMMANDS = (
    ('en', (
        ('help', 'Help!'),
        ('join', 'join to our channels'),
        ('invite', 'invite your friends into the bot!'),
        ('login', 'login to our website!'),
    )),
    ('ru', (
        ('help', 'помощь!'),
        ('join', 'присоединяйтесь к нашим каналам'),
        ('invite', 'пригласить друзей в бота!'),
        ('login', 'войти на наш сайт!'),
    )),
)
