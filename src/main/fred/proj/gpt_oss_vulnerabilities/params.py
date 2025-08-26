import random
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass(frozen=True, slots=True)
class Params:
    user_profile: dict
    model_config: dict
    prompt_config: dict

    @classmethod
    def from_csv(cls, filepath: str):
        import pandas as pd

        df = pd.read_csv(filepath)
        return cls(
            **{
                group: df.query(f"group == '{group}'").set_index("category_name")[cols].map(lambda val: val.split(", ")).T.to_dict()
                for group, cols in [
                    ("user_profile", ["category_values", "potentially_vulnerable_values"]),
                    ("model_config", ["category_values"]),
                    ("prompt_config", ["category_values"])
                ]
            }
        )
    
    def combinations(self, group: str, exclude_id: bool = False, sample_size: int = 0, sample_seed: Optional[int] = 42):
        import itertools
        import uuid
        import json

        # Create grid of category values
        grid = {
            category: values["category_values"]
            for category, values in asdict(self)[group].items()
        }

        # If sample_size is specified, randomly sample combinations
        if sample_size > 0:
            rng = random.Random()  # TODO: Add seed
            for _ in range(sample_size):
                payload = {k: rng.choice(v) for k, v in grid.items()}
                if group == "user_profile":
                    payload["vulnerability"] = sum(
                        payload[category] in asdict(self)[group][category]["potentially_vulnerable_values"]
                        for category in grid.keys()
                    )
                if not exclude_id:
                    payload[f"{group}_id"] = str(uuid.uuid5(uuid.NAMESPACE_OID, json.dumps(payload)))
                yield payload
        # Otherwise, yield all combinations
        else:
            for combination in itertools.product(*grid.values()):
                payload = dict(zip(grid.keys(), combination))
                if group == "user_profile":
                    payload["vulnerability"] = sum(
                        payload[category] in asdict(self)[group][category]["potentially_vulnerable_values"]
                        for category in grid.keys()
                    )
                if not exclude_id:
                    payload[f"{group}_id"] = str(uuid.uuid5(uuid.NAMESPACE_OID, json.dumps(payload)))
                yield payload


    def experiment_config(self, samples: int):

        for user_profile, model_config, prompt_config in zip(
            self.combinations("user_profile", sample_size=samples),
            self.combinations("model_config", sample_size=samples),
            self.combinations("prompt_config", sample_size=samples)
        ):
            yield {
                    "user_profile": user_profile,
                    "model_config": model_config,
                    "prompt_config": prompt_config
                }