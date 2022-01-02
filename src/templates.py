__author__ = 'Dror Paz'

from jinja2 import Template

PDF_TEMPLATE = Template('''
<!DOCTYPE html>
<html dir="rtl" >
<head lang="he">
<style>
table tr {
    border-top: 1px  black solid;
}
</style>
    <meta charset="UTF-8">
    <title text-align=center >{{ title }}</title>
</head>
    <h1 style="text-align: center;">{{ title }}</h1>
    <body lang=he text-align=right'>
        {{ table }}
    </body>
</html>
''')

TABLE_STYLE = [{'selector': '',
                'props': [('border', '1px solid lightgrey'), ]},
               {'selector': 'table',
                'props': [('table-layout', 'fixed'),
                          ('width', '100%'),
                          ('border', '1px solid lightgrey'),
                          ('border-collapse', 'collapse'),
                          ]},
               {'selector': 'th',
                'props': [('border-bottom', '1px solid lightgrey'),
                          ('font-family', 'arial'),
                          ('border-collapse', 'collapse'),
                          ('width', '10%')
                          ]},
               {'selector': '.col_heading',
                'props': [('text-align', 'center'),
                          ('border-bottom', '1px solid lightgrey'),
                          ('font-family', 'arial'),
                          ('border-collapse', 'collapse'),
                          ]},
               {'selector': 'tbody td',
                'props': [('border-bottom', '1px solid lightgrey'),
                          ('border-collapse', 'collapse'),
                          ('font-size', '11.5px'),
                          ('font-family', 'arial'),
                          ('text-align', 'center'),
                          ('na_rep', ''),
                          ('width', '35%')
                          ]},
               {'selector': 'tbody tr:nth-child(odd)',
                'props': [('background-color', 'lightblue')]}
               ]
