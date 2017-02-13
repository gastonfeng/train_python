from datetime import datetime

import pytz
from pytz import UTC

ct = datetime.now(tz=pytz.timezone('Asia/Shanghai')).replace(tzinfo=None)
#ct= ct.replace(tzinfo=None)
if ct.hour>7:
    print 'ok'
interval = (ct - datetime.strptime(ct.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")).seconds / 60

print ct