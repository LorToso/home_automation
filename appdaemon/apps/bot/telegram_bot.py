import appdaemon.plugins.hass.hassapi as hass
import telebot
import json


class TelegramBot(hass.Hass):
    auth_token: str
    chat_id: str
    bot: telebot.TeleBot

    def initialize(self):
        self.auth_token = self.args["auth_token"]
        self.chat_id = self.args["chat_id"]
        self.bot = telebot.TeleBot(self.auth_token)

        self.listen_event(self.on_telegram_message, "telegram_text")

    def on_telegram_message(self, event_name, data, kwargs):
        self.log(f"--on_event: event_name: {event_name}, data: {data}, kwargs: {kwargs}")
        self.log(f"text: {data['text']}")
        ## Quotationmarks are strange. Need to be double
        json_text = json.loads(data["text"].replace("'", '"'))

        if self.is_voice_message(json_text):
            self.download_voice_message(json_text["voice"]["file_id"])

    def is_voice_message(self, json_text):
        return "voice" in json_text

    def download_voice_message(self, voice_msg_file_id: str):
        file_info = self.bot.get_file(voice_msg_file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)

        with open('new_file.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)

# {
#     "event_type": "telegram_text",
#     "data": {
#         "user_id": 326651817,
#         "from_first": "Lorenzo",
#         "id": 48,
#         "from_last": "Toso",
#         "chat_id": 326651817,
#         "text": "{'message_id': 48, 'date': 1619307342, 'chat': {'id': 326651817, 'type': 'private', 'first_name': 'Lorenzo', 'last_name': 'Toso'}, 'entities': [], 'caption_entities': [], 'photo': [], 'voice': {'file_id': 'AwACAgIAAxkBAAMwYISrTlueUR5hgoNub6KtOkrTzO0AAg0MAAKuUyhIaGmuX-whDSMfBA', 'file_unique_id': 'AgADDQwAAq5TKEg', 'duration': 3, 'mime_type': 'audio/ogg', 'file_size': 10403}, 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 326651817, 'first_name': 'Lorenzo', 'is_bot': False, 'last_name': 'Toso', 'language_code': 'de'}}"
#     },
#     "origin": "LOCAL",
#     "time_fired": "2021-04-24T23:35:42.424618+00:00",
#     "context": {
#         "id": "0d29f6f460ff2be16003ba4717372fc9",
#         "parent_id": null,
#         "user_id": null
#     }
# }