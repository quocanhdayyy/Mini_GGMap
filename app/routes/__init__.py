"""
Routes Registration
===================

Đăng ký tất cả blueprints cho Flask app
"""

def register_blueprints(app):
    """
    Register all blueprints with the Flask app
    
    Args:
        app (Flask): Flask application instance
    """
    
    # Main routes (home, map display)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)
    
    # API routes (pathfinding, geocoding)
    from app.routes.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Admin routes removed
    
    app.logger.info("All blueprints registered")