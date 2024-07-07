from datetime import datetime

my_date = "07.07.2024"
date_object = datetime.strptime(my_date, "%d.%m.%Y")
print(date_object.strftime("%w"))
print(date_object.strftime("%A"))
