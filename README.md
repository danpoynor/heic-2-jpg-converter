# HEIC 2 JPG Converter

## Description

A quick simple application to convert HEIC files to JPG format. Drag and drop HEIC files onto the application icon or window to convert them.

## Usage

1. Download the ZIP file from the `distro/` directory.
2. Extract the ZIP file and open the `heic2jpg`.
3. Double-click the `heic2jpg.exe` executable.
4. Drag and drop HEIC files onto the application window. The files will be automatically converted to JPG format.

## Developer Notes

Create a Virtual Environment

```
python -m venv env
```

Activate the Virtual Environment

```
source env/Scripts/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Verify Installation:

```
pip list
```

Create the executable with PyInstaller using something like:

```
pyinstaller -F -w src/heic2jpg.py --icon=assets/heic2jpg_icon2.ico --additional-hooks-dir=.
```

This will create a `heic2jpg.exe` binary executable file in the `dist/` directory.

If it seems like the build goes too quick, delete the `build` and `dist` directorise and the `.spec` file generated to avoid any cache-like behaviour:

```
rm -rf build dist *.spec
```

## Support

Any issues please contact <danpoynor@gmail.com>.