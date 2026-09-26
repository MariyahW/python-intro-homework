from datetime import datetime
now=datetime.now()
formatted=now.strftime("%B %d, %Y")
print(f"Today is {formatted}.")