# 📂 SmartFileSorter v5.0

**[🇷 Русский](#-русский)** | **[🇬🇧 English](#-english)**

**Умный сортировщик файлов с безопасным откатом и двуязычным интерфейсом**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![Version](https://img.shields.io/badge/version-5.0-orange.svg)

---

# 🇷🇺 Русский

##  Что нового в v5.0

- 🛡️ **Скрипт отката** — добавлен `undo_sort.bat` для возврата всех файлов на места одним кликом
- 👁️ **Тестовый режим (Dry Run)** — анализируйте файлы без реального перемещения
- 📅 **Сортировка по дате** — фото и видео автоматически раскладываются по папкам Год/Месяц
-  **Многопоточность** — интерфейс остаётся отзывчивым во время сортировки
-  **Логирование** — подробный отчёт о всех операциях в `sort_log.txt`
- 🔒 **Обработка занятых файлов** — корректная обработка файлов, заблокированных другими программами
- 🖱️ **Drag & Drop** — перетаскивайте папки прямо в окно приложения

## ✅ Исправлено

- 🐛 Исправлено зависание интерфейса при сортировке больших папок
-  Исправлена обработка дубликатов файлов (автоматическое переименование)
- 🐛 Убраны лишние пробелы в расширениях файлов

## ✨ Возможности

- 🎯 **Умная категоризация** — автоматическое определение типа файла
-  **Сортировка по дате** — структура Год/Месяц для фото и видео
- ️ **Тестовый режим** — предпросмотр без реальных изменений
- ️ **Безопасный откат** — BAT-скрипт для возврата файлов
-  **Подробные логи** — отчёт о всех перемещениях и ошибках
- 🎨 **Современный UI** — CustomTkinter с тёмной/светлой темой
- ️ **Drag & Drop** — перетаскивание папок в окно
- ⚡ **Многопоточность** — интерфейс не зависает
- 🔄 **Обработка дубликатов** — автоматическое переименование
-  **Подсчёт размера** — показывает размер папки до сортировки
- 🌐 **Двуязычный интерфейс** — 🇷🇺 Русский / 🇬🇧 English

##  Установка

### Быстрый старт
Скачайте готовый `SmartFileSorter.exe` из раздела **Releases** — установка Python не требуется!

### Из исходного кода

```bash
git clone https://github.com/kebineugene/SmartFileSorter.git
cd SmartFileSorter
pip install -r requirements.txt
python main.py
```

**requirements.txt:**
```txt
customtkinter>=5.2.0
tkinterdnd2>=0.3.0
```

## 📖 Использование

1. **Запустите приложение**
2. **Выберите язык** — переключатель 🇺/🇬 вверху окна
3. **Выберите папку** — кнопка «Обзор» или Drag & Drop
4. **Настройте параметры:**
   - ☑️ Тестовый режим — сначала проверьте, что будет сделано
   - ☑️ Сортировка по дате — для фото и видео
   - ☑️ Открыть папку после завершения
5. **Нажмите «🚀 Начать уборку»**
6. **Подтвердите операцию**
7. **Проверьте результаты** — откройте `sort_log.txt`

### Откат изменений
1. Откройте отсортированную папку
2. Запустите `undo_sort.bat` двойным кликом
3. Все файлы вернутся на места

## 📁 Структура проекта

```
SmartFileSorter/
├── main.py              # GUI приложения
├── organizer.py         # Логика сортировки
├── i18n.py              # Модуль локализации (RU/EN)
├── icon.ico             # Иконка приложения
├── SmartFileSorter.exe  # Готовое приложение
── README.md            # Документация
```

## 📬 Контакты

**Автор:** kebineugene  
**GitHub:** [@kebineugene](https://github.com/kebineugene)  
**Проект:** [SmartFileSorter](https://github.com/kebineugene/SmartFileSorter)

---

# 🇬🇧 English

## 🎉 What's New in v5.0

- 🛡️ **Undo script** — added `undo_sort.bat` to restore all files with one click
- 👁️ **Dry Run mode** — analyze files without actually moving them
- 📅 **Date-based sorting** — photos and videos automatically organized into Year/Month folders
- ⚡ **Multithreading** — interface stays responsive during sorting
-  **Logging** — detailed report of all operations in `sort_log.txt`
- 🔒 **Busy file handling** — proper handling of files locked by other programs
- 🖱️ **Drag & Drop** — drop folders directly into the app window

## ✅ Fixed

- 🐛 Fixed interface freezing when sorting large folders
- 🐛 Fixed duplicate file handling (automatic renaming)
- 🐛 Removed extra spaces in file extensions

## ✨ Features

- 🎯 **Smart categorization** — automatic file type detection
- 📅 **Date-based sorting** — Year/Month structure for photos and videos
- ️ **Dry Run mode** — preview without real changes
- 🛡️ **Safe undo** — BAT script for file restoration
- 📊 **Detailed logs** — report of all moves and errors
- 🎨 **Modern UI** — CustomTkinter with dark/light theme
- 🖱️ **Drag & Drop** — drop folders into the window
- ⚡ **Multithreading** — interface never freezes
- 🔄 **Duplicate handling** — automatic renaming
- 📏 **Size calculation** — shows folder size before sorting
- 🌐 **Bilingual interface** — 🇷🇺 Русский / 🇬🇧 English

## 🚀 Installation

### Quick Start
Download the ready-to-use `SmartFileSorter.exe` from **Releases** — no Python installation needed!

### From source

```bash
git clone https://github.com/kebineugene/SmartFileSorter.git
cd SmartFileSorter
pip install -r requirements.txt
python main.py
```

**requirements.txt:**
```txt
customtkinter>=5.2.0
tkinterdnd2>=0.3.0
```

## 📖 Usage

1. **Launch the app**
2. **Select language** — 🇷🇺/🇬🇧 toggle at the top of the window
3. **Select a folder** — "Browse" button or Drag & Drop
4. **Configure options:**
   - ☑️ Dry Run — check what will be done first
   - ☑️ Sort by date — for photos and videos
   - ☑️ Open folder after completion
5. **Click "🚀 Start Sorting"**
6. **Confirm the operation**
7. **Check results** — open `sort_log.txt`

### Undoing Changes
1. Open the sorted folder
2. Double-click `undo_sort.bat`
3. All files will be restored to their original locations

## 📁 Project Structure

```
SmartFileSorter/
├── main.py              # Application GUI
├── organizer.py         # Sorting logic
├── i18n.py              # Localization module (RU/EN)
├── icon.ico             # App icon
├── SmartFileSorter.exe  # Ready-to-use application
└── README.md            # Documentation
```

## 📬 Contact

**Author:** kebineugene  
**GitHub:** [@kebineugene](https://github.com/kebineugene)  
**Project:** [SmartFileSorter](https://github.com/kebineugene/SmartFileSorter)

---

**⭐ Если проект был полезен / If you found this project useful, please give it a star on GitHub!**
