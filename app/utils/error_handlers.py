"""
Error Handlers
==============

Xử lý lỗi và exception handling cho Flask app
"""

from flask import render_template, jsonify, request

def setup_error_handlers(app):
    """
    Setup error handlers for the Flask app
    
    Args:
        app (Flask): Flask application instance
    """
    
    @app.errorhandler(404)
    def not_found_error(error):
        if request.path.startswith('/api'):
            return jsonify({
                'status': 'error',
                'message': 'API endpoint not found'
            }), 404
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        app.logger.error(f"Internal error: {error}")
        
        if request.path.startswith('/api'):
            return jsonify({
                'status': 'error',
                'message': 'Internal server error'
            }), 500
        return render_template('errors/500.html'), 500
    
    @app.errorhandler(400)
    def bad_request_error(error):
        if request.path.startswith('/api'):
            return jsonify({
                'status': 'error',
                'message': 'Bad request'
            }), 400
        return render_template('errors/400.html'), 400
    
    app.logger.info("Error handlers configured")