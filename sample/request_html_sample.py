from requests_html import HTMLSession

session = HTMLSession()

# r = session.get('https://python.org/')
r = session.get('http://python-requests.org')
# print(r.html.links)

# print('absolute links')

# print(r.html.absolute_links)
# about = r.html.find('#about', first=True)
# print(about.attrs)
r.html.render()
