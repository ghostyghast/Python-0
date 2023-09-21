import time
from datetime import datetime

print("Seconds since Janurary 1, 1970:", end=' ')
print("{:,.4f} or {:.2e}".format(time.time(), time.time()))
print(datetime.now().strftime("%B %d %Y"))
