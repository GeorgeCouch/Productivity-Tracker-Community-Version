import PyInstaller.__main__
import os
import shutil

# Change this directory as needed
output_dir = r'c:\Users\georg\OneDrive\Documents\Personal Productivity Tracker Community Version exe'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Copy the icon4.ico file to the output directory
shutil.copy('icon4.ico', os.path.join(output_dir, 'icon4.ico'))

PyInstaller.__main__.run([
    'Productivity Tracker.py',
    '--onefile',
    '--windowed',
    '--hidden-import=plyer.platforms.win.notification',
    '--hidden-import=plyer.platforms.linux.notification',
    '--hidden-import=plyer.platforms.macosx.notification',
    '--add-data=icon4.ico;.',  # This line includes the icon in the bundle
    '--add-data=%s;.' % os.path.join(output_dir, 'icon4.ico'),  # This line includes the icon in the distpath
    '--icon=icon4.ico',
    '--distpath=%s' % output_dir,
    '--workpath=%s' % os.path.join(output_dir, 'build'),
])