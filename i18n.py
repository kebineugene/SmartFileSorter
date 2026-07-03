"""Модуль локализации для SmartFileSorter"""
from typing import Dict, List

CURRENT_LANG: str = "ru"

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "ru": {
        "title": "📂 SmartFileSorter",
        "subtitle": "Умная сортировка файлов с безопасным откатом",
        "browse_button": "Обзор...",
        "path_placeholder": "Перетащите папку сюда или нажмите 'Обзор'...",
        "clean_button": "🚀 Начать уборку",
        "cleaning_button": " Идет уборка...",
        "analyzing_button": "⏳ Анализ...",
        "open_folder_button": "📂 Открыть папку",
        "dry_run_checkbox": "👁️ Тестовый режим (не перемещать, только отчет)",
        "sort_by_date_checkbox": " Раскладывать фото/видео по дате (Год/Месяц)",
        "open_after_checkbox": "📂 Открыть папку после завершения",
        "status_waiting": "Ожидание выбора папки...",
        "status_folder_selected": "✓ Папка выбрана. Файлов на: {}",
        "status_error_no_folder": "❌ Ошибка: Сначала выберите папку!",
        "status_error_path": "❌ Ошибка: Указанный путь не существует!",
        "status_error_open_folder": "❌ Сначала выберите существующую папку!",
        "status_cleaning": "⏳ {} (Интерфейс отзывчив!)",
        "status_cleaning_text": "Сортировка файлов...",
        "status_analyzing_text": "Тестовый анализ...",
        "status_cancelled": "⏸ Отменено. Файлы остались на месте.",
        "status_success": "✔ Успех! Разобрано файлов: {} ({})\nОтчет: {}",
        "status_success_dry_run": "👁️ Тестовый прогон завершен!\nПроанализировано файлов: {}\nОтчет: {}",
        "status_success_undo": "\n🛡️ Скрипт отката: undo_sort.bat",
        "status_error": "❌ Ошибка: {}",
        "warning_text": "️ Не используйте для сетевых папок и открытых файлов!",
        "github_link": "🐱 Проект на GitHub | ⭐ Поставьте звезду!",
        "dnd_tip": "💡 Совет: Вы можете перетащить папку прямо в поле ввода!",
        "confirm_title": "⚠️ Внимание!",
        "confirm_message": "После уборки все файлы разлетятся по новым папкам.\n\nЕсли вы чистите Telegram Downloads — старые файлы пропадут из чатов!\n\nНе волнуйтесь: в папке появится undo_sort.bat для отката!\n\nВы готовы продолжить?",
        "language_label": "🌐 Language:",
        "language_ru": "🇷🇺 Русский",
        "language_en": "🇬 English",
        "cat_images": "Изображения",
        "cat_documents": "Документы",
        "cat_archives": "Архивы",
        "cat_music": "Музыка",
        "cat_videos": "Видео",
        "cat_programs": "Программы",
        "cat_images_disk": "Образы",
        "cat_virtualization": "Виртуализация",
        "cat_other": "Разное",
        "month_1": "Январь",
        "month_2": "Февраль",
        "month_3": "Март",
        "month_4": "Апрель",
        "month_5": "Май",
        "month_6": "Июнь",
        "month_7": "Июль",
        "month_8": "Август",
        "month_9": "Сентябрь",
        "month_10": "Октябрь",
        "month_11": "Ноябрь",
        "month_12": "Декабрь",
        "log_filename": "sort_log.txt",
        "log_filename_dry": "dry_run_log.txt",
        "error_folder_not_exists": "Папка не существует: {}",
        "error_not_folder": "Это не папка: {}",
        "error_file_busy": "Файл '{}' занят другой программой",
        "error_busy_short": "Занят другой программой",
        "error_unknown_size": "Размер неизвестен",
        "error_permission_create": "Ошибка: нет прав на создание папки",
        "error_move_failed": "Не удалось переместить '{}': {}",
        "error_save_log": "Не удалось сохранить лог: {}",
        "error_create_undo": "Не удалось создать скрипт отката: {}",
        "bat_header": "SmartFileSorter: Возврат файлов...",
        "bat_done": "Готово! Файлы возвращены на места.",
    },
    "en": {
        "title": "📂 SmartFileSorter",
        "subtitle": "Smart file sorting with safe undo",
        "browse_button": "Browse...",
        "path_placeholder": "Drop a folder here or click 'Browse'...",
        "clean_button": "🚀 Start Sorting",
        "cleaning_button": " Sorting...",
        "analyzing_button": "⏳ Analyzing...",
        "open_folder_button": "📂 Open Folder",
        "dry_run_checkbox": "👁️ Dry Run (don't move, report only)",
        "sort_by_date_checkbox": "📅 Sort photos/videos by date (Year/Month)",
        "open_after_checkbox": "📂 Open folder after completion",
        "status_waiting": "Waiting for folder selection...",
        "status_folder_selected": "✓ Folder selected. Files size: {}",
        "status_error_no_folder": "❌ Error: Please select a folder first!",
        "status_error_path": "❌ Error: The specified path does not exist!",
        "status_error_open_folder": " Please select an existing folder first!",
        "status_cleaning": "⏳ {} (Interface is responsive!)",
        "status_cleaning_text": "Sorting files...",
        "status_analyzing_text": "Dry run analysis...",
        "status_cancelled": "⏸ Cancelled. Files remain in place.",
        "status_success": "✔ Success! Sorted files: {} ({})\nReport: {}",
        "status_success_dry_run": "👁️ Dry run completed!\nFiles analyzed: {}\nReport: {}",
        "status_success_undo": "\n🛡️ Undo script: undo_sort.bat",
        "status_error": "❌ Error: {}",
        "warning_text": "⚠️ Do not use on network folders and open files!",
        "github_link": " Project on GitHub | ⭐ Give it a star!",
        "dnd_tip": "💡 Tip: You can drag & drop a folder directly into the input field!",
        "confirm_title": "⚠️ Warning!",
        "confirm_message": "After sorting, all files will be moved to new folders.\n\nIf you're cleaning Telegram Downloads — old files will disappear from chats!\n\nDon't worry: an undo_sort.bat script will be created for rollback!\n\nAre you ready to continue?",
        "language_label": " Language:",
        "language_ru": "🇺 Русский",
        "language_en": "🇬🇧 English",
        "cat_images": "Images",
        "cat_documents": "Documents",
        "cat_archives": "Archives",
        "cat_music": "Music",
        "cat_videos": "Videos",
        "cat_programs": "Programs",
        "cat_images_disk": "Disk Images",
        "cat_virtualization": "Virtualization",
        "cat_other": "Other",
        "month_1": "January",
        "month_2": "February",
        "month_3": "March",
        "month_4": "April",
        "month_5": "May",
        "month_6": "June",
        "month_7": "July",
        "month_8": "August",
        "month_9": "September",
        "month_10": "October",
        "month_11": "November",
        "month_12": "December",
        "log_filename": "sort_log.txt",
        "log_filename_dry": "dry_run_log.txt",
        "error_folder_not_exists": "Folder does not exist: {}",
        "error_not_folder": "This is not a folder: {}",
        "error_file_busy": "File '{}' is locked by another program",
        "error_busy_short": "Locked by another program",
        "error_unknown_size": "Size unknown",
        "error_permission_create": "Error: no permission to create folder",
        "error_move_failed": "Failed to move '{}': {}",
        "error_save_log": "Failed to save log: {}",
        "error_create_undo": "Failed to create undo script: {}",
        "bat_header": "SmartFileSorter: Restoring files...",
        "bat_done": "Done! Files restored to original locations.",
    },
}


