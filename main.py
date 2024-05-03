import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# List of common image file extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Function to delete files with specified extensions
def delete_files(dir_path, extensions):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file_path)[1].lower()
            if file_ext in extensions:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

class PhotoDeleterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        delete_button = Button(text='Delete Photos', on_press=self.delete_photos)
        layout.add_widget(delete_button)
        return layout

    def delete_photos(self, instance):
        directory = 'E://New folder'
        delete_files(directory, image_extensions)

if __name__ == '__main__':
    PhotoDeleterApp().run()