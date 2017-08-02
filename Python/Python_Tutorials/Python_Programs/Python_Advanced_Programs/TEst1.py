import os
root = '/Users/santosh/pyprojects'
def all_files_under(path):
    """Iterates through all files that are under the given path."""
    for cur_path, dirnames, filenames in os.walk(path):
        for filename in filenames:
            print('Yes')
            if not filename.startswith('.'):
                yield os.path.join(cur_path, filename)

latest_file = max(all_files_under(root), key=os.path.getmtime)
print(latest_file)