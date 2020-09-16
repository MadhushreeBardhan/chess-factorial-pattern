import webbrowser
import os

html_tag = ''
for row in range(8):
    start_tag = '<tr>'
    for col in range(8):
        total = row + col
        if total % 2 == 0:
            start_tag = start_tag \
                + '<td height=30px width=30px bgcolor=#FFFFFF></td>'
        else:
            start_tag = start_tag \
                + '<td height=30px width=30px bgcolor=#000000></td>'
    start_tag = start_tag + '</tr>'
    html_tag = html_tag + start_tag
start = \
    '''<!DOCTYPE html>
    <html>
    <head>
    <title>Chess Board</title>
    <meta http-equip=\"content-type\" content=\"text/html; charset=UTF-8\">
    </head>
    <body>
    <h3>Chess Board using nested for loop created by Madhushree</h3>
    <table width=\"270px\" cellspacing=\"0px\" cellpadding=\"0px\" border=\"1px\">
    {}
    </table>
    </body>
    </html>
    '''.format(html_tag)
with open('chess_html.html', 'w') as f:
    f.write(start)

url = os.path.abspath(os.getcwd()) + '/chess_html.html'
webbrowser.open(url, new=2)