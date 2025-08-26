import os
import time
import datetime as dt
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True, slots=True)
class CLI:
    start_counter: float = field(default_factory=time.perf_counter)
    start_ts: str = field(default_factory=dt.datetime.utcnow().isoformat)

    @classmethod
    def cli_exec(cls, *args, **kwargs):
        import fire

        cli_instance = cls(*args, **kwargs)
        return fire.Fire(cli_instance)

    @property
    def version(self) -> str:
        version_filepath = os.path.join(
            os.path.dirname(__file__),
            "version"
        )
        with open(version_filepath, "r") as file:
            return file.read().strip()

    def env(self, var: str) -> str:
        return os.environ.get(var) or ""

    def hello(self, name: Optional[str] = None) -> str:
        return f"Hello, {name or 'World'}!"