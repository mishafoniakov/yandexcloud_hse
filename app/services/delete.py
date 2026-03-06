import os

class DeleteAllCache:
    def __init__(self):
        self.cache_path = './uploads'

    def delete_all_cache(self):
        cache_list = os.listdir(self.cache_path)
        if len(cache_list) == 0:
            return "No cache to delete"
        else:
            cache_list = os.listdir(self.cache_path)
            for file in cache_list:
                os.remove(os.path.join(self.cache_path, file))
            return "All cache is deleted"
    
    def delete_all_pycache(self):
        current_directory = '.'
        folders_list = [item for item in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, item))]
        for folder in folders_list:
            if folder == '__pycache__':
                for item in os.listdir(os.path.join(current_directory, folder)):
                    os.remove(os.path.join(current_directory, folder, item))
            else:
                folders_list = [item for item in os.listdir(os.path.join(current_directory, folder)) if os.path.isdir(os.path.join(current_directory, folder, item))]
                for subfolder in folders_list:
                    if subfolder == '__pycache__':
                        for item in os.listdir(os.path.join(current_directory, folder, subfolder)):
                            os.remove(os.path.join(current_directory, folder, subfolder, item))
    
    def __call__(self):
        self.delete_all_cache()
        self.delete_all_pycache()