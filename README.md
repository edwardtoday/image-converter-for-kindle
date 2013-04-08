image-converter-for-kindle
==========================

Convert JPEG images to kindle screensaver size

The script will look for images in specified directory, do the following processing steps and save the results to 'ss' subdirectory.

1. Rotate landscape images to portrait.
2. Resize/crop to fit 600*800 resolution.
3. Convert to grayscale.


Usage
-----
```bash
python convert2kindless.py ./sample
```

Generates `./sample/ss/sample.jpg`.
