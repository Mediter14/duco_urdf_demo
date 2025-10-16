from asyncio import sleep
from vuer import Vuer, VuerSession
from vuer.schemas import Urdf

app = Vuer()


@app.spawn(start=True)
async def main(proxy: VuerSession):
    proxy.upsert @ Urdf(
        src="https://raw.githubusercontent.com/Mediter14/duco_urdf_demo/main/test.urdf",
        jointValues={},
        rotation=[3.14/2 + 3.14, 0, 0],
        position=[0, 0, 0],
        key="duco_model",
    )

    # keep the session alive.
    while True:
        await sleep(10)
