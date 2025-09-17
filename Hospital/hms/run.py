from app.routes import application

if __name__ == "__main__":
    # Run Flask app
   application.run(host="0.0.0.0", port=5001, debug=True)
