from PIL import Image
import os

def convert_to_webp(input_file, output_file, quality=85):
    
    img = Image.open(input_file)
    
    img.save(output_file, 'WEBP', quality=quality)
    
    os.remove(input_file)
    print(f"Converted {os.path.basename(input_file)} to {os.path.basename(output_file)} and deleted original.")

if __name__ == "__main__":
    folder = os.getcwd() 

    
    for filename in os.listdir(folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):  
            input_file = os.path.join(folder, filename)
            output_file = os.path.join(folder, f"{os.path.splitext(filename)[0]}.webp")
            convert_to_webp(input_file, output_file)
