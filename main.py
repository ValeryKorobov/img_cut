from pathlib import Path

from PIL import Image
from rembg import remove


def remove_magic():
    """Loop through and cut the background from each picture in the list."""
    extensions = ['*.jpg', '*.png']
    files = []
    for ext in extensions:
        files.extend(Path('input_pics').glob(ext))

    for index, file in enumerate(files):
        input_path = Path(file)
        file_name = input_path.stem
        output_path = f'output_pics/{file_name}_output.png'

        input_pic = Image.open(input_path)
        output_pic = remove(input_pic)
        output_pic.save(output_path)

        print(f'Completed: {index + 1}/{len(files)}')


def main():
    remove_magic()


if __name__ == '__main__':
    main()
