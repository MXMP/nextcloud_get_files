import owncloud

LOGIN = 'your_login'
PWD = 'your_password'
PATH = 'testdir'


nc = owncloud.Client('https://nc.nl.tab.digital/')
nc.login(LOGIN, PWD)

nc.get_file(file.path)
