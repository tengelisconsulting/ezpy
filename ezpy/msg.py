from .apptypes import Frames


WORKER = b"\x01"
CLIENT = b"\x02"

HEARTBEAT = b"\x01"
REPLY = b"\x02"


def heartbeat(service_name: bytes) -> Frames:
    return _as_msg([HEARTBEAT, service_name])


def _as_msg(frames: Frames) -> Frames:
    return [b"", WORKER] + frames
