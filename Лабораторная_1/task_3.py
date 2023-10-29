# TODO Найдите количество книг, которое можно разместить на дискете

TOTAL_VOLUME_OF_DISK = 1.44  # Объём дискеты (Мб)
PAGES_IN_BOOK = 100  # Количество страниц в книге
STR_ON_PAGE = 50  # Число строк на странице
SYMB_IN_STR = 25  # Количество символов в строке
VOLUME_OF_ONE_SYMB = 4  # Объём для хранения кода одного символа (байт)

tot_vol_of_one_book = VOLUME_OF_ONE_SYMB * SYMB_IN_STR * STR_ON_PAGE * PAGES_IN_BOOK  # Объём одной книги (байт)
count_books = round(TOTAL_VOLUME_OF_DISK * (1024 ** 2) // tot_vol_of_one_book)  # Объём дискеты берём в байтах

print("Количество книг, помещающихся на дискету:", count_books)
