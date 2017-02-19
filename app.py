import dictogram
import sample
import sentence
import word_array
import word_count
import markov

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return sample.generate_word(histogram)
    # return sentence.generate_sentence(app.histogram)
    return app.mar.gen_sent()


def create_histogram():
    words_list = word_array.list_token("tom_sawyer.txt")
    # make a Dictogram object which types dictionary
    app.histogram = dictogram.Dictogram(words_list)


def markov_sent():
    words_list = word_array.list_token("tom_sawyer.txt")
    app.mar = markov.Markov(words_list=words_list)


create_histogram()
markov_sent()

if __name__ == '__main__':
    # This code only runs if you execute this script locally
    app.run()
