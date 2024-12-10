from cx_Freeze import setup, Executable

setup(
    name = "MP3Converter",
    version = "1.0",
    description = "Media to MP3 Converter",
    executables = [Executable("mp3.py", base="Win32GUI")]
)