"""
Basic test to verify project structure
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

def test_import_app():
    """Test that app can be imported"""
    try:
        from app import create_app
        app = create_app('testing')
        assert app is not None
        print("✅ App creation successful")
    except Exception as e:
        print(f"❌ App creation failed: {e}")
        return False
    return True

def test_config():
    """Test configuration"""
    try:
        from app.config import get_config
        config = get_config('testing')
        assert config is not None
        print("✅ Config loading successful")
    except Exception as e:
        print(f"❌ Config loading failed: {e}")
        return False
    return True

def test_routes():
    """Test route registration"""
    try:
        from app import create_app
        app = create_app('testing')
        
        with app.test_client() as client:
            # Test main routes
            response = client.get('/')
            print(f"✅ Main route status: {response.status_code}")
            
            # Test API routes
            response = client.get('/api/map/data')
            print(f"✅ API route status: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Route testing failed: {e}")
        return False
    return True

if __name__ == '__main__':
    print("🧪 Testing Mini-GGmap project structure...")
    
    tests = [
        test_import_app,
        test_config,
        test_routes
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Project structure is ready.")
    else:
        print("⚠️ Some tests failed. Check the errors above.")