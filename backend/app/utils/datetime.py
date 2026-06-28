from datetime import datetime
from zoneinfo import ZoneInfo

JAKARTA_TZ = ZoneInfo("Asia/Jakarta")


def now_jakarta() -> datetime:
    """
    Menghasilkan waktu sekarang dengan timezone Asia/Jakarta.
    """
    return datetime.now(JAKARTA_TZ)