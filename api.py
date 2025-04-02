from flask import Blueprint, jsonify, request\nfrom flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token\nfrom models import User, Visualization, Report, db\nfrom werkzeug.security import check_password_hash\n\napi_bp = Blueprint('api', __name__)\n\n@api_bp.route('/register', methods=['POST'])\ndef register():\n    data = request.get_json()\n    if not data or not data.get('username') or not data.get('password'):\n        return jsonify({'error': 'Username and password are required'}), 400\n    user = User(username=data['username'])\n    user.set_password(data['password'])\n    db.session.add(user)\n    db.session.commit()\n    return jsonify({'message': 'User registered successfully'}), 201\n\n@api_bp.route('/login', methods=['POST'])\ndef login():\n    data = request.get_json()\n    if not data or not data.get('username') or not data.get('password'):\n        return jsonify({'error': 'Username and password are required'}), 400\n    user = User.query.filter_by(username=data['username']).first()\n    if not user or not user.check_password(data['password']):\n        return jsonify({'error': 'Invalid credentials'}), 401\n    access_token = create_access_token(identity=user.id)\n    return jsonify({'access_token': access_token}), 200\n\n@api_bp.route('/uploadCSV', methods=['POST'])\n@jwt_required()\ndef uploadCSV():\n    # Placeholder for CSV upload logic\n    return jsonify({'message': 'CSV uploaded successfully'}), 200\n\n@api_bp.route('/visualize', methods=['GET'])\n@jwt_required()\ndef visualize():\n    # Placeholder for visualization logic\n    return jsonify({'message': 'Visualization generated successfully'}), 200\n\n@api_bp.route('/customize', methods=['POST'])\n@jwt_required()\ndef customize():\n    # Placeholder for customization logic\n    return jsonify({'message': 'Customization applied successfully'}), 200\n\n@api_bp.route('/generateReport', methods=['GET'])\n@jwt_required()\ndef generateReport():\n    # Placeholder for report generation logic\n    return jsonify({'message': 'Report generated successfully'}), 200\n\n@api_bp.route('/saveVisualization', methods=['POST'])\n@jwt_required()\ndef saveVisualization():\n    # Placeholder for visualization saving logic\n    return jsonify({'message': 'Visualization saved successfully'}), 200\n