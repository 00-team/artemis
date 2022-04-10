HELP_PATTERN = '^help_(join|invite|login)$'

CONTNET_EN = {
    'start': (
        '🌀 Welcome to the Nightcurly Bot\n'
        'if you join our chats and invite 3 ppl into the bot\n'
        'we give you a free 10$ NFT\n'
        '...'
    ),
    'help': (
        '-------- Help Title --------\n\n'
        'describing how users can get a free NFT\n'
        '1.join all the channels\n'
        '2.invite 3 ppl into the bot\n'
        '3.login to the website and give us your wallet\n'
        'after 24H admin will gift you a free NFT\n\n'
        'Join! - for joining into our chats\n'
        'Invite - for inviting your frinds\n'
        'Login - for loging into the website\n'
        'type help'
    ),
    'help_keyboard': [
        [{'text': 'Join!', 'callback_data': 'help_join'}],
        [{'text': 'Invite Others', 'callback_data': 'help_invite'}],
        [{'text': 'Login', 'callback_data': 'help_login'}],
    ],

    'external_login': 'Login with this button 👇',
    'login_button': 'Login!',
    'login': (
        'Register for the last step on the site and send your wallet\n'
        'Nft will be sent to your account within 24 hours.'
    ),

    'chats_check_button': 'check ✅',
    'join_chats': 'Subscribe to the channel below 👇',
    'joined_chats': 'you already join all the channels',
    'join_complete': 'Congratulations\nSuccessfully joined the channels 🎉',

    'invite_button': 'To get NFT enter the robot ✅',
    'invites': (
        'Ask three of your friends to join'
        'the bot with your special link. 🔗\n'
        'Your Link: {}\nYour total invites: {}/3'
    ),
    'invite_banner': (
        'The first valid bot that gives free nft as a gift 🎁\n\n'
        'From the opensea site ⛵️\n\n'
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
        '🌀 Добро пожаловать в бота Nightcurly\n'
        'if you join our chats and invite 3 ppl into the bot\n'
        'we give you a free 10$ NFT\n'
        '...'
    ),
    'help': (
        '-------- Help Title --------\n\n'
        'describing how users can get a free NFT\n'
        '1.join all the channels\n'
        '2.invite 3 ppl into the bot\n'
        '3.login to the website and give us your wallet\n'
        'after 24H admin will gift you a free NFT\n\n'
        'Join! - for joining into our chats\n'
        'Invite - for inviting your frinds\n'
        'Login - for loging into the website\n'
        'type help'
    ),
    'help_keyboard': [
        [{'text': 'Join!', 'callback_data': 'help_join'}],
        [{'text': 'Invite Others', 'callback_data': 'help_invite'}],
        [{'text': 'Login', 'callback_data': 'help_login'}],
    ],

    'external_login': 'Login with this button 👇',
    'login_button': 'Login!',
    'login': (
        'Зарегистрируйтесь на последний шаг на '
        'сайте и отправьте свой кошелек\n'
        'Nft будет отправлен на ваш счет в течение 24 часов.'
    ),

    'chats_check_button': 'check ✅',
    'join_chats': 'Подпишитесь на канал ниже 👇',
    'joined_chats': 'you already join all the channels',
    'join_complete': 'Поздравления\nУспешно присоединился к каналу 🎉',

    'invite_button': 'To get NFT enter the robot ✅',
    'invites': (
        'Попросите трех своих друзей присоединиться '
        'к роботу по вашей специальной ссылке. 🔗\n'
        'Your Link: {}\nYour total invites: {}/3'
    ),
    'invite_banner': (
        'Первый робот, раздающий nft бесплатно 🎁'
        'С сайта: opensea ⛵️\n\n'
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
