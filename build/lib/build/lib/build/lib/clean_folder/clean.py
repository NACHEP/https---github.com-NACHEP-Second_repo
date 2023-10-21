import sys
from pathlib import Path
import shutil
#from normalize import normalize
import re



CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
#CYRILLIC_SYMBOLS = tuple(CYRILLIC_SYMBOLS)

for c, t in zip(CYRILLIC_SYMBOLS , TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()
    
def normalize(name):
    name = re.sub(r"\W", "_", name.translate(TRANS))
    return name



# if __name__ == "__main__":
#     INPUT = "доброго_дня! 13.10.23"
#     normalized_line = normalize(INPUT)
#     print(normalized_line)
EXTENSIONS = {
    'images': ('.JPEG', '.PNG', '.JPG', '.SVG'),
    'videos': ('.AVI', '.MP4', '.MOV', '.MKV'),
    'documents': ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'),
    'music': ('.MP3', '.OGG', '.WAV', '.AMR'),
    'archives': ('.ZIP', '.GZ', '.TAR'),
    'others': ()}

extensions_known = set()
unknown_extensions = set()

def get_extensions(name):
    return Path(name).suffix.upper()

def sort_by_category(file_path, category):
    destination_folder = Path(category)
    destination_folder.mkdir(parents=True, exist_ok=True)
    update_name = normalize(file_path.stem) + file_path.suffix
    update_path = destination_folder / update_name
    file_path.rename(update_path)
    if category == 'archives':
        shutil.unpack_archive(str(update_path), str(destination_folder))
        update_path.unlink()

def skan(folders_path):
    global extensions_known
    global unknown_extensions
    
    for item in folders_path.iterdir():
        if item.is_file():
            extension = get_extensions(item.name)
            if extension in EXTENSIONS['images']:
                sort_by_category(item, 'images')
            elif extension in EXTENSIONS['videos']:
                sort_by_category(item, 'videos')
            elif extension in EXTENSIONS['documents']:
                sort_by_category(item, 'documents')
            elif extension in EXTENSIONS['music']:
                sort_by_category(item, 'music')
            elif extension in EXTENSIONS['archives']:
                sort_by_category(item, 'archives')
            else:
                sort_by_category(item, 'others')
                unknown_extensions.add(extension)
            extensions_known.add(extension)
        elif item.is_dir():
            skan(item)
            if not any(True for _ in item.iterdir()):
                item.rmdir()

    print(extensions_known)
    print(unknown_extensions)


def start():
    if sys.argv[1]:
        folder_path = Path(sys.argv[1])
        skan(folder_path)
        print("Сортировка файлов завершена.")

        



# if __name__ == "__main__":
#     folder_path = Path(sys.argv[1])
#     skan(folder_path)
    
#     # Дополнительная логика после завершения сортировки
#     print("Сортировка файлов завершена.")