def t(key: str, *args) -> str:
    """Получить перевод по ключу с поддержкой форматирования."""
    lang = CURRENT_LANG
    text = TRANSLATIONS.get(lang, {}).get(key, key)
    if args:
        try:
            return text.format(*args)
        except (IndexError, KeyError):
            return text
    return text


def get_months() -> List[str]:
    """Получить список названий месяцев на текущем языке."""
    return [t(f"month_{i}") for i in range(1, 13)]


def get_categories() -> Dict[str, List[str]]:
    """Получить словарь категорий файлов на текущем языке."""
    return {
        t("cat_images"): [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
        t("cat_documents"): [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".rtf", ".odt"],
        t("cat_archives"): [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
        t("cat_music"): [".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".wma"],
        t("cat_videos"): [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
        t("cat_programs"): [".exe", ".msi", ".bat", ".sh"],
        t("cat_images_disk"): [".iso", ".img", ".bin"],
        t("cat_virtualization"): [".vhd", ".vhdx", ".vmdk", ".qcow2", ".vdi", ".raw", ".ova", ".ovf"],
    }


def get_media_categories() -> List[str]:
    """Получить список медиа-категорий для сортировки по дате."""
    return [t("cat_images"), t("cat_videos")]


def set_language(lang: str) -> None:
    """Установить текущий язык приложения."""
    global CURRENT_LANG
    if lang in TRANSLATIONS:
        CURRENT_LANG = lang
        print(f"Language changed to: {lang}")  # Для отладки
    else:
        print(f"Language '{lang}' not found! Available: {list(TRANSLATIONS.keys())}")