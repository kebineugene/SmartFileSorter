import os
import shutil
import datetime
from pathlib import Path
from typing import Callable, Optional, List

from i18n import t, get_months, get_categories, get_media_categories


def safe_move(src_path: Path, dst_dir: Path, dry_run: bool = False) -> Path:
    """Безопасно перемещает файл."""
    dst_path = dst_dir / src_path.name
    
    if dst_path.exists():
        name = src_path.stem
        ext = src_path.suffix
        counter = 1
        while dst_path.exists():
            dst_path = dst_dir / f"{name}_{counter}{ext}"
            counter += 1
    
    if not dry_run:
        try:
            shutil.move(str(src_path), str(dst_path))
        except PermissionError as e:
            raise PermissionError(t("error_file_busy", src_path.name)) from e
        except Exception as e:
            raise Exception(t("error_move_failed", src_path.name, e)) from e
    
    return dst_path


def organize_folder(
    folder_path: str,
    progress_callback: Optional[Callable[[float], None]] = None,
    dry_run: bool = False,
    sort_by_date: bool = False,
    lang: str = "ru"
) -> int:
    """Сортирует файлы в папке."""
    from i18n import set_language, CURRENT_LANG
    if lang != CURRENT_LANG:
        set_language(lang)
    
    target_dir = Path(folder_path)
    
    if not target_dir.exists():
        raise ValueError(t("error_folder_not_exists", folder_path))
    if not target_dir.is_dir():
        raise ValueError(t("error_not_folder", folder_path))
    
    FILE_TYPES = get_categories()
    MEDIA_CATEGORIES = get_media_categories()
    MONTHS = get_months()
    
    all_files: List[Path] = [
        item for item in target_dir.iterdir()
        if item.is_file() and not item.name.startswith('.')
        and item.name not in ['desktop.ini', 'Thumbs.db']
    ]
    
    total_files: int = len(all_files)
    moved_count: int = 0
    log_entries: List[str] = []
    error_entries: List[str] = []
    
    for item in all_files:
        file_ext: str = item.suffix.lower()
        found_category: Optional[str] = None
        
        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                found_category = category
                break
        
        if not found_category:
            found_category = t("cat_other")
        
        category_dir = target_dir / found_category
        
        if sort_by_date and found_category in MEDIA_CATEGORIES:
            try:
                mtime = item.stat().st_mtime
                dt = datetime.datetime.fromtimestamp(mtime)
                month_name = MONTHS[dt.month - 1]
                date_subfolder = f"{dt.year}/{dt.month:02d}_{month_name}"
                category_dir = category_dir / date_subfolder
            except Exception:
                pass
        
        if not dry_run:
            try:
                category_dir.mkdir(parents=True, exist_ok=True)
            except PermissionError:
                error_entries.append(f"{item.name} -> {t('error_permission_create')}")
                continue
        
        try:
            final_path = safe_move(item, category_dir, dry_run=dry_run)
            rel_path = final_path.relative_to(target_dir)
            log_entries.append(f"{item.name} -> {rel_path.as_posix()}")
            moved_count += 1
        except PermissionError:
            error_entries.append(f"{item.name} -> {t('error_busy_short')}")
        except Exception as e:
            error_entries.append(f"{item.name} -> {str(e)}")
        
        if progress_callback and total_files > 0:
            current_progress = moved_count / total_files
            progress_callback(current_progress)
    
    _save_reports(target_dir, log_entries, error_entries, moved_count, dry_run)
    return moved_count


def _save_reports(target_dir: Path, log_entries: List[str], error_entries: List[str], 
                  moved_count: int, dry_run: bool) -> None:
    """Сохраняет логи."""
    if not log_entries and not error_entries:
        return
    
    log_name = t("log_filename_dry") if dry_run else t("log_filename")
    log_path = target_dir / log_name
    
    try:
        with open(log_path, "w", encoding="utf-8") as f:
            header = "ТЕСТОВЫЙ ПРОГОН (ФАЙЛЫ НЕ ПЕРЕМЕЩАЛИСЬ)" if dry_run else "SORTING REPORT"
            f.write(f"{header}\n")
            f.write(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total files: {moved_count}\n")
            f.write("=" * 60 + "\n\n")
            
            if log_entries:
                f.write("Successfully moved:\n")
                f.write("-" * 60 + "\n")
                for entry in log_entries:
                    f.write(entry + "\n")
                f.write("\n")
            
            if error_entries:
                f.write("Errors/skipped:\n")
                f.write("-" * 60 + "\n")
                for entry in error_entries:
                    f.write(entry + "\n")
        
        if not dry_run and log_entries:
            _create_undo_script(target_dir, log_entries)
    except Exception as e:
        print(f"Error saving log: {e}")


def _create_undo_script(target_dir: Path, log_entries: List[str]) -> None:
    """Создаёт BAT-скрипт отката."""
    bat_path = target_dir / "undo_sort.bat"
    
    try:
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write("@echo off\n")
            f.write("chcp 65001 >nul\n")
            f.write("echo ================================================\n")
            f.write(f"echo   SmartFileSorter: Restoring files...\n")
            f.write("echo ================================================\n\n")
            f.write('cd /d "%~dp0"\n\n')
            
            for entry in log_entries:
                parts = entry.split(" -> ")
                if len(parts) == 2:
                    orig_name = parts[0]
                    rel_path_win = parts[1].replace("/", "\\")
                    f.write(f'move "{rel_path_win}" "{orig_name}"\n')
            
            f.write("\necho ================================================\n")
            f.write("echo   Done! Files restored.\n")
            f.write("echo ================================================\n")
            f.write("echo.\n")
            f.write("pause\n")
    except Exception as e:
        print(f"Error creating undo script: {e}")