from opencompass.models import HuggingFaceBaseModel
import torch


models = [
    dict(
        type=HuggingFaceBaseModel,
        abbr='PULSE-7bv5',
        path='/home/PULSE-7bv5',
        tokenizer_path='/home/PULSE-7bv5',
        model_kwargs=dict(
            trust_remote_code=True,
            torch_dtype=torch.bfloat16,
            device_map='auto',
        ),
        tokenizer_kwargs=dict(
            trust_remote_code=True,
        ),
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
