import openai
import base64
import time
import os

# === CONFIG ===
openai.api_key = "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"  # 🔒 Replace with your API key
output_dir = "generated_drawings"
os.makedirs(output_dir, exist_ok=True)

prompts = [
    "An engineering drawing showing the front, or a section view, of a complex mechanical part. ISO style.",
    "A technical drawing showing a flange with chamfers, fillets, and multiple holes. Dimensioned.",
    "A CAD drawing of a gearbox cross section with a title block. Black and white.",
]

# === Generate Images ===
for i, prompt in enumerate(prompts):
    print(f"🧠 Generating image {i+1}: {prompt}")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        model="gpt-4o"  # GPT-4o uses this under the hood
    )

    image_url = response["data"][0]["url"]
    print("📸 Image URL:", image_url)

    # Save the image to disk
    import requests
    image_data = requests.get(image_url).content
    filename = os.path.join(output_dir, f"drawing_{i+1}.png")
    with open(filename, "wb") as f:
        f.write(image_data)
    print(f"✅ Saved to {filename}\n")

    time.sleep(1)  # Respect rate limits