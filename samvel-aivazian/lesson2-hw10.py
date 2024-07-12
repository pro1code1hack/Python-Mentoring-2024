def url_shortener() -> None:
    url = input("Enter a URL: ")
    shortened_url = f"{url[:7]}...{url[-3:]}"
    print(f"Shortened URL: {shortened_url}")


url_shortener()
