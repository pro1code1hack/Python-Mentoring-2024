import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True


def main():
    logging.info("Enter an IP address: ")
    ip = input().strip()
    if is_valid_ip(ip):
        logging.info("Correct")
    else:
        logging.info("Incorrect")


if __name__ == "__main__":
    main()
