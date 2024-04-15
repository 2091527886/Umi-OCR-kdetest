# 根据当前环境，提供不同平台对象
import sys

# 根据当前操作系统选择要导入的模块
_plat = sys.platform
if _plat.startswith("win32"):
    from .win32.win32_api import Api as _Platform
    print("no")
elif _plat.startswith("linux"):
    
    #raise ImportError("尚未支持linux系统！")
    #from .win32.win32_api import Api as _Platform
    print("no")
elif _plat.startswith("darwin"):
    raise ImportError("尚未支持macos系统！")
else:
    raise ImportError(f"未知系统：{_plat}")
class Api:
    def __init__(self) -> None:
        pass
# 构造单例：平台对象
Platform = Api()
