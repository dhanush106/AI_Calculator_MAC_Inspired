import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

output_file = "model_list.txt"

with open(output_file, "w") as f:
    if not api_key:
        f.write("API Key not found in environment\n")
    else:
        f.write(f"Using API Key: {api_key[:10]}...\n")
        genai.configure(api_key=api_key)
        try:
            f.write("Listing all models:\n")
            models = list(genai.list_models())
            if not models:
                f.write("No models found.\n")
            for m in models:
                f.write(f"- {m.name} (Methods: {m.supported_generation_methods})\n")
        except Exception as e:
            f.write(f"Error listing models: {e}\n")

print(f"Results written to {output_file}")
