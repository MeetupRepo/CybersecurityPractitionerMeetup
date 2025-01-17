from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from typing import List, Dict, Any

app = FastAPI()

# Load model and tokenizer globally
print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    padding_side="right"
)
print("Model loaded successfully!")

class GenerateRequest(BaseModel):
    prompt: str
    max_length: int = 200
    temperature: float = 0.7

@app.post("/generate")
async def generate_text(request: GenerateRequest) -> Dict[str, Any]:
    try:
        # Format prompt according to TinyLLaMA chat template
        chat_prompt = f"<|im_start|>user\n{request.prompt}<|im_end|>\n<|im_start|>assistant\n"
        
        inputs = tokenizer(chat_prompt, return_tensors="pt").to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=request.max_length,
                temperature=request.temperature,
                do_sample=True,
                pad_token_id=tokenizer.pad_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        response = response.split("assistant\n")[-1].strip()
        
        return {
            "generated_text": response,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "TinyLlama-1.1B-Chat"}