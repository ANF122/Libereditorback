from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Activer les requêtes CORS pour accepter les requêtes cross-origin

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Gérer la requête POST
        try:
            data = request.get_json()  # Récupérer les données envoyées
            if not data:
                return jsonify({'error': 'Aucune donnée fournie'}), 400

            # Traiter les données reçues (par exemple, les sauvegarder dans une base de données)
            # Ici on va juste renvoyer les données pour tester
            return jsonify({
                'message': 'Requête POST réussie !',
                'data_received': data
            }), 200

        except Exception as e:
            return jsonify({'error': f'Erreur lors de la requête POST : {str(e)}'}), 500

    elif request.method == 'GET':
        # Gérer la requête GET
        try:
            return jsonify({'message': 'Hello World!'}), 200
        except Exception as e:
            return jsonify({'error': f'Erreur lors de la requête GET : {str(e)}'}), 500

# Endpoint pour vérifier si l'API est en ligne
@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'API en ligne'}), 200

# Endpoint pour gérer des requêtes plus spécifiques si besoin
@app.route('/api/data', methods=['POST'])
def handle_data():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Aucune donnée reçue'}), 400

        # Faire des opérations avec les données, par exemple :
        processed_data = {'key': 'valeur de test'}  # Simulation de traitement

        return jsonify({
            'message': 'Les données ont été traitées avec succès',
            'original_data': data,
            'processed_data': processed_data
        }), 200

    except Exception as e:
        return jsonify({'error': f'Erreur lors du traitement des données : {str(e)}'}), 500

if __name__ == '__main__':
    # Lancer l'application sur le port 10000 (changer le port si nécessaire)
    app.run(host='0.0.0.0', port=10000)
