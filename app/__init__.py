"""
App package initialization
"""

from .config import get_config
from .extensions import init_extensions
from .routes import register_blueprints
from .utils.error_handlers import setup_error_handlers

import os
import sys
from flask import Flask

# Ensure UTF-8 encoding for Vietnamese text on Windows
if os.name == 'nt':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def create_app(config_name='development'):
    """
    Application Factory Pattern
    
    Args:
        config_name (str): Configuration environment ('development', 'testing', 'production')
    
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions (database, cache, etc.)
    init_extensions(app)
    
    # Register blueprints
    register_blueprints(app)
    
    # Setup error handlers
    setup_error_handlers(app)
    
    return app