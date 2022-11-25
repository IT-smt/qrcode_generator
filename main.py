import qrcode


def create_qrcode(box_size, border, link, path, fill_color, back_color):
    """Функция создает QR-код"""
    qr = qrcode.QRCode(
        box_size=box_size,
        border=border
    )
    qr.add_data(link)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(path)


def main():
    """Функция принимает данные от пользователя и передает их"""
    box_size = int(input("Введите размер QR-кода: "))
    border = int(input("Введите границу QR-кода: "))
    link = input("Введите ссылку на которую будет переход по QR-коду: ")
    path = input(
        "Введите путь (В конце введите название файла. Пример: D:\qrcode.png): ")
    fill_color = input("Введите цает QR-кода: ")
    back_color = input("Введите цвет фона: ")
    create_qrcode(box_size=box_size, border=border, link=link,
                  path=path, fill_color=fill_color, back_color=back_color)


if __name__ == "__main__":
    main()
