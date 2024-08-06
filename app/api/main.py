from fastapi import FastAPI


def create_app() -> FastAPI:
	app = FastAPI(
		title='test case from metro',
		docs_url='/api/docs',
		description='test case from metro',
		debug=True,
	)
	app.include_router()

	return app
