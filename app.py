from flask import Flask, render_template,g

app = Flask(__name__)
import keras
import csv
import numpy as np
import random

@app.before_first_request
def do_something_on_startup():
    # Add code here to run on server startup

    
      # select n random items from data
       
    pass

@app.route('/')
def home():
    # Add code here for your home page
    with open(r'files\books_details.csv', encoding='utf-8') as fd:
        reader = csv.reader(fd)
        g.data = list(reader)
    n = 8
    random_books = random.sample(g.data[1:], n)
    context={
        "random_books":random_books
    }
    return render_template('index.html', **context)

@app.route('/recommendations')
def recommendations():
    # Add code here to calculate and return recommended books
    # Load the trained model from file
    model = keras.models.load_model(r'model\trained_book_model.h5')

    # Get the book embedding layer from the loaded model
    book_layer = model.get_layer('book_embedding')

    # Get the learned weights of the book embedding layer
    book_weights = book_layer.get_weights()[0]

    # Normalize the book weights using L2 normalization
    book_weights = book_weights / np.linalg.norm(book_weights, axis=1).reshape((-1, 1))

    with open(r'files\books.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)

    books = np.array(data).reshape(len(data))
    book_index = {book: idx for idx, book in enumerate(books)}
    index_book = {idx: book for book, idx in book_index.items()}
    pass

if __name__ == '__main__':
    app.run()
