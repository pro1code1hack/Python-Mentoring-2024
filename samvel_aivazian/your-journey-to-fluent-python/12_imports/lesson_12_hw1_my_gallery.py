import argparse
import os

from PIL import Image


def resize_images(input_folder, output_folder, thumbnail_size=(128, 128)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                img.thumbnail(thumbnail_size)
                img.save(os.path.join(output_folder, filename))


def generate_gallery(thumbnails_folder, output_file):
    with open(output_file, 'w') as f:
        f.write('<html><head><title>Image Gallery</title></head><body>\n')
        f.write('<h1>Image Gallery</h1>\n')
        f.write('<div style="display: flex; flex-wrap: wrap;">\n')

        for filename in os.listdir(thumbnails_folder):
            if filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp')):
                img_path = os.path.join(thumbnails_folder, filename)
                full_img_path = os.path.abspath(img_path)
                f.write(
                    f'<a href="{full_img_path}" target="_blank"><img src="{img_path}" style="margin: 10px; border: 1px solid #ccc;"></a>\n')

        f.write('</div>\n')
        f.write('</body></html>\n')


def main():
    parser = argparse.ArgumentParser(description='Generate an HTML image gallery from a folder of images.')
    parser.add_argument('input_folder', type=str, help='The folder containing the images.')
    parser.add_argument('output_folder', type=str, help='The folder to save the thumbnails and HTML file.')
    parser.add_argument('--thumbnail_size', type=int, nargs=2, default=(128, 128),
                        help='The size of the thumbnails (width height).')

    args = parser.parse_args()

    thumbnails_folder = os.path.join(args.output_folder, 'thumbnails')
    resize_images(args.input_folder, thumbnails_folder, tuple(args.thumbnail_size))
    generate_gallery(thumbnails_folder, os.path.join(args.output_folder, 'gallery.html'))


if __name__ == '__main__':
    main()
