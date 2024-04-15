import os
import sys
import site
import traceback
import subprocess
if __name__ == "__main__":

     # 获取 pystand.exe 记录的程序入口环境变量
    
        # 启动正式入口
    from py_src.run import main

    main(engineAddImportPath="/home/temp/Umi-OCR/UmiOCR-data/py_src/venv/lib/python3.11/site-packages/PySide2/Qt/qml/")