from transformers import AutoTokenizer, AutoModelForCausalLM
import os

MODEL_NAME = "Ricky131/model-hoax-gpt2"
MODEL_DIR = "./model"

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

print(f"Downloading model '{MODEL_NAME}' to '{MODEL_DIR}'...")

# Download and save the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)

print("✅ Model download complete.")