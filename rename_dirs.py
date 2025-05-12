import os
import re

def rename_directories(base_path):
    """
    Rename directories under the Java path to use 4-digit zero-padded problem numbers.
    
    For example: "123 Problem Name" -> "0123 Problem Name"
    """
    java_path = os.path.join(base_path, "java")
    
    if not os.path.exists(java_path):
        print(f"Java directory not found at {java_path}")
        return
    
    # List all directories under the Java path
    dirs = [d for d in os.listdir(java_path) if os.path.isdir(os.path.join(java_path, d))]
    
    # Regular expression to match directory names with numbers
    pattern = re.compile(r'^(\d+)(.*)$')
    
    renamed_count = 0
    for dir_name in dirs:
        match = pattern.match(dir_name)
        if match:
            # Extract the number and remainder of the directory name
            number = match.group(1)
            remainder = match.group(2)
            
            # Create new directory name with 4-digit zero-padded number
            new_dir_name = f"{int(number):04d}{remainder}"
            
            if dir_name != new_dir_name:
                old_path = os.path.join(java_path, dir_name)
                new_path = os.path.join(java_path, new_dir_name)
                
                # Rename the directory
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed: {dir_name} -> {new_dir_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"Error renaming {dir_name}: {e}")
    
    print(f"\nCompleted renaming {renamed_count} directories.")

if __name__ == "__main__":
    base_path = r"d:\Code\neet-code-150-python"
    rename_directories(base_path)
