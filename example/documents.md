# 使い方
## Setting


config.txt

```
[config]
title : Test Document
stylesheet : css/style.css
directory : example/
user : inner

[menu]
インデックス : index.md
・準備 : install.md
・使い方 : documents.md
・Markdon : markdown.md

[header]
title : Document-builder
comments : Markdown のドキュメントビルダーです。（ここの内容はテストしているだけなので適当です）

[footer]
text : @copyright 2015 inner
```


## Document の作成

```
$ cd document-builder
$ python3 run.py
```

