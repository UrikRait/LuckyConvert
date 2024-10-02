from PIL import Image
import os

def convert_to_webp(input_file, output_file, quality=85):
    # Открываем изображение
    img = Image.open(input_file)
    
    # Конвертируем изображение в WebP и сохраняем его
    img.save(output_file, 'WEBP', quality=quality)
    
    # Удаляем оригинальный файл
    os.remove(input_file)
    print(f"Converted {os.path.basename(input_file)} to {os.path.basename(output_file)} and deleted original.")

if __name__ == "__main__":
    folder = os.getcwd()  # Текущая папка, где лежит скрипт

    # Проходим по каждому файлу в папке
    for filename in os.listdir(folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  # Проверка форматов
            input_file = os.path.join(folder, filename)
            output_file = os.path.join(folder, f"{os.path.splitext(filename)[0]}.webp")
            convert_to_webp(input_file, output_file)