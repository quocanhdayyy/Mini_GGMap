"""
Mini Google Maps - Main Application
=====================================

Ứng dụng tìm đường tối ưu trên bản đồ với nhiều thuật toán khác nhau.
Dự án được thiết kế để phát triển theo team với các module độc lập.

Author: Team Mini-GGmap
Version: 1.0.0
"""

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
    from app.config import get_config
    app.config.from_object(get_config(config_name))
    
    # Initialize extensions (database, cache, etc.)
    from app.extensions import init_extensions
    init_extensions(app)
    
    # Register blueprints
    from app.routes import register_blueprints
    register_blueprints(app)
    
    # Setup error handlers
    from app.utils.error_handlers import setup_error_handlers
    setup_error_handlers(app)
    
    return app

if __name__ == '__main__':
    # Environment variables for easy configuration
    config_name = os.environ.get('FLASK_ENV', 'development')
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'true').lower() == 'true'
    
    app = create_app(config_name)
    
    print(f"🚀 Mini-GGmap starting...")
    print(f"📍 Environment: {config_name}")
    print(f"🌐 URL: http://{host}:{port}")
    
    app.run(host=host, port=port, debug=debug, use_reloader=False)
