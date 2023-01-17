"""
Take a zip file containing HEIC images and
(1) Convert each heic image to monochrome png image
(2) Combine all png images into a single pdf file
"""
import subprocess
import sys
from pathlib import Path

zip_file = Path(sys.argv[1])

# Unzip into folder with same name
output_folder = zip_file.with_name(zip_file.stem)
if not output_folder.exists():
  cmd = ['unzip', '-d', output_folder, zip_file]
  subprocess.run(cmd)

# Convert HEIC files to png
for image_file in output_folder.glob('*.HEIC'):
  png_file = image_file.with_suffix('.png')
  cmd = ['convert', image_file, '-monochrome', png_file]
  subprocess.run(cmd)

# Append all png files into a single pdf file
png_files = list(sorted(output_folder.glob('*.png')))
cmd = ['convert'] + png_files + [ output_folder / 'output.pdf']
subprocess.run(cmd)
