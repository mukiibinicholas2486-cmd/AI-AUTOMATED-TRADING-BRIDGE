
import os
from dotenv import load_dotenv

load_dotenv()

def get_bool(name, default=False):
    return os.getenv(name, str(default)).lower() in (
        "true", "1", "yes"
    )

class Config:

    PAPER_MODE = get_bool("PAPER_MODE", True)
    LIVE_TRADING_ENABLED = get_bool(
        "LIVE_TRADING_ENABLED", False
    )

    ACTIVE_BROKER = os.getenv(
        "ACTIVE_BROKER", "paper"
    )

    RISK_PER_TRADE = float(
        os.getenv("RISK_PER_TRADE", "0.005")
    )

    MAX_DAILY_LOSS = float(
        os.getenv("MAX_DAILY_LOSS", "2")
    )

    MAX_OPEN_TRADES = int(
        os.getenv("MAX_OPEN_TRADES", "2")
    )

    RISK_REWARD_RATIO = float(
        os.getenv("RISK_REWARD_RATIO", "3")
    )

    MIN_CONFIDENCE = int(
        os.getenv("MIN_CONFIDENCE", "75")
    )

    TIMEFRAME = os.getenv("TIMEFRAME", "M5")
    HIGHER_TIMEFRAME = os.getenv(
        "HIGHER_TIMEFRAME", "H1"
    )

    DERIV_APP_ID = os.getenv("DERIV_APP_ID", "")
    DERIV_API_TOKEN = os.getenv("DERIV_API_TOKEN", "")
    DERIV_SYMBOL = os.getenv("DERIV_SYMBOL", "R_100")
    DERIV_CURRENCY = os.getenv("DERIV_CURRENCY", "USD")
    DERIV_STAKE = float(os.getenv("DERIV_STAKE", "1"))

    MT5_LOGIN = os.getenv("MT5_LOGIN", "")
    MT5_PASSWORD = os.getenv("MT5_PASSWORD", "")
    MT5_SERVER = os.getenv("MT5_SERVER", "")
    MT5_PATH = os.getenv("MT5_PATH", "")

    EXNESS_ENABLED = get_bool("EXNESS_ENABLED", False)

    DASHBOARD_PORT = int(
        os.getenv("DASHBOARD_PORT", "8501")
    )

config = Config()
