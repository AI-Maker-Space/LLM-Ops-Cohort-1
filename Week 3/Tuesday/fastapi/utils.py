import time
import torch
import functools
from transformers import AutoModelForCausalLM, AutoTokenizer


def time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        return (result, exec_time)

    return wrapper


def memory_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        torch.cuda.empty_cache()
        torch.cuda.reset_peak_memory_stats()
        result, exec_time = func(*args, **kwargs)
        peak_mem = torch.cuda.max_memory_allocated()
        peak_mem_consumption = peak_mem / 1e9
        return peak_mem_consumption, exec_time, result

    return wrapper


@memory_decorator
@time_decorator
def generate_output(
    prompt: str, model: AutoModelForCausalLM, tokenizer: AutoTokenizer
) -> torch.Tensor:
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    input_ids = input_ids.to("cuda")
    outputs = model.generate(input_ids, max_length=500)
    return outputs
