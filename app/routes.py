from flask import Blueprint, jsonify
from app import db

api_bp = Blueprint('api', __name__)

@api_bp.route('/categories', methods=['GET'])
def get_categories():
    try:
        # Get all documents from the 'universalCategories' collection
        categories_ref = db.collection('universalCategories')
        docs = categories_ref.stream()
        
        categories = []
        for doc in docs:
            category_data = doc.to_dict()
            category_data['id'] = doc.id
            categories.append(category_data)
        
        return jsonify({
            "status": "success",
            "data": categories
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api_bp.route('/brands', methods=['GET'])
def get_brands():
    try:
        # Get all documents from the 'brands' collection
        brands_ref = db.collection('brands')
        docs = brands_ref.stream()
        
        brands = []
        for doc in docs:
            brand_data = doc.to_dict()
            brand_data['id'] = doc.id
            brands.append(brand_data)
        
        return jsonify({
            "status": "success",
            "data": brands
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@api_bp.route('/all-data', methods=['GET'])
def get_all_data():
    try:
        # Get categories
        categories_ref = db.collection('universalCategories')
        categories_docs = categories_ref.stream()
        
        categories = []
        for doc in categories_docs:
            category_data = doc.to_dict()
            category_data['id'] = doc.id
            categories.append(category_data)
        
        # Get brands
        brands_ref = db.collection('brands')
        brands_docs = brands_ref.stream()
        
        brands = []
        for doc in brands_docs:
            brand_data = doc.to_dict()
            brand_data['id'] = doc.id
            brands.append(brand_data)
        
        return jsonify({
            "status": "success",
            "data": {
                "categories": categories,
                "brands": brands
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500