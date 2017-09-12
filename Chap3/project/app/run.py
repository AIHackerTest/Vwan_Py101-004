from init import create_app

app = create_app("DEVELOPMENT")

if __name__ == "__main__":
    print(app)
    app.run()
