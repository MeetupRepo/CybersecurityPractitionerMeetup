from fastapi import FastAPI
from transformers import pipeline
import torch

app = FastAPI()

# Enable GPU optimization
torch.backends.cudnn.benchmark = True

# Load model with optimizations
model = pipeline("text-generation",
    model="TinyLLama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.float16,  # Use half precision
    device_map="auto",         # Automatic device optimization
    model_kwargs={
        "low_cpu_mem_usage": True,
    }
)

# Batch processing configuration
BATCH_SIZE = 1  # Adjust based on your GPU memory
MAX_LENGTH = 256  # Limit output length

@app.post("/generate")
async def generate_text(prompt: str):
    try:
        response = model(prompt, 
            max_length=MAX_LENGTH,
            num_return_sequences=1,
            pad_token_id=model.tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7
        )
        return {"generated_text": response[0]["generated_text"]}
    except Exception as e:
        return {"error": str(e)}