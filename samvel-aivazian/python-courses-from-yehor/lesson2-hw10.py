def url_shortener() -> None:
    """
    Shorten a URL by retaining the first 7 characters and the last 3 characters.
    """
    url = input("Enter a URL: ")

    # Check if the URL is long enough to be meaningfully shortened
    if len(url) > 10:
        shortened_url = f"{url[:7]}...{url[-3:]}"
    else:
        shortened_url = url  # If the URL is too short, return it as is

    print(f"Shortened URL: {shortened_url}")


if __name__ == "__main__":
    url_shortener()
