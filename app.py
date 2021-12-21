from tensorflow.keras.preprocessing.text import Tokenizer

#Let's add custom sentences 
sentences = [
    "OSMO FOUNDATION - osmo Montreal QC Tangerine travel savings",
    "Withdrawal to Tangerine Savings Account-Travel-434535435!",
    "Tangerine SQUARE INC MSP/DIV travel"
]

#Tokenize the sentences
myTokenizer = Tokenizer(num_words=10)
myTokenizer.fit_on_texts(sentences)
print(myTokenizer.word_index)