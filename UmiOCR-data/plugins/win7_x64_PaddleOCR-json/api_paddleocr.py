# 调用 PaddleOCR-json.exe 的 Python Api
# 项目主页：
# https://github.com/hiroi-sora/PaddleOCR-json

from call_func import CallFunc
from json import loads as jsonLoads, dumps as jsonDumps
from .paddleocr import PPOCR_pipe
import subprocess
import os
import psutil  # 进程检查
from PIL import Image
import io
# exe路径
ExePath = os.path.dirname(os.path.abspath(__file__)) + "/PaddleOCR-json.exe"
# exe启动参数映射表。将配置项映射到启动参数
ExeConfigs = [
    ("enable_mkldnn", "enable_mkldnn"),  # mkl加速
    ("config_path", "language"),  # 配置文件路径
    ("cls", "cls"),  # 方向分类
    ("use_angle_cls", "cls"),  # 方向分类
    ("limit_side_len", "limit_side_len"),  # 长边压缩
    ("cpu_threads", "cpu_threads"),  # 线程数
]


class Api:  # 公开接口
    def __init__(self, globalArgd):
        # 测试路径是否存在
        # 初始化参数
        self.api = None  # api对象
        self.exeConfigs = {}  # exe启动参数字典
        self._updateExeConfigs(self.exeConfigs, globalArgd)  # 更新启动参数字典
        # 内存清理参数
        self.ramInfo = {"max": -1, "time": -1, "timerID": ""}
        m = globalArgd["ram_max"]
        if isinstance(m, (int, float)):
            self.ramInfo["max"] = m
        m = globalArgd["ram_time"]
        if isinstance(m, (int, float)):
            self.ramInfo["time"] = m
        self.isInit = True

    # 更新启动参数，将data的值写入target
    def _updateExeConfigs(self, target, data):
        print("_updateExeConfigs没实现")

    # 启动引擎。返回： "" 成功，"[Error] xxx" 失败
    def start(self, argd):
        # 加载局部参数
        print("start没实现")
        return ""

    def stop(self):  # 停止引擎
        #if self.api == None:
            #return
        #self.api.exit()
        #self.api = None
        print("stop没实现")

    def runPath(self, imgPath: str):  # 路径识图
        self.__runBefore()
        #res = self.api.run(imgPath)
        #self.__ramClear()
        command = "cd /home/temp/Umi-OCR-1/UmiOCR-data/plugins/win7_x64_PaddleOCR-json/&&/home/temp/Umi-OCR-1/UmiOCR-data/plugins/win7_x64_PaddleOCR-json/PaddleOCR-json.exe -image_path=\""+imgPath+"\" 2>/dev/null| sed '1,3d'| sed '2d' > /tmp/1.txt"
        sub1 = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True,encoding="utf-8")
        sub1.wait()
        with open("/tmp/1.txt", 'rb') as file:
            res =jsonLoads(file.read().decode("utf-8", errors="ignore"))
            
            print(type(res))
            print(res)
        file.close()
        return res

    def runBytes(self, imageBytes):  # 字节流
        #self.__runBefore()
        image_file = io.BytesIO(imageBytes)
        image = Image.open(image_file)
        image.save('/tmp/output_image.png')
        name = "/tmp/output_image.png"
        command = "cd /home/temp/Umi-OCR-1/UmiOCR-data/plugins/win7_x64_PaddleOCR-json/&&/home/temp/Umi-OCR-1/UmiOCR-data/plugins/win7_x64_PaddleOCR-json/PaddleOCR-json.exe -image_path=\""+name+"\" 2>/dev/null| sed '1,3d'| sed '2d' > /tmp/2.txt"
        sub1 = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True,encoding="utf-8")
        sub1.wait()
        with open("/tmp/2.txt", 'rb') as file:
            res =jsonLoads(file.read().decode("utf-8", errors="ignore"))
            
            print(type(res))
            print(res)
        file.close()
        return res
       #res = self.api.runBytes(imageBytes)
        #self.__ramClear()
        #return res
        #print("runBytes没实现")

    def runBase64(self, imageBase64):  # base64字符串
        self.__runBefore()
        #res = self.api.runBase64(imageBase64)
        #self.__ramClear()
        #return res
        print("runBase64没实现")

    def __runBefore(self):
        CallFunc.delayStop(self.ramInfo["timerID"])  # 停止ram清理计时器

    def _restart(self):  # 重启引擎
        print("_restart没实现")

    def __ramClear(self):
        print("__ramClear没实现")# 内存清理
