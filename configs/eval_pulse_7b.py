from mmengine.config import read_base

with read_base():
    from .datasets.MedBench.medbench_gen import medbench_datasets
    from .models.pulse.hf_pulse_7b import models

datasets = [*medbench_datasets]
