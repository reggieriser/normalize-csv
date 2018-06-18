import sys

import csv
import fileinput
import re
from datetime import datetime, timedelta


def utf8_file():
    """
    A generator that converts the input (either file or stdin-based) to UTF-8.  Any
    invalid UTF-8 characters are replaced by the Unicode Replacement Character.

    :return: Yields each line of the input, decoded/adjusted to UTF-8.
    """
    for row in fileinput.input(mode="rb"):
        yield row.decode("utf-8", "replace")


def convert_to_timedelta(duration_str):
    """
    Converts a duration string to a timedelta object.

    :param duration_str: A string representing a duration in HH:MM:SS.MS format.
    :return: A timedelta object representing the duration.
    """
    hours_str, minutes_str, seconds_str, milliseconds_str = re.split(
        r"[:.]", duration_str
    )
    return timedelta(
        hours=int(hours_str),
        minutes=int(minutes_str),
        seconds=int(seconds_str),
        milliseconds=int(milliseconds_str),
    )


if __name__ == "__main__":
    reader = csv.DictReader(utf8_file())

    writer = csv.DictWriter(sys.stdout, reader.fieldnames)
    writer.writeheader()

    for row_number, row in enumerate(reader, 1):
        try:
            # Note: Could use pytz for better time zone support, but that brings in an external
            # dependency which I'd like to avoid to make this simpler for others to run/evaluate.
            row["Timestamp"] = (
                    datetime.strptime(row["Timestamp"], "%m/%d/%y %I:%M:%S %p")
                    + timedelta(hours=3)
            ).isoformat()
            row["ZIP"] = row["ZIP"].zfill(5)
            row["FullName"] = row["FullName"].upper()

            foo_duration = convert_to_timedelta(row["FooDuration"])
            row["FooDuration"] = foo_duration.total_seconds()

            bar_duration = convert_to_timedelta(row["BarDuration"])
            row["BarDuration"] = bar_duration.total_seconds()

            # Note: Add them as timedelta objects to avoid floating point precision issues.
            total_duration = foo_duration + bar_duration
            row["TotalDuration"] = total_duration.total_seconds()

            writer.writerow(row)
        except Exception as e:
            sys.stderr.write("WARNING: Dropping data row {} due to error: {}\n".format(row_number, e))
