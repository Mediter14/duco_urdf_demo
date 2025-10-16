import asyncio
from vuer import Vuer, VuerSession
from vuer.schemas import Urdf
import os

desktop_path = "/home/yifan2577923879/Desktop"
urdf_path = os.path.join(desktop_path, "test.urdf")

# 检查文件是否存在
print("检查 URDF 文件:", os.path.exists(urdf_path))
print("检查 static_root 目录:", os.path.exists(desktop_path))

# 明确指定静态文件目录
app = Vuer(static_root=desktop_path, debug=True)

@app.spawn(start=True)
async def main(session: VuerSession):
    # 告诉 Vuer 你的 URDF 在 /static 路径下
    session.upsert @ Urdf(
        src="/static/111.urdf",  # 非本地路径！一定要 /static 开头
        position=[0, 0, 0],
        rotation=[0, 0, 0],
        scale=[1000, 1000, 1000],  # 若 STL 是毫米制
        key="duco_arm"
    )

    while True:
        await asyncio.sleep(1)

app.run()
