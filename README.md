# HEIC 2 JPG Converter

## Description

A quick simple application to convert HEIC files to JPG format. Drag and drop HEIC files onto the application icon or window to convert them.

## Usage

1. Download the ZIP file from the `dist/` directory.
2. Extract the ZIP file.
3. Run the executable.
4. Drag and drop HEIC files onto the application window. The files will be automatically converted to JPG format.

## Developer Notes

Install dependencies:

```
pip install -r requirements.txt
```

Create the executable with PyInstaller using something like:

```
pyinstaller -F -w src/heic2jpg.py --icon=assets/heic2jpg_icon2.ico --additional-hooks-dir=.
```


## Support

Any issues please contact <danpoynor@gmail.com>.