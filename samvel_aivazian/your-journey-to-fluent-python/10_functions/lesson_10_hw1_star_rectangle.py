import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def draw_rectangle():
    width = 7
    height = 6
    for i in range(height):
        if i == 0 or i == height - 1:
            logging.info('*' * width)
        else:
            logging.info('*' + ' ' * (width - 2) + '*')


if __name__ == "__main__":
    draw_rectangle()
