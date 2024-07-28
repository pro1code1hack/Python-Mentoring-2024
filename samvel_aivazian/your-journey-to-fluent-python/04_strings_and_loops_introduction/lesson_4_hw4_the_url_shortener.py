import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class URLShortener:
    @staticmethod
    def shorten_url(url):
        return url[:7] + '...' + url[-3:] if len(url) > 10 else url


def main():
    logging.info("Enter a URL: ")
    url = input()
    shortener = URLShortener()
    shortened_url = shortener.shorten_url(url)
    logging.info(f"Shortened URL: {shortened_url}")


if __name__ == "__main__":
    main()
