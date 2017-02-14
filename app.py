import dictogram
import sample
import sentence
import word_array
import word_count


from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return sample.generate_word(histogram)
    return sentence.generate_sentence(app.histogram)


def create_histogram():
    words_list = word_array.list_token("tom_sawyer.txt")
    # make a Dictogram object which types dictionary
    app.histogram = dictogram.Dictogram(words_list)


create_histogram()


if __name__ == '__main__':
    app.run()
