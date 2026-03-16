from __future__ import annotations

from datetime import datetime, timedelta

TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def create_interval_before(delta: timedelta, end: datetime | None = None, time_format: str = TIME_FORMAT) -> str:
    """
    Create an interval string for the Genesys API.
    :param delta: The time delta to subtract from the end date.
    :param end: The end date. If None, use the current date and time.
    :param time_format: The time_format for the datetime string. Default is "%Y-%m-%dT%H:%M:%S.%fZ".
    :return: A string representing the interval in the format "start/end".
    """
    if end is None:
        end = datetime.today()
    start = end - delta
    return create_interval(start, end, time_format)

def create_interval_after(delta: timedelta, start: datetime | None = None, time_format: str = TIME_FORMAT) -> str:
    """
    Create an interval string for the Genesys API.
    :param delta: The time delta to add to the start date.
    :param start: The start date. If None, use the current date and time.
    :param time_format: The time_format for the datetime string. Default is "%Y-%m-%dT%H:%M:%S.%fZ".
    :return: A string representing the interval in the format "start/end".
    """
    if start is None:
        start = datetime.today()
    end = start + delta
    return create_interval(start, end, time_format)

def create_interval(start: datetime, end: datetime, time_format: str = TIME_FORMAT) -> str:
    """
    Create an interval string for the Genesys API.
    :param start: The start date.
    :param end: The end date.
    :param time_format: The time_format for the datetime string. Default is "%Y-%m-%dT%H:%M:%S.%fZ".
    :return: A string representing the interval in the format "start/end".
    """
    return f"{start.strftime(time_format)}/{end.strftime(time_format)}"

def create_days_before_interval(days: int = 1, end: datetime | None = None, time_format: str = TIME_FORMAT) -> str:
    """
    Create an interval string for the Genesys API.
    :param days: The number of days to subtract from the end date.
    :param end: The end date. If None, use the current date and time.
    :param time_format: The time_format for the datetime string. Default is "%Y-%m-%dT%H:%M:%S.%fZ".
    :return: A string representing the interval in the format "start/end".
    """
    if days < 1:
        raise ValueError("days must be greater than 0")

    if end is None:
        end = datetime.today()
    end = datetime(end.year, end.month, end.day, 23, 59, 59)
    start = end - timedelta(days=days)
    return create_interval(start, end, time_format)