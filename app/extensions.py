"""
Flask Extensions
================

Khởi tạo và cấu hình các extension cho Flask app
"""

def init_extensions(app):
    """
    Initialize Flask extensions
    
    Args:
        app (Flask): Flask application instance
    """
    
    # Initialize cache (in-memory for now, can be extended to Redis)
    init_cache(app)
    
    # Initialize logging
    init_logging(app)
    
    # Initialize data directories
    init_directories(app)

def init_cache(app):
    """Initialize caching system"""
    # Simple in-memory cache for development
    # TODO: Implement Redis cache for production
    if not hasattr(app, 'cache'):
        app.cache = {}
    
    app.logger.info("Cache initialized (in-memory)")

def init_logging(app):
    """Initialize logging configuration"""
    import logging
    
    if not app.debug:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(levelname)s: %(message)s'
        )
    
    app.logger.info("Logging initialized")

def init_directories(app):
    """Initialize required directories"""
    app.config['DATA_DIR'].mkdir(parents=True, exist_ok=True)
    app.config['GEOJSON_DIR'].mkdir(parents=True, exist_ok=True)
    app.config['GRAPH_DIR'].mkdir(parents=True, exist_ok=True)
    
    app.logger.info("Data directories initialized")