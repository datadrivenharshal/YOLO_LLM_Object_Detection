from transformers import pipeline

def generate_text(objects):
    """Generates descriptive text based on detected objects."""
    text_generator = pipeline('text-generation', model='gpt-2')
    prompt = f"In the image, I see {', '.join(objects)}."
    generated_text = text_generator(prompt, max_length=50)[0]['generated_text']
    return generated_text
