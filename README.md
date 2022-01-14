# ImageConverter
A Python based Image converter supporting a bunch of image formats.
### Supported Formats:
`.bmp`, `.dds`, `.dib`, `.eps`, `.gif`, `.icns`, `.ico`, `.im`, `.msp`, `.pcx`, `.png`, `.ppm`, `.sgi`, `.spider`, `.tga`, `.tiff`, `.webp`, `.xbm`, `.palm`, `.pdf`, `.xv`
Note that many more file formats such as ``.jpg` and `.jpeg` can be read by the program but not converted into.

### Requirments
Python needs to be isntalled for this program to work.
Tkinter doesn't work when .py converted to .exe for some reason - this script uses Tkinter as the graphics library

I recommend creating a shortcut that executes the command automatically and pin it to Start or Taskbar (navigate to StartMenu folder, right click, new > shortcut, command:`C:\Windows\System32\cmd.exe /k python [File location]/ImageConverter_v1.1.py && exit`

##### Required Python libraries
- PIL (install with `pip install pillow`)
- sys (install with `pip install sys`)
- os (install with `pip install os`)
- tkinter (install with `pip install tk`)

**Usually sys and os come already preinstalled along with the python installation**

### Demonstration
![ezgif-2-1a693e16d6](https://user-images.githubusercontent.com/91549607/149475537-8841d8ba-4889-4c1d-a6f4-e27a8dfc3416.gif)
