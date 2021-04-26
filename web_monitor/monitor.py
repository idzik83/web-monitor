import asyncio
import logging
import time

import aiohttp

from web_monitor.models import MonitorConfigModel

logger = logging.getLogger(__file__)


class WebMonitor:
    def __init__(self, config: dict):
        self._config = MonitorConfigModel.validate(config)
        self._is_running = False

    async def run(self):
        self._is_running = True
        while self._is_running:
            await self._run_monitoring()
            await asyncio.sleep(self._config.period)

    def stop(self):
        self._is_running = False

    async def _run_monitoring(self):
        start_time = time.time()
        response = await self._get_response()
        end_time = time.time()
        print(f"Url: {self._config.web_site}; Status: {response.status}; Response time: {end_time - start_time}")

    async def _get_response(self) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            return await session.get(self._config.web_site)
