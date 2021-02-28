from datetime import datetime
now = datetime.now()
hours = str((now.hour + 8 + (now.minute + 30) // 60) % 24)
minutes = str((now.minute + 30) % 60)
print('0' * (2 - len(hours)), hours, ':', '0' * (2 - len(minutes)), minutes, sep='')
