
import os

def write_project_structure(root_dir, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(root_dir):
            level = root.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            file.write(f'{indent}{os.path.basename(root)}/\n')
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                file.write(f'{sub_indent}{f}\n')

write_project_structure('C:/1', 'project_structure.txt')
