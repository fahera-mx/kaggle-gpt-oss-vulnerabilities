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
    
    def run_experiment(
            self,
            size: int,
            experiment_params_filepath: str,
            output_dirpath: Optional[str] = None,
    ):
        from fred.proj.gpt_oss_vulnerabilities.experiment import Experiment

        output_dirpath = output_dirpath or os.path.join(
            os.path.dirname(experiment_params_filepath),
            "experiment-output"
        )
        experiment = Experiment.from_csv(experiment_params_filepath)
        experiment.run(output_dirname=output_dirpath, sample_size=size)