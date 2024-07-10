from app import create_app
app = create_app('dev')


@app.errorhandler(404)
def page_not_found(e):
    return '404 Not Found!💣💣', 404


if __name__ == '__main__':
    app.run(host=app.config.get('FLASK_RUN_HOST'),
            port=app.config.get('FLASK_RUN_PORT'))
