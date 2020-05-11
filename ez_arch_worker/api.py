import asyncio
import logging

import ez_arch_worker.lib.app as ez_app
import ez_arch_worker.lib.worker as worker


Frames = ez_app.Frames
Handler = ez_app.Handler
State = ez_app.State


async def run_worker(
        *,
        service_name: bytes,
        handler: Handler,
        initial_state: State = None,
        listen_host: str,
        port: int,
        poll_interval_ms: int = ez_app.DEFAULT_POLL_INTERVAL_MS
)-> None:
    app = ez_app.App(
        con_s = "tcp://{}:{}".format(listen_host, port),
        handler = handler,
        impl_state = initial_state,
        poll_interval_ms = poll_interval_ms,
        service_name = service_name,
    )
    await worker.run_main_loop(app)
    return
