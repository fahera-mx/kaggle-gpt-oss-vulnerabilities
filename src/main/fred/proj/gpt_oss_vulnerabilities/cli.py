import os
import time
import datetime as dt
from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True, slots=True)
class CLI:
    start_counter: float = field(default_factory=time.perf_counter)
    start_ts: str = field(default_factory=dt.datetime.utcnow().isoformat)

    def __post_init__(self):
        from dotenv import load_dotenv

        # TODO: we should allow user to disable this...
        # probably with an intential env.var such as "FRD_SKIP_DOTENV_AUTOLOAD"
        load_dotenv()

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
    
    @staticmethod
    def run_experiment(
            name: str,
            num: int,
            work_dirpath: str,
            **kwargs,
    ):
        from fred.proj.gpt_oss_vulnerabilities.experiment import (
            ExperimentGrid,
            ExperimentContrast,
        )

        output_dirpath = os.path.join(
            work_dirpath,
            f"experiment-{name}-output".lower()
        )
        match name.lower():
            case "grid":
                experiment = ExperimentGrid.from_csv(
                    filepath=os.path.join(
                        work_dirpath,
                        kwargs.get("params_filename", "experiment-params.csv")
                    )
                )
                experiment.run(output_dirpath=output_dirpath, sample_size=num)
            case "contrast":
                experiment = ExperimentContrast()
                experiment.run(output_dirpath=output_dirpath, n=num)
            case _:
                raise ValueError(f"Unknown experiment name: {name}")