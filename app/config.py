"""
Configuration Management
========================

Cấu hình cho các môi trường khác nhau: development, testing, production
"""

import os
from pathlib import Path

# Base directory của project
BASE_DIR = Path(__file__).parent.resolve()

class Config:
    """Base configuration class"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Data file paths
    DATA_DIR = BASE_DIR / 'static' / 'data'
    GEOJSON_DIR = DATA_DIR / 'geojson'
    GRAPH_DIR = DATA_DIR / 'graph'
    
    # Map settings
    DEFAULT_MAP_CENTER = [21.0285, 105.8542]  # Hà Nội
    DEFAULT_ZOOM = 13
    
    # Algorithm settings
    SUPPORTED_VEHICLES = ['car', 'motor', 'foot']
    SUPPORTED_ALGORITHMS = ['dijkstra', 'a_star', 'bfs', 'dfs', 'greedy']
    
    # Performance settings
    MAX_NODES = 10000
    CACHE_TIMEOUT = 300  # 5 minutes
    
    @staticmethod
    def init_app(app):
        """Initialize app with this config"""
        # Create data directories if they don't exist
        Config.DATA_DIR.mkdir(parents=True, exist_ok=True)
        Config.GEOJSON_DIR.mkdir(parents=True, exist_ok=True)
        Config.GRAPH_DIR.mkdir(parents=True, exist_ok=True)

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    
    # Relaxed settings for development
    MAX_NODES = 5000

class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    
    # Smaller limits for faster tests
    MAX_NODES = 1000
    CACHE_TIMEOUT = 10

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # Stricter settings for production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        
        # Production-specific initialization
        import logging
        from logging.handlers import RotatingFileHandler
        
        # Setup file logging
        if not app.debug:
            file_handler = RotatingFileHandler(
                'logs/mini_ggmap.log', maxBytes=10240, backupCount=10
            )
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
            ))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
            app.logger.setLevel(logging.INFO)
            app.logger.info('Mini-GGmap startup')

# Configuration mapping
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(config_name=None):
    """Get configuration class by name"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    return config.get(config_name, config['default'])