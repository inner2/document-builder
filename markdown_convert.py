
import markdown


markdown_text = '''# Markdown
## 見出し Heading
- 見出しはシャープ記号を用いる
- HTML の Heading タグに相当する
- シャープ数により見出しの大きさを変更できる

```
# (<h1>タグに相当)
## (<h2>タグに相当)
....
###### (<h6>まで存在)
```

## Bold と Italic
アスタリスクで囲むと *itaric* もしくは **bold** にできる

## Link
カッコを使ってリンクも作成可能
```
[Link_name](www.hogehoge.com)
```
## Images
Markdown ファイル内に画像等を添付する
```
![alt text](http://example.com/logo.png)
![alt text](image/img.png)
```

'''


def markdown_c():
    md = markdown.Markdown()
    # makedown -> html
    text1 = markdown_text.split('```')
    # text1 = markdown_text.replace('```', 'o')
    print(len(text1))
    for i in range(len(text1)):
        if i % 2 == 0:
            html = md.convert(text1[i])
            print(html)
        else:
            print(text1[i])



# Main
if __name__ == '__main__':
    # module gfm
    # gfm_c()

    # markdown
    markdown_c()

    print("end")