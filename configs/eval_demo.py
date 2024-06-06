from mmengine.config import read_base

with read_base():
    from .datasets.MedBench.medbench_gen import medbench_datasets
    from .models.chatglm.hf_chatglm2_6b_int4 import models

datasets = [*medbench_datasets]
