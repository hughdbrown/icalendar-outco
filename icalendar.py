#!/usr/bin/env python
from __future__ import print_function

from hashlib import sha1
from datetime import datetime
from json import loads


EVENT_HEAD_FMT = """BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VTIMEZONE
TZID:{time_zone}
X-LIC-LOCATION:{time_zone}
BEGIN:DAYLIGHT
DTSTART:19700308T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU
TZNAME:MDT
TZOFFSETFROM:-0700
TZOFFSETTO:-0600
END:DAYLIGHT
BEGIN:STANDARD
DTSTART:19701101T020000
RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU
TZNAME:MST
TZOFFSETFROM:-0600
TZOFFSETTO:-0700
END:STANDARD
END:VTIMEZONE"""

EVENT_FMT = """BEGIN:VEVENT
UID:{hash}
DTSTART;TZID={time_zone}:{start_time}
DTEND;TZID={time_zone}:{end_time}
SUMMARY:{summary}
URL:{url}
DESCRIPTION:{url}
END:VEVENT"""


def process_event(kwargs):
    return EVENT_FMT.format(**kwargs)


def print_ics(events, tz):
    args = {
        'hash': sha1(str(events)).hexdigest(),
        'time_zone': tz,
    }
    print(EVENT_HEAD_FMT.format(**args))
    for event in events:
        extra = {
            'start_time': event['start_time'],
            'end_time': event['end_time'],
            'hash': sha1(str(event)).hexdigest(),
            'summary': event['summary'],
            'url': event.get('url', ""),
        }
        args.update(extra)
        print(process_event(args))
    print("""END:VCALENDAR""")


def outco(unformatted_events):
    datefmt = "%Y%m%dT%H%M%S"
    return [
        {
            "start_time": datetime(*event["start"]).strftime(datefmt),
            "end_time": datetime(*event["end"]).strftime(datefmt),
            "summary": event["msg"],
            "url": event.get("url", ""),
        }
        for event in unformatted_events
    ]


if __name__ == '__main__':
    unformatted = loads(open("events.json").read())
    events = outco(unformatted)
    print_ics(events, tz="America/Los_Angeles")
