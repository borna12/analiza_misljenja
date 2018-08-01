import cx_Freeze, os, sys

base = None
os.environ['TCL_LIBRARY'] = r"D:\py32\tcl\tcl8.6" 
os.environ['TK_LIBRARY'] = r"D:\py32\tcl\tk8.6" 

if sys.platform=='win32':
    base="Win32GUI"

executables=[cx_Freeze.Executable("analiza misljenja.py",base=base,icon='favicon.ico')]

cx_Freeze.setup(
    name="rjecnik",
    options={"build_exe":{"packages":["tkinter","nltk","io",'atexit', 'numpy.core._methods', 'numpy.lib.format'],
    "include_files":["favicon.ico","tcl86t.dll", "tk86t.dll", "pozitivno.txt", "negativno.txt", "neutralno.txt"]}},
    version="0.1",
    description="program za analizu mišljenja iz teksta",
    executables=executables
)


