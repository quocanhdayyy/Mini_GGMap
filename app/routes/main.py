"""
Main Routes
===========

Routes chính cho việc hiển thị bản đồ và giao diện người dùng
"""

from flask import Blueprint, render_template, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Trang chủ - hiển thị bản đồ chính
    
    TODO: 
    - Load map configuration từ config
    - Load danh sách vehicles và algorithms available
    """
    
    config = {
        'map_center': current_app.config['DEFAULT_MAP_CENTER'],
        'zoom': current_app.config['DEFAULT_ZOOM'],
        'vehicles': current_app.config['SUPPORTED_VEHICLES'],
        'algorithms': current_app.config['SUPPORTED_ALGORITHMS']
    }
    
    return render_template('index.html', config=config)

@main_bp.route('/about')
def about():
    """
    Trang thông tin về project
    
    TODO: Viết nội dung about page
    """
    return render_template('about.html')

@main_bp.route('/help')
def help():
    """
    Trang hướng dẫn sử dụng
    
    TODO: Viết documentation cho user
    """
    return render_template('help.html')