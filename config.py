import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "28243586")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7427875913:AAECLn_AjdTMSizPFEnHQPwm8G855Hi2EIY")  # ⚠️ Required

    # database config
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://madarazbotz:PIxkrEpWc8KhiUci@cluster0.ispey.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME = os.environ.get("DB_NAME", "cluster0")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/3fdd20984777d4380f854.jpg")
    ADMIN = int(os.environ.get('ADMIN', '1341294921 5340652544 919147646 1844080002'))  # ⚠️ Required
    DEFAULT_WELCOME_MSG = os.environ.get("WELCOME_MSG", "Hey {user},\nYour Request Approved ✅,\n\nWelcome to **{title}**")
    DEFAULT_LEAVE_MSG = os.environ.get("LEAVE_MSG", "By {user},\nSee You Again 👋\n\nFrom **{title}**")

    # user client config
    SESSION = os.environ.get("SESSION", "AQGu9oIAZSF5zqS4GFi7cfBiIpREHeD3V6_B0VaiTEV2_pVsaEsOczoh_rm2Q4PdTI1wc3E7aqsK-BA1_NvfDDC8qIBp6GF0vAIRkO9PtJGlU2LJANrfPAOkF-z2ZTSI9pyfbHen9jnOyTga_6WPEfl2jl03Ld7fDmg0ygfiM3wl1RUQmCloRkKtAWG5vyDq1x07OI9wPAPBaedKUIRvJPPYP-96QL_nrNdfNf2WaMbfX2VbA9J09qEeMK8l4KbwvFDMFbTnewE6jIJS3h-5px08mbCGcl0STOEEM0r9_mt_01V0K6NPpIKUUJ_KXbsQO9Qc6JS0LtF95c59RRWAN9AwIN8fEAAAAAFZFXRRAA")  # ⚠️ Required @SnowStringGenBot

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class TxT(object):

    HELP_MSG = """
<b> ADMIN Available commands:- </b>

➜ /set_welcome - To set custom welcome message (support photo & video & animation or gif)
➜ /set_leave - To set custom leave message (support photo & video & animation or gif)
➜ /option - To toggle your welcome & leave message also auto accept (whether it'll show to user or not and will auto accept or not)
➜ /auto_approves - To toggle your auto approve channel or group
➜ /status - To see status about bot
➜ /restart - To restart the bot
➜ /broadcast - To brodcast the users (only those user who has started your bot)
➜ /acceptall - To accept all the pending join requests
➜ /declineall - To decline all the pending join requests

⚠️ <b> Support HTML & Markdown formating in welcome or leave message for more info <a href=https://core.telegram.org/api/entities#:~:text=%2C%20MadelineProto.-,Allowed%20entities,-For%20example%20the> Link </a>. </b>


<b>⦿ Developer:</b> <a href=https://t.me/unreal_x_bot>ᴜɴʀᴇᴀʟ ʙᴏᴛ ❄️</a>
"""
