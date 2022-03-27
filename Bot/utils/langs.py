langs = {
    'welcome': {
        'en': '🌀 Welcome to the Artemis Bot',
        'ru': '🌀 Добро пожаловать в бота Artemis',
    },
    'join_chats': {
        'en': 'Subscribe to the channel below 👇',
        'ru': 'Подпишитесь на канал ниже 👇'
    },
    'join_complete': {
        'en': 'Congratulations\nSuccessfully joined the channels 🎉',
        'ru': 'Поздравления\nУспешно присоединился к каналу 🎉',
    },
    'invites': {
        'en': 'Ask three of your friends to join the bot with your special link. 🔗',
        'ru':
        'Попросите трех своих друзей присоединиться к роботу по вашей специальной ссылке. 🔗'
    },
    'invite_banner': {
        'en':
        'The first valid bot that gives free nft as a gift 🎁\n\nFrom the opensea site ⛵️\n\nGain multi-dollar nfts in just three steps 💵💰',
        'ru':
        'Первый робот, раздающий nft бесплатно 🎁\n\nС сайта: opensea ⛵️\n\nПолучите многодолларовую NFT всего за три шага 💵💰'
    },
    'success_invite': {
        'en': 'You have succeeded adding someone into the bot 🎉',
        'ru': 'Вам удалось добавить кого-то в бота 🎉'
    },
    'enough_invites': {
        'en':
        'Congratulations, you have successfully invited three people to the robot 🎉',
        'ru': 'Поздравляем, вы успешно пригласили в робота трех человек 🎉',
    },
    'login': {
        'en': 'Register for the last step on the site and send your wallet\nNft will be sent to your account within 24 hours.',
        'ru':
        'Зарегистрируйтесь на последний шаг на сайте и отправьте свой кошелек\nNft будет отправлен на ваш счет в течение 24 часов.'
    },
    'external_login': {
        'en': 'cool',
        'ru': ' с помощью этВойтиой кнопки 👇'
    }
}

HELP_PATTERN = '^help_(join|help|login|start|invite)$'

CONTNET_EN = {
    'start': (
        'welcome to bot XXX\n'
        'if you join our chats and invite 3 ppl into the bot\n'
        'we give you a free 10$ NFT\n'
        '...'
    ),
    'help': (
        '-------- Help Title --------\n\n'
        'Start! - welcome message and info\n'
        'Join! - for joining into our chats\n'
        'Invite - for inviting your frinds\n'
        'Login - for loging into the website\n'
        'Help 🆘 - for showing this message\n'
    ),
    'help_keyboard': [
        [
            {
                'text': 'Start!',
                'callback_data': 'help_start'
            },
            {
                'text': 'Join!',
                'callback_data': 'help_join'
            },
        ],
        [
            {
                'text': 'Login',
                'callback_data': 'help_login'
            },
            {
                'text': 'Invite Others',
                'callback_data': 'help_invite'
            },
        ],
        [
            {
                'text': 'Help 🆘',
                'callback_data': 'help_help'
            },
        ],
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
        'the bot with your special link\. 🔗\n'
        '[Your Link]({})\nYour total invites: {}/3'
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

TRANSLATED_CONTENT = ['en', 'ru']
CONTNET = {'en': CONTNET_EN, 'ru': CONTNET_EN}
