import os
import threading
import webbrowser
from tkinter import filedialog, messagebox
from typing import Callable, Optional
import customtkinter as ctk

try:
    from tkinterdnd2 import TkinterDnD, DND_FILES
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False

import i18n
from i18n import t, set_language
from organizer import organize_folder


class SmartSorterApp(ctk.CTk):
    """Основное приложение SmartFileSorter с поддержкой локализации."""

    def __init__(self) -> None:
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green")

        self.title(t("title"))
        self.geometry("550x720")
        self.resizable(True, False)

        try:
            if os.path.exists("icon.ico"):
                self.iconbitmap("icon.ico")
        except Exception:
            pass

        self.dry_run_var: ctk.BooleanVar = ctk.BooleanVar(value=False)
        self.sort_by_date_var: ctk.BooleanVar = ctk.BooleanVar(value=True)
        self.open_after_var: ctk.BooleanVar = ctk.BooleanVar(value=False)

        self._setup_ui()

        if DND_AVAILABLE:
            self._setup_drag_and_drop()

    def _setup_ui(self) -> None:
        """Создает все элементы интерфейса."""
        # Заголовок
        self.title_label = ctk.CTkLabel(
            self, text=t("title"),
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.title_label.pack(pady=(20, 10))

        # Подзаголовок
        self.subtitle_label = ctk.CTkLabel(
            self, text=t("subtitle"),
            font=ctk.CTkFont(size=13), text_color="gray"
        )
        self.subtitle_label.pack(pady=(0, 20))

        # ===== Переключатель языка =====
        self.lang_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.lang_frame.pack(pady=(0, 10))

        self.lang_label = ctk.CTkLabel(
            self.lang_frame, text=t("language_label"),
            font=ctk.CTkFont(size=13)
        )
        self.lang_label.pack(side="left", padx=(0, 10))

        # Создаем переключатель БЕЗ привязки к переменной
        self.lang_switch = ctk.CTkSegmentedButton(
            self.lang_frame,
            values=[t("language_ru"), t("language_en")],
            command=self._on_language_change,  # Без variable!
            font=ctk.CTkFont(size=12)
        )
        self.lang_switch.pack(side="left")
        
        # Устанавливаем текущий язык визуально
        current_lang_text = t("language_ru") if i18n.CURRENT_LANG == "ru" else t("language_en")
        self.lang_switch.set(current_lang_text)

        # Поле ввода пути
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=(0, 20), padx=30, fill="x")

        self.path_input = ctk.CTkEntry(
            self.input_frame, placeholder_text=t("path_placeholder"),
            width=350, font=ctk.CTkFont(size=12)
        )
        self.path_input.pack(side="left", padx=(0, 10), fill="x", expand=True)

        self.browse_button = ctk.CTkButton(
            self.input_frame, text=t("browse_button"),
            width=100, command=self.select_folder
        )
        self.browse_button.pack(side="left")

        # Чекбоксы
        self.dry_run_checkbox = ctk.CTkCheckBox(
            self, text=t("dry_run_checkbox"),
            variable=self.dry_run_var, font=ctk.CTkFont(size=13),
            hover_color=("gray70", "gray30")
        )
        self.dry_run_checkbox.pack(pady=(10, 5), padx=30, anchor="w")

        self.date_checkbox = ctk.CTkCheckBox(
            self, text=t("sort_by_date_checkbox"),
            variable=self.sort_by_date_var, font=ctk.CTkFont(size=13),
            hover_color=("gray70", "gray30")
        )
        self.date_checkbox.pack(pady=(5, 5), padx=30, anchor="w")

        self.open_after_checkbox = ctk.CTkCheckBox(
            self, text=t("open_after_checkbox"),
            variable=self.open_after_var, font=ctk.CTkFont(size=13),
            hover_color=("gray70", "gray30")
        )
        self.open_after_checkbox.pack(pady=(5, 15), padx=30, anchor="w")

        # Кнопки
        self.clean_button = ctk.CTkButton(
            self, text=t("clean_button"),
            font=ctk.CTkFont(size=18, weight="bold"),
            width=250, height=45, command=self.start_cleaning
        )
        self.clean_button.pack(pady=10)

        self.open_folder_button = ctk.CTkButton(
            self, text=t("open_folder_button"),
            width=150, height=35, command=self.open_folder,
            fg_color="gray", hover_color="gray40"
        )
        self.open_folder_button.pack(pady=5)

        # Прогресс и статус
        self.progress_bar = ctk.CTkProgressBar(self, width=450, height=20)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(
            self, text=t("status_waiting"),
            font=ctk.CTkFont(size=14), justify="center", wraplength=500
        )
        self.status_label.pack(pady=10)

        self.warning_label = ctk.CTkLabel(
            self, text=t("warning_text"),
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=("#D97706", "#FBBF24"), justify="center"
        )
        self.warning_label.pack(pady=15, padx=30)

        self.github_link = ctk.CTkLabel(
            self, text=t("github_link"),
            font=ctk.CTkFont(size=12, underline=True, weight="bold"),
            text_color=("#1F6AA5", "#1F8EF1"), cursor="hand2"
        )
        self.github_link.pack(pady=(0, 10))
        self.github_link.bind("<Button-1>", lambda e: self.open_github())

        if DND_AVAILABLE:
            self.dnd_label = ctk.CTkLabel(
                self, text=t("dnd_tip"),
                font=ctk.CTkFont(size=11), text_color="gray"
            )
            self.dnd_label.pack(pady=(0, 10))

    def _on_language_change(self, value: str) -> None:
        """Обрабатывает смену языка."""
        print(f"Language change triggered with value: '{value}'")
        print(f"Current lang before: {i18n.CURRENT_LANG}")

        # Определяем язык по тексту
        if "Русск" in value:
            new_lang = "ru"
        elif "English" in value:
            new_lang = "en"
        else:
            # Fallback
            new_lang = "en" if i18n.CURRENT_LANG == "ru" else "ru"

        print(f"Setting language to: {new_lang}")
        set_language(new_lang)
        print(f"Current lang after: {i18n.CURRENT_LANG}")

        # Пересоздаем UI с новым языком
        self._rebuild_ui()

    def _rebuild_ui(self) -> None:
        """Пересоздаёт весь интерфейс с текущим языком."""
        print(f"Rebuilding UI for language: {i18n.CURRENT_LANG}")

        # Сохраняем путь из поля ввода
        saved_path = self.path_input.get().strip() if hasattr(self, 'path_input') else ""

        # Удаляем все виджеты
        for widget in self.winfo_children():
            widget.destroy()

        # Обновляем заголовок окна
        self.title(t("title"))

        # Пересоздаём интерфейс
        self._setup_ui()

        # Восстанавливаем Drag & Drop
        if DND_AVAILABLE:
            self._setup_drag_and_drop()

        # Восстанавливаем путь
        if saved_path:
            self.path_input.delete(0, ctk.END)
            self.path_input.insert(0, saved_path)
            self._update_folder_info(saved_path)

    def _setup_drag_and_drop(self) -> None:
        """Настраивает поддержку Drag & Drop."""
        try:
            self.path_input.drop_target_register(DND_FILES)
            self.path_input.dnd_bind('<<Drop>>', self._on_drop)
        except Exception as e:
            print(f"Drag & Drop error: {e}")

    def _on_drop(self, event) -> str:
        """Обрабатывает событие перетаскивания папки."""
        try:
            path = event.data.strip('{}')
            if os.path.isdir(path):
                self.path_input.delete(0, ctk.END)
                self.path_input.insert(0, path)
                self._update_folder_info(path)
        except Exception as e:
            print(f"Drop error: {e}")
        return "break"

    def open_github(self) -> None:
        """Открывает репозиторий GitHub."""
        webbrowser.open("https://github.com/kebineugene/SmartFileSorter")

    def open_folder(self) -> None:
        """Открывает выбранную папку."""
        folder_path = self.path_input.get().strip()
        if folder_path and os.path.exists(folder_path):
            try:
                os.startfile(folder_path)
            except Exception:
                os.system(f'explorer "{folder_path}"')
        else:
            self.status_label.configure(text=t("status_error_open_folder"), text_color="red")

    def get_folder_size(self, folder_path: str) -> str:
        """Вычисляет общий размер файлов."""
        total_size = 0
        try:
            for item in os.scandir(folder_path):
                if item.is_file():
                    total_size += item.stat().st_size
            for unit in ["B", "KB", "MB", "GB"]:
                if total_size < 1024.0:
                    return f"{total_size:.1f} {unit}"
                total_size /= 1024.0
            return f"{total_size:.1f} GB"
        except Exception:
            return t("error_unknown_size")

    def _update_folder_info(self, folder_path: str) -> None:
        """Обновляет информацию о папке."""
        folder_size = self.get_folder_size(folder_path)
        self.status_label.configure(
            text=t("status_folder_selected", folder_size),
            text_color="gray"
        )
        self.progress_bar.set(0)

    def select_folder(self) -> None:
        """Открывает диалог выбора папки."""
        initial_dir = os.path.expanduser("~")
        selected_dir = filedialog.askdirectory(initialdir=initial_dir)
        if selected_dir:
            self.path_input.delete(0, ctk.END)
            self.path_input.insert(0, selected_dir)
            self._update_folder_info(selected_dir)

    def update_progress(self, value: float) -> None:
        """Обновляет прогресс-бар."""
        self.after(0, lambda: self.progress_bar.set(value))

    def on_task_success(self, count: int, final_size: str, is_dry_run: bool) -> None:
        """Обрабатывает успешное завершение."""
        self.clean_button.configure(state="normal", text=t("clean_button"))

        if is_dry_run:
            self.status_label.configure(
                text=t("status_success_dry_run", count, t("log_filename_dry")),
                text_color="cyan"
            )
        else:
            msg = t("status_success", count, final_size, t("log_filename"))
            folder_path = self.path_input.get().strip()
            if os.path.exists(os.path.join(folder_path, "undo_sort.bat")):
                msg += t("status_success_undo")
            self.status_label.configure(text=msg, text_color="lightgreen")
            if self.open_after_var.get():
                self.open_folder()

        self.progress_bar.set(1.0)

    def on_task_error(self, error_msg: str) -> None:
        """Обрабатывает ошибку."""
        self.clean_button.configure(state="normal", text=t("clean_button"))
        self.status_label.configure(text=t("status_error", error_msg), text_color="red")

    def run_organizer_task(self, folder_path: str, is_dry_run: bool, sort_by_date: bool) -> None:
        """Фоновая задача сортировки."""
        try:
            count = organize_folder(
                folder_path=folder_path,
                progress_callback=self.update_progress,
                dry_run=is_dry_run,
                sort_by_date=sort_by_date,
                lang=i18n.CURRENT_LANG
            )
            final_size = self.get_folder_size(folder_path)
            self.after(0, lambda: self.on_task_success(count, final_size, is_dry_run))
        except Exception as e:
            self.after(0, lambda: self.on_task_error(str(e)))

    def start_cleaning(self) -> None:
        """Запускает процесс сортировки."""
        folder_path = self.path_input.get().strip()

        if not folder_path:
            self.status_label.configure(text=t("status_error_no_folder"), text_color="red")
            return

        if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
            self.status_label.configure(text=t("status_error_path"), text_color="red")
            return

        is_dry_run = self.dry_run_var.get()
        sort_by_date = self.sort_by_date_var.get()

        if not is_dry_run:
            user_agreement = messagebox.askyesno(
                title=t("confirm_title"),
                message=t("confirm_message"),
            )
            if not user_agreement:
                self.status_label.configure(text=t("status_cancelled"), text_color="yellow")
                return

        btn_text = t("analyzing_button") if is_dry_run else t("cleaning_button")
        self.clean_button.configure(state="disabled", text=btn_text)

        mode_text = t("status_analyzing_text") if is_dry_run else t("status_cleaning_text")
        self.status_label.configure(text=t("status_cleaning", mode_text), text_color="cyan")
        self.progress_bar.set(0)

        thread = threading.Thread(
            target=self.run_organizer_task,
            args=(folder_path, is_dry_run, sort_by_date),
            daemon=True
        )
        thread.start()


if __name__ == "__main__":
    app = SmartSorterApp()
    app.mainloop()