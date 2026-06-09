#==========DATE_TIME_UTILS==========


from datetime import datetime, date, timedelta


def parse_deadline(dead_line_str : str) -> datetime:

    return datetime.strptime(dead_line_str, "%Y/%m/%d %H:%M")


def format_deadline(dt : datetime) -> str:

    if dt is None:

        raise ValueError("No dead line.")

    return dt.strftime("%Y/%m/%d %H:%M") 