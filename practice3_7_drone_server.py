import websockets
import asyncio
import logging

logging.basicConfig(level=logging.INFO, filemode='w')


class SecureProxy:
    def __init__(self, control_drone):
        self.control_drone = control_drone

    async def __call__(self, websocket, path):
        async for msg in websocket:
            if self.is_auth(websocket):
                await self.control_drone(websocket, path, msg)
            else:
                await websocket.send("Неавторизированный доступ")

    def is_auth(self, websocket):
        try:
            # Проверка наличия параметров в пути вебсокета
            if "?" in websocket.path:
                params = websocket.path.split("?")[1]
                # Обработка параметров, разделенных амперсандом, и проверка наличия "="
                params = dict(param.split("=") for param in params.split("&") if "=" in param)
                # Проверка токена на валидность
                return params.get("token") == "valid_token"
        except Exception as e:
            # Логирование ошибки аутентификации
            logging.info(f"Ошибка аутентификации: {e}")
        return False


async def control_drone(websocket, path, msg):
    try:
        logging.info(f"Получена команда: {msg}")  # Заменить все принты на logging.info()
        # print(f"Получена команда: {msg}")
        if msg == "takeoff":
            logging.info(f"Дрон взлетает")
            await websocket.send("Дрон взлетает")
        elif msg == "land":
            logging.info(f"Дрон приземлился")
            await websocket.send("Дрон приземляется")

    except websockets.ConnectionClosed as e:
        logging.info(f"Соединение закрыто {e}")
    except Exception as e:
        logging.info(f"Ошибка: {e}")


async def main():
    proxy = SecureProxy(control_drone)

    async with websockets.serve(proxy, host="localhost", port=8765) as server:
        try:
            await server.wait_closed()
        except Exception as e:
            logging.info(e)
            logging.info("Сервер закрыт")
        # await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())
