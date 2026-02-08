import shutil
import os

SOURCE_PATH = "mlartifacts/5/models/m-741c86c866d1420f878084332ee0b844/artifacts/model.pkl"

DEST_DIR = os.path.join(os.path.dirname(__file__))
DEST_FILE = os.path.join(DEST_DIR, "model.pkl")

def get_model():
    project_root = os.path.abspath(os.path.join(DEST_DIR, "../../"))
    full_source_path = os.path.join(project_root, SOURCE_PATH)

    print(f"Ищем модель здесь: {full_source_path}")

    if os.path.exists(full_source_path):
        print("Файл найден! Копируем...")
        shutil.copy2(full_source_path, DEST_FILE)
        print(f"Успех! Модель сохранена в: {DEST_FILE}")
    else:
        print("ОШИБКА: Файл не найден по этому пути.")
        print("Убедись, что запускаешь скрипт из корня проекта.")

if __name__ == "__main__":
    get_model()
