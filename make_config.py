import configparser

config = configparser.ConfigParser()

# 変数
conf = {'title': 'Test title', 'stylesheet': 'css/style.css', 'directory': 'example/', 'user': 'inner'}
menu = {'ホーム': 'index.md', '準備': 'install.md', '使い方': 'documents.md', 'Markdown': 'markdown.md'}
header = {'title': 'Document-builder', 'comments': 'ここの内容は適当です。'}
footer = {'text': '@copyright 2015 inner'}

# config
config['config'] = conf
config['menu'] = menu
config['header'] = header
config['footer'] = footer

# write
with open('config.txt', 'w') as configfile:
    config.write(configfile)

print("make config file")