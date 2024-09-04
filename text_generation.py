from transformers import pipeline

def generate_text(objects):
    """Generates descriptive text based on detected objects."""
    #text_generator = pipeline('text-generation', model='gpt-2')
    text_generator = pipeline('text-generation', model='gpt2', use_auth_token='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')

    prompt = f"In the image, I can see {', '.join(objects)}."
    generated_text = text_generator(prompt, max_length=50)[0]['generated_text']
    return generated_text
