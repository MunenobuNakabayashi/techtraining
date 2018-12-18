import os
import logging
import json
import urllib.request

# ���O�ݒ�
logger = logging.getLogger()
logger.setLevel(logging.INFO)

##### def lambda_handler(event, context):
def handle_slack_event(event, context):
    
    # ��M�f�[�^��Cloud Watch���O�ɏo��
    logging.info(json.dumps(event))

    # Slack��Event API�̔F��
    if "challenge" in event:
        return event["challenge"]

    # token�̃`�F�b�N
    if not is_verify_token(event):
         return "OK"    

    # �{�b�g�ւ̃����V�����łȂ��ꍇ
    if not is_app_mention(event):
        return "OK"    

    # Slack�Ƀ��b�Z�[�W�𓊍e����
    ##### post_message_to_channel(event.get("event").get("channel"), "Hello, Slack Bot!")
    post_message_to_channel("#times-nakabayashi", "Python�ł��B")
    return 'OK'

def post_message_to_channel(channel, message):
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    }
    
    data = {
        "token": os.environ["SLACK_BOT_VERIFY_TOKEN"],
        "channel": channel,
        "text": message,
        "username": "edojou.chabouzu",
        "icon_emoji": ":blowfish:",
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), method="POST", headers=headers)
    urllib.request.urlopen(req)

def is_verify_token(event):

    # �g�[�N�����`�F�b�N    
    token = event.get("token")
    if token != os.environ["SLACK_BOT_VERIFY_TOKEN"]:
        return False
    return True
    
def is_app_mention(event):
    ### return event.get("event").get("type") == "app_mention"
    return event.get("type") == "app_mention"
