import webbrowser

gmail = 'https://mail.google.com/mail/u/0/#inbox'
capra_mail = 'https://mail.google.com/mail/u/1/#inbox'
yara_mail = 'https://outlook.office.com/mail/inbox'

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


webbrowser.get(chrome_path).open(gmail)
webbrowser.get(chrome_path).open(capra_mail)
webbrowser.get(chrome_path).open(yara_mail)
