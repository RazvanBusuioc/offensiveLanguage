from mimetypes import init
import tensorflow as tf
import tensorflow_addons as tfa
from transformers import TFAutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("readerbench/RoBERT-base")
bert = TFAutoModel.from_pretrained("readerbench/RoBERT-base")


def decodeLabel(numberLabel):
    labelCodificationMap = {0:"OTHER", 1:"PROFANITY", 2:"INSULT", 3:"ABUSE"}
    return labelCodificationMap[numberLabel]

class Model:
    def __init__(self, modelPath, tokenLen):
        self.model = tf.keras.models.load_model(modelPath)
        self.tokenLen = tokenLen
    
    def predict(self, texts):
        XTEST = tokenizer(texts, padding='max_length',return_tensors="np", truncation=True, max_length=self.tokenLen)
        XTEST = list(XTEST.values())
        predictions = self.model.predict(XTEST)
        return [decodeLabel(tf.argmax(pred, axis=0).numpy()) for pred in predictions]