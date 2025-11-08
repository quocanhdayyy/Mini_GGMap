"""
Admin Routes
============

Routes cho quản lý dữ liệu và monitoring system
"""

from flask import Blueprint, render_template, request, jsonify, current_app
import os
from pathlib import Path

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/')
def dashboard():
    """
    Admin dashboard
    
    TODO: 
    - System monitoring
    - Performance metrics
    - Data management tools
    """
    
    stats = {
        'total_nodes': 0,  # TODO: Count from graph
        'total_edges': 0,  # TODO: Count from graph
        'data_files': len(list(current_app.config['GEOJSON_DIR'].glob('*.geojson'))),
        'cache_size': len(getattr(current_app, 'cache', {}))
    }
    
    return render_template('admin/dashboard.html', stats=stats)

@admin_bp.route('/data')
def data_management():
    """
    Data management interface
    
    TODO:
    - Upload new GeoJSON files
    - Validate data format
    - Rebuild graph from new data
    """
    
    data_files = []
    geojson_dir = current_app.config['GEOJSON_DIR']
    
    if geojson_dir.exists():
        for file in geojson_dir.glob('*.geojson'):
            stat = file.stat()
            data_files.append({
                'name': file.name,
                'size': stat.st_size,
                'modified': stat.st_mtime
            })
    
    return render_template('admin/data.html', data_files=data_files)

@admin_bp.route('/upload', methods=['POST'])
def upload_data():
    """
    Upload new map data files
    
    TODO:
    - File validation
    - GeoJSON format checking
    - Automatic graph rebuilding
    """
    
    try:
        if 'file' not in request.files:
            return jsonify({
                'status': 'error',
                'message': 'No file uploaded'
            }), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({
                'status': 'error',
                'message': 'No file selected'
            }), 400
        
        if not file.filename.endswith('.geojson'):
            return jsonify({
                'status': 'error',
                'message': 'Only GeoJSON files are allowed'
            }), 400
        
        # TODO: Implement file upload and validation
        
        return jsonify({
            'status': 'success',
            'message': 'File uploaded successfully'
        })
        
    except Exception as e:
        current_app.logger.error(f"Upload error: {str(e)}")
        
        return jsonify({
            'status': 'error',
            'message': 'Upload failed'
        }), 500

@admin_bp.route('/rebuild', methods=['POST'])
def rebuild_graph():
    """
    Rebuild graph from current data
    
    TODO:
    - Load all GeoJSON files
    - Build new graph structure
    - Cache management
    """
    
    try:
        # TODO: Implement graph rebuilding
        
        return jsonify({
            'status': 'success',
            'message': 'Graph rebuilt successfully'
        })
        
    except Exception as e:
        current_app.logger.error(f"Rebuild error: {str(e)}")
        
        return jsonify({
            'status': 'error',
            'message': 'Rebuild failed'
        }), 500