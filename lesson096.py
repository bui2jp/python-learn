import string
#with closeを自動でやってくれる
s = """\

テンプレートの使い方

Hi $name

$contents

xxxxx

"""

t = string.Template(s)
c = t.substitute(name='Mike', contents='bbbbbb')

print(c)