from datetime import datetime
import re


current_date = str(datetime.now())[:-7]
current_date = re.sub(r"[ ,.;@#?!&$:-]+", '', current_date)

print(current_date)


