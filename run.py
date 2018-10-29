"""
   A file for running the server
"""
from storeapi import create_app

if __name__ == "__main__": 
    app = create_app('development')
    app.run()
    
