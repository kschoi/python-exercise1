from urllib.request import *
from html.parser import HTMLParser


class ImageParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)


def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    print('\n'.join( sorted(dataSet) ))


def main():
    url = "http://www.google.com/"
    request = Request(url)
    response = urlopen(request)
    charset = response.info().get_param('charset')
    data = response.read().decode(charset)
    response.close()

    print("\n>>>>>>>>> Fetch Images from", url)
    parse_image(data)


if __name__ == '__main__':
    main()

