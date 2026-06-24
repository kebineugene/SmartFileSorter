import os
import webbrowser  # Модуль для открытия ссылок в браузере
from tkinter import filedialog, messagebox  # Модуль для всплывающих окон
import customtkinter as ctk

# Импортируем нашу функцию сортировки из файла organizer.py
from organizer import organize_folder

# Инициализируем настройки интерфейса
ctk.set_appearance_mode("System")  # Подстраивается под темную/светлую тему Windows
ctk.set_default_color_theme("green")  # Основной цвет кнопок — зеленый

# Создаем главное окно
app = ctk.CTk()
app.title("SmartFileSorter v2.6")
app.geometry("500x470")  # Высота идеально подогнана под все элементы
app.resizable(False, False)  # Запрещаем изменять размер окна


def open_github():
    """Функция открывает главную страницу GitHub"""
    webbrowser.open("https://github.com/kebineugene/SmartFileSorter")


def get_folder_size(folder_path):
    """Считает размер всех файлов в папке и красиво форматирует результат (Б, КБ, МБ, ГБ)"""
    total_size = 0
    try:
        for item in os.scandir(folder_path):
            if item.is_file():
                total_size += item.stat().st_size

        # Переводим байты в читаемый человеком вид
        for unit in ["Б", "КБ", "МБ", "ГБ"]:
            if total_size < 1024.0:
                return f"{total_size:.1f} {unit}"
            total_size /= 1024.0
        return f"{total_size:.1f} ГБ"
    except Exception:
        return "Размер неизвестен"


def update_progress(value):
    """Вызывается из organizer.py при переносе каждого файла"""
    progress_bar.set(value)  # Устанавливаем значение полосы (от 0.0 до 1.0)
    app.update_idletasks()  # Принудительно перерисовываем окно


def select_folder():
    """Открывает стандартное окно Windows для выбора папки"""
    initial_dir = os.path.expanduser("~")
    selected_dir = filedialog.askdirectory(initialdir=initial_dir)

    if selected_dir:
        path_input.delete(0, ctk.END)
        path_input.insert(0, selected_dir)

        # Вычисляем размер выбранной папки
        folder_size = get_folder_size(selected_dir)

        # Выводим информацию о весе папки пользователю
        status_label.configure(
            text=f"Папка выбрана. Общий вес файлов: {folder_size}\nНажмите 'Начать уборку'",
            text_color="gray",
        )
        progress_bar.set(0)  # Сбрасываем прогресс-бар


def start_cleaning():
    """Запускает процесс сортировки файлов с предварительным подтверждением"""
    folder_path = path_input.get().strip()

    if not folder_path:
        status_label.configure(
            text="❌ Ошибка: Сначала выберите папку!", text_color="red"
        )
        return

    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        status_label.configure(
            text="❌ Ошибка: Указанный путь не существует!", text_color="red"
        )
        return

    # Интерактивный дисклеймер-предупреждение
    user_agreement = messagebox.askyesno(
        title="⚠️ Официальный дисклеймер!",
        message="Внимание!\n\nПосле уборки все файлы разлетятся по новым папкам.\n"
        "If you are cleaning up Telegram downloads, it will lose old files from chats.\n\n"
        "Пожалуйста, хорошенько подумайте, иначе разгневанные пользователи вас порвут, "
        "когда не найдут свои файлы на привычных местах! 😂\n\n"
        "Вы берете на себя эту ответственность и готовы продолжить?",
    )

    # Если пользователь передумал
    if not user_agreement:
        status_label.configure(
            text="⏸ Уборка отменена от греха подальше.", text_color="yellow"
        )
        messagebox.showinfo(
            title="Вы спаслись!",
            message="Умный выбор. Разработчик вздохнул с облегчением, файлы остались нетронутыми! 🙌",
        )
        return

    try:
        status_label.configure(text="⏳ Сортировка файлов...", text_color="cyan")
        progress_bar.set(0)
        app.update_idletasks()

        # Замеряем размер ДО уборки для финального сообщения
        final_size = get_folder_size(folder_path)

        # Запуск бэкенд-логики перемещения файлов
        count = organize_folder(folder_path, progress_callback=update_progress)

        # Выводим успешный результат с указанием веса и количества файлов
        status_label.configure(
            text=f"✔ Успех! Разобрано файлов: {count} ({final_size})",
            text_color="lightgreen",
        )

    except Exception as e:
        status_label.configure(text=f"❌ Произошла ошибка: {e}", text_color="red")


# === СТРОИМ ИНТЕРФЕЙС (ВИДЖЕТЫ) ===

# Главный заголовок
title_label = ctk.CTkLabel(
    app, text="📂 SmartFileSorter", font=ctk.CTkFont(size=24, weight="bold")
)
title_label.pack(pady=20)

subtitle_label = ctk.CTkLabel(
    app,
    text="Выберите замусоренную папку для автоматического наведения порядка",
    font=ctk.CTkFont(size=12),
    text_color="gray",
)
subtitle_label.pack(pady=5)

# Фрейм-контейнер для строки ввода и кнопки "Обзор"
input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=20, padx=20, fill="x")

# Поле ввода пути
path_input = ctk.CTkEntry(input_frame, placeholder_text="Путь к папке...", width=320)
path_input.pack(side="left", padx=(10, 5))

# Кнопка "Обзор"
browse_button = ctk.CTkButton(
    input_frame, text="Обзор...", width=80, command=select_folder
)
browse_button.pack(side="left", padx=(5, 10))

# Главная кнопка запуска
clean_button = ctk.CTkButton(
    app,
    text="🚀 Начать уборку",
    font=ctk.CTkFont(size=16, weight="bold"),
    width=200,
    height=40,
    command=start_cleaning,
)
clean_button.pack(pady=10)

# Элемент Прогресс-бар
progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.pack(pady=15)
progress_bar.set(0)

# Текст текущего статуса программы
status_label = ctk.CTkLabel(
    app,
    text="Ожидание выбора папки...",
    font=ctk.CTkFont(size=13),
    justify="center",
)
status_label.pack(pady=10)

# Заметное предупреждение о сетевых каталогах с правильными отступами
warning_label = ctk.CTkLabel(
    app,
    text="⚠️ Внимание: Не используйте программу для сортировки сетевых папок!\nЭто может замедлить работу сети или привести к ошибкам перемещения.",
    font=ctk.CTkFont(size=11, weight="bold"),
    text_color=("#D97706", "#FBBF24"),
    justify="center",
)
warning_label.pack(pady=15, padx=15)

# Кликабельная ссылка на GitHub
github_link = ctk.CTkLabel(
    app,
    text="🐱 Проект на GitHub",
    font=ctk.CTkFont(size=12, underline=True, weight="bold"),
    text_color=("#1F6AA5", "#1F8EF1"),
    cursor="hand2",
)
github_link.pack(pady=(0, 15))

# Привязываем событие клика мышки к нашей функции open_github
github_link.bind("<Button-1>", lambda event: open_github())

# Запуск главного цикла приложения
app.mainloop()
