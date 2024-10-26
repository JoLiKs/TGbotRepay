import time

from aiogram.filters import BaseFilter
from aiogram.types import Message


class LangFilter(BaseFilter):

    def __init__(self, s, s2=None):
        self.s = s
        self.s2 = s2

    async def __call__(self, message: Message):
        if not self.s2 is None:
            if message.text == lang[self.s][message.from_user.language_code] or message.text == \
                    lang[self.s2][message.from_user.language_code]:
                return True
        if message.text == lang[self.s][message.from_user.language_code]:
            return True
        else:
            return False


class myDict(dict):
    default_lang = {
        'bye': 'Спасибо за заявку! С вами свяжется наш специалист.\nКонтакт для связи: @personaldriver_by',
        'not_tag': 'У вас нет тега! Укажите в настройках телеграма тег.\n\nИнструкция:\n- Нажмите на кнопку "Настройки" в боковом меню.\n- Выберите опцию "имя пользователя"\n- Заполните поле ввода и нажмите галочку для сохранения.',
    }

    def __getitem__(self, item):
        try:
            return self.d[item]
        except:
            return self.default_lang

    def __init__(self, d):
        super().__init__()
        self.d = d


lang = myDict({
    "geo_received": {
        "ru": "Ваша геолокация получена",
        "en": "Your location has been received",
        "fr": "Votre localisation a été reçue",
        "de": "Ihr Standort wurde empfangen",
        "tr": "Konumunuz alındı",
        "zh": "您的位置已收到",
        "it": "La tua posizione è stata ricevuta"
    },
    "rules": {
        "ru":"Для участия вам необходимо будет заполнить данные и подписаться на канал" }
    ,
"surname": {
        "ru": "Фамилия",
        "en": "Surname",
        "fr": "Nom de famille",
        "de": "Nachname",
        "tr": "Soyadı",
        "zh": "姓",
        "it": "Cognome"
    },
    "name": {
        "ru": "Имя",
        "en": "Name",
        "fr": "Prénom",
        "de": "Vorname",
        "tr": "Adı",
        "zh": "名字",
        "it": "Nome"
    },
    "company": {
        "ru": "Компания",
        "en": "Company",
        "fr": "Entreprise",
        "de": "Firma",
        "tr": "Şirket",
        "zh": "公司",
        "it": "Azienda"
    },
    "position": {
        "ru": "Должность",
        "en": "Position",
        "fr": "Poste",
        "de": "Position",
        "tr": "Pozisyon",
        "zh": "职位",
        "it": "Posizione"
    },
    "telegram_contact": {
        "ru": "Контакт в телеграме",
        "en": "Telegram Contact",
        "fr": "Contact Telegram",
        "de": "Telegram-Kontakt",
        "tr": "Telegram İletişim",
        "zh": "电报联系",
        "it": "Contatto Telegram"
    },
    "email": {
        "ru": "Почта",
        "en": "Email",
        "fr": "Courriel",
        "de": "E-Mail",
        "tr": "E-posta",
        "zh": "电子邮件",
        "it": "Email"
    },
    "in_main_menu": {
        "ru": "В главное меню",
        "en": "To main menu",
        "fr": "Au menu principal",
        "de": "Zum Hauptmenü",
        "tr": "Ana menüye",
        "zh": "主菜单",
        "it": "Al menu principale"
    },
    "not_allowed": {
        "ru": "Вы не зарегистрированы как водитель"
    },
    "join": {
        "ru": "Участвовать",
        "en": "Join",
        "fr": "Participer",
        "de": "Teilnehmen",
        "tr": "Katıl",
        "zh": "参加",
        "it": "Partecipare"
    },


    "not_tag": {
        "ru": "У вас нет тега! Укажите в настройках телеграма тег.\n\nИнструкция:\n- Нажмите на кнопку \"Настройки\" в боковом меню.\n- Выберите опцию \"имя пользователя\"\n- Заполните поле ввода и нажмите галочку для сохранения.",
        "en": "You don't have a tag! Specify a tag in the Telegram settings.\n\nInstructions:\n- Click the \"Settings\" button in the side menu.\n- Select the \"username\" option.\n- Fill in the input field and click the checkmark to save.",
        "fr": "Vous n'avez pas de tag ! Spécifiez un tag dans les paramètres de Telegram.\n\nInstructions :\n- Cliquez sur le bouton \"Paramètres\" dans le menu latéral.\n- Sélectionnez l'option \"nom d'utilisateur\".\n- Remplissez le champ de saisie et cliquez sur la coche pour enregistrer.",
        "de": "Sie haben keinen Tag! Geben Sie einen Tag in den Telegram-Einstellungen an.\n\nAnleitung:\n- Klicken Sie auf die Schaltfläche \"Einstellungen\" im Seitenmenü.\n- Wählen Sie die Option \"Benutzername\".\n- Füllen Sie das Eingabefeld aus und klicken Sie auf das Häkchen, um zu speichern.",
        "tr": "Etiketiniz yok! Telegram ayarlarında bir etiket belirtin.\n\nTalimatlar:\n- Yan menüdeki \"Ayarlar\" düğmesine tıklayın.\n- \"Kullanıcı adı\" seçeneğini seçin.\n- Giriş alanını doldurun ve kaydetmek için onay işaretine tıklayın.",
        "zh": "您没有标签！在Telegram设置中指定一个标签。\n\n说明：\n- 点击侧边菜单中的“设置”按钮。\n- 选择“用户名”选项。\n- 填写输入字段并点击复选标记以保存。",
        "it": "Non hai un tag! Specifica un tag nelle impostazioni di Telegram.\n\nIstruzioni:\n- Clicca sul pulsante \"Impostazioni\" nel menu laterale.\n- Seleziona l'opzione \"nome utente\".\n- Compila il campo di input e clicca sul segno di spunta per salvare."
    },

})

eng = {

}
