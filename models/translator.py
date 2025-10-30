from transformers import MarianMTModel, MarianTokenizer

def translate_text(text):
    # Load Helsinki NLP's English to Farsi model
    model_name = "Helsinki-NLP/opus-mt-en-fa"
    
    # Load tokenizer and model
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    # Tokenize the text
    batch = tokenizer([text], return_tensors="pt", padding=True)
    
    # Generate translation
    translated = model.generate(**batch)
    
    # Decode the generated tokens
    result = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
    return result