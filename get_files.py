import owncloud

oc = owncloud.Client('https://nc.nl.tab.digital/')
oc.login('your_login', 'your_password')

for file in oc.list('testdir'):
    oc.get_file(file.path)
