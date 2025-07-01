from app import create_app

app = create_app()


@app.route('/api/demo')
def demo():
    return "Backend is running!"

if __name__ == "__main__":
    app.run(debug=True)