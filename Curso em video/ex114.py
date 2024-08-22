import urllib.request
from urllib.error import URLError

try:
    site = urllib.request.urlopen("https://www.youtube.com/watch?v=8jAykqxIeqw")
except URLError:
    print('Não consegui acessar')
else:
    print('O site está acessível')
