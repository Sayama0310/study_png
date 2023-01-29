from bytes_operation.purity_format import purity_hex_format_bytes


if __name__ == '__main__':
    with open('sample_png_image/cat01.png', mode='rb') as img:
        png_bytes = img.read()
        print(purity_hex_format_bytes(png_bytes)[:200])