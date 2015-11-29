# Markdown Documentation Builder
# Module
import markdown
import configparser

# template
html_temp = '''
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="{{ stylesheet }}">
<title>{{ title }}</title>
</head>
<body>
<div id="wrapper">
<div id="header">
{{ header }}
</div>  <!-- header -->
<div id="sidebar">
<h3>Menu</h3>
{{ sidebar }}
</div>  <!-- sidebar -->
<div id="contents">
{{ contents }}
</div>  <!-- contents -->
<div id="footer">
{{ footer }}
</div>  <!-- footer -->
</div>  <!-- wrapper -->
</body>
</html>
'''
link_temp = '''<p><a href="{{ link }}">{{ label }}</a></p>'''


# build documents
def build_documents():
    # 変数
    sidebar_menu = ''
    builder_config = {'title': 'title', 'stylesheet': 'style.css', 'directory': 'example/'}

    # read config file
    config = configparser.ConfigParser()
    config.read('setting2.txt')
    builder_config['title'] = config['config']['title']
    builder_config['stylesheet'] = config['config']['stylesheet']

    # header
    header = '<h1>' + config['header']['title'] + '</h1><p>' + config['header']['comments'] + '</p>'

    # footer
    footer = config['footer']['text']

    # create sidebar menu
    for label in config['menu']:
        md_file = config['menu'][label]
        link = md_file.replace('.md', '.html')

        elements = link_temp.replace('{{ link }}', link)
        elements = elements.replace('{{ label }}', label)
        sidebar_menu = sidebar_menu + elements + ''
    print(sidebar_menu)

    # html template の更新
    html_temp2 = html_temp.replace('{{ stylesheet }}', builder_config['stylesheet'])
    html_temp2 = html_temp2.replace('{{ title }}', builder_config['title'])
    html_temp2 = html_temp2.replace('{{ header }}', header)
    html_temp2 = html_temp2.replace('{{ sidebar }}', sidebar_menu)
    html_temp2 = html_temp2.replace('{{ footer }}', footer)

    # convert to html file
    for label in config['menu']:
        md_file = config['menu'][label]
        link = md_file.replace('.md', '.html')
        md_file = 'example/' + md_file
        link = 'example/' + link
        convert_markdown2(md_file, link, html_temp2)


# convert to html file
def convert_markdown2(md_file, html_file, html):
    print('convert to html')
    print(html_file)
    print(md_file)

    md = markdown.Markdown()
    fr = open(md_file, 'r')
    contents_text = fr.read()
    fr.close()
    contents = ''

    contents_list = contents_text.split('```')
    for i in range(len(contents_list)):
        if i % 2 == 0:
            contents = contents + md.convert(contents_list[i])
        else:
            contents_list[i] = contents_list[i].replace('<', '&lt;')
            contents = contents + '<pre><code>' + contents_list[i] + '</code></pre>'

    kai = '''<pre><code>
'''
    contents = contents.replace(kai, '<pre><code>')
    html = html.replace('{{ contents }}', contents)

    # create html file
    fw = open(html_file, 'w')
    fw.write(html)
    fw.close()


# Main
if __name__ == '__main__':
    print("program start")

    build_documents()

    print("program end")