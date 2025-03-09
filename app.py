from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch data from the Dog API
    breeds_response = requests.get('https://dogapi.dog/api/v2/breeds')
    facts_response = requests.get('https://dogapi.dog/api/v2/facts?limit=5')
    
    if breeds_response.status_code == 200:
        breeds = breeds_response.json()
    else:
        breeds = []

    if facts_response.status_code == 200:
        facts = facts_response.json()
    else:
        facts = []

    return render_template('index.html', breeds=breeds, facts=facts)

@app.route('/breeds/<id>')
def breed(id):
    try:
        # Fetch breed details from the Dog API
        breed_response = requests.get(f'https://dogapi.dog/api/v2/breeds/{id}')

        if breed_response.status_code != 200:
            raise requests.RequestException("Breed not found")
        
        breed = breed_response.json()

        return render_template('breed.html', breed=breed)
    
    except requests.RequestException as e:
        return render_template('404.html', error=str(e))


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)