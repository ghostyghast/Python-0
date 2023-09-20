import time
from datetime import datetime

print("Seconds since  since Janurary 1, 1970: {:,.4F} or {:e}".format(time.time(), time.time()))
print(datetime.now().strftime("%B %d %Y"))