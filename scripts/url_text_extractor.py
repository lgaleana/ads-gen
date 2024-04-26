import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template

app = Flask(__name__)


def extract_text_from_soup(soup: BeautifulSoup):
    text = ' '.join(t.strip() for t in soup.stripped_strings)
    return text


def extract_images_from_soup(soup: BeautifulSoup):
    images = [img['src'] for img in soup.find_all('img')]
    for link in soup.find_all('link', rel='stylesheet'):
        if 'background-image' in link['href']:
            images.append(link['href'])
    return images


@app.route('/extract', methods=['POST'])
def extract():
    url = request.form['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = extract_text_from_soup(soup)
    images = extract_images_from_soup(soup)
    return render_template('index.html', text=text, images=images)


if __name__ == '__main__':
    app.run(debug=True)