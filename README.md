# HEIC 2 JPG Converter

## Description

A quick simple application to convert HEIC files to JPG format. Drag and drop HEIC files onto the application icon or window to convert them.

## Windows 10 Usage

1. Download the raw ZIP file from the [`distro/`](https://github.com/danpoynor/heic-2-jpg-converter/blob/main/distro/heic2jpg.zip) (download arrow icon on the right).
2. Extract the ZIP file and open the `heic2jpg` directory.
3. Drag the `heic2jpg.exe` executable to whereever you want it to live on your computer (such as your desktop)
4. Double-click the icon to open it then drag and drop HEIC files onto the application window. The files will be automatically converted to JPG format.
5. You should also be able to drag and drop `.heic` image files on to the icon and it will open and convert them automatically.

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