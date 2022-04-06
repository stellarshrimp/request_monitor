#!/usr/bin/env python3

import re
import datetime
import sys
import json
import urllib.request


if len(sys.argv) < 3:
    sys.exit(1)
CHECK_INTERVAL = int(sys.argv[1])
WEBHOOK_URL = sys.argv[2]

TODAY_DATE = datetime.datetime.now(datetime.timezone.utc)
MIN_DATE = TODAY_DATE - datetime.timedelta(hours=CHECK_INTERVAL)

COUNT_GET = 0
COUNT_POST = 0
for line in sys.stdin:
    PATTERN = "\[(\d+\-\d+\-\d+T\d+\:\d+\:\d+Z)"
    match = re.search(PATTERN, line)
    if match:
        DATE_TEXT = match.group(1)
        DATE_ITEM = datetime.datetime.strptime(DATE_TEXT, "%Y-%m-%dT%H:%M:%S%z")
        if DATE_ITEM > MIN_DATE:
            if "method: GET" in line:
                COUNT_GET += 1
            if "method: POST" in line:
                COUNT_POST += 1

REQ_DATA = {"text":"requests per last " + str(CHECK_INTERVAL) + " hours: GET: " + str(COUNT_GET) + ", POST: "+ str(COUNT_POST)}
JSON_DATA = json.dumps(REQ_DATA).encode('utf8')
REQ = urllib.request.Request(WEBHOOK_URL, data=JSON_DATA, headers={'content-type': 'application/json'})
RESPONSE = urllib.request.urlopen(REQ)
print("Send to Slack result: " + RESPONSE.read().decode('utf8'))
