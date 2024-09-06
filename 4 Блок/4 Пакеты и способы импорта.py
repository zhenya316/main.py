#from modules.package1.package2.module3 import main # абсолютный импорт полностью указали дорогу к файлу, слишком долго
from .module3 import main       # относительный импорт, если ошибка: ImportError: attempted relative import with no known parent package
# сделать входную  точку через файл main, или сделать абсолютный импорт
# from ..module3 import main    # .. подняться повыше в директории