from opencompass.models import HuggingFaceCausalLM
import torch


models = [
    dict(
        type=HuggingFaceCausalLM,
        abbr='PULSE-7bv5',
        path='/home/dongru/PULSE-7bv5',
        tokenizer_path='/home/dongru/PULSE-7bv5',
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
        run_cfg=dict(num_gpus=2),
    )
]