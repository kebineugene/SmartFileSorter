import os
import shutil
from pathlib import Path


def organize_folder(folder_path, progress_callback=None):
    target_dir = Path(folder_path)

    if not target_dir.exists():
        raise ValueError("Указанная папка не существует!")

    FILE_TYPES = {
        "Изображения": [
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".svg",
            ".webp",
        ],
        "Документы": [
            ".pdf",
            ".docx",
            ".doc",
            ".txt",
            ".xlsx",
            ".xls",
            ".pptx",
            ".csv",
        ],
        "Архивы": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Музыка": [".mp3", ".wav", ".flac", ".ogg", ".m4a"],
        "Видео": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Программы": [".exe", ".msi"],
        "Образы": [".iso", ".img"],
        "Виртуализация": [
            ".vhd",
            ".vhdx",
            ".vmdk",
            ".qcow2",
            ".vdi",
            ".raw",
            ".img",
            ".ova",
            ".ovf",
        ],
    }

    # 1. Сначала просто считаем, сколько всего файлов нужно обработать
    all_files = [item for item in target_dir.iterdir() if item.is_file()]
    total_files = len(all_files)

    moved_count = 0

    # 2. Перебираем файлы и двигаем прогресс
    for item in all_files:
        file_ext = item.suffix.lower()

        found_category = None
        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                found_category = category
                break

        if not found_category:
            found_category = "Разное"

        category_dir = target_dir / found_category
        category_dir.mkdir(exist_ok=True)

        shutil.move(str(item), str(category_dir / item.name))
        moved_count += 1

        # Если нам передали функцию для обновления прогресса — вызываем её
        if progress_callback and total_files > 0:
            # Вычисляем долю выполненного от 0.0 до 1.0
            current_progress = moved_count / total_files
            progress_callback(current_progress)

    return moved_count
