from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Carregar o modelo BERT pré-treinado para classificação de sentimentos (PyTorch)
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Carregar o tokenizador correspondente ao modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Função para preprocessar o texto
def preprocess_text(text):
    # Tokenizar o texto
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    return inputs

# Função para prever o sentimento
def predict_sentiment(text):
    # Pré-processar o texto
    inputs = preprocess_text(text)
    
    # Fazer a predição
    with torch.no_grad():  # Impede que o PyTorch calcule o gradiente
        predictions = model(**inputs).logits
    sentiment = torch.argmax(predictions, dim=1).item()  # Pega a classe com maior valor

    # Sentimento baseado na classe
    if sentiment == 0:
        return "Negativo"
    elif sentiment == 1:
        return "Levemente Negativo"
    elif sentiment == 2:
        return "Neutro"
    elif sentiment == 3:
        return "Levemente Positivo"
    else:
        return "Positivo"

while True:
    try:
        mensagem = input("Digite uma frase para analisar o sentimentos:\n")
        print(f"\n{predict_sentiment(mensagem)}\n")
    except Exception as e:
        print(f"Erro ao processar a entrada: {e}")