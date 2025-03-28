import qrcode

first_name = "I Pardhiv"
last_name = "Sai Kumar"
email = "saipardhiv01@gmail.com"
phone_number = "9959976205"

vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{first_name};{last_name};;;\nFN:{first_name}\nEMAIL:{email};TYPE=INTERNET:{email}" f"\nTEL;TYPE=CELL:{phone_number}\nEND:VCARD"

img = qrcode.make(vcard)
img.save('contact.png')