from waitress import serve
from parent import create_app
import os
env=os.environ.get('ENV')


if env != "production":
	app=serve(create_app(),host="0.0.0.0",port=8000)
else:
    app=create_app()
    app.run(debug=True)