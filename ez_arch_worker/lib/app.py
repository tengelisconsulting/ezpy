from typing import Any
from typing import Awaitable
from typing import Callable
from typing import List
from typing import NamedTuple
from typing import Tuple

import zmq.asyncio

DEFAULT_POLL_INTERVAL_MS = 3000

Ctx = zmq.asyncio.Context
Frames = List[bytes]
State = Any
Handler = Callable[[State, Frames],
                   Awaitable[Tuple[State, Frames]]]


class App(NamedTuple):
    handler: Handler
    c: Ctx = zmq.asyncio.Context()
    con_s: str = ""
    dealer: zmq.asyncio.Socket = None
    impl_state: State = None
    poller: zmq.asyncio.Poller = zmq.asyncio.Poller()
    poll_interval_ms: int = DEFAULT_POLL_INTERVAL_MS
    service_name: bytes = b""