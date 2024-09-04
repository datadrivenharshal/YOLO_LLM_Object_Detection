from transformers import pipeline

def generate_text(objects):
    """Generates descriptive text based on detected objects."""
    # Initialize the text generation pipeline
    text_generator = pipeline(
        'text-generation', 
        model='gpt2', 
        tokenizer='gpt2',
        use_auth_token=''  # Token for authentication
    )

    # Prepare the prompt
    prompt = f"In the image, I can see {', '.join(objects)}."

    # Generate text
    generated_texts = text_generator(prompt, max_length=50, num_return_sequences=1, truncation=True)

    # Extract the generated text
    generated_text = generated_texts[0]['generated_text']
    
    return generated_text
