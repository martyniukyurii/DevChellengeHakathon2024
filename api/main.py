# main.py
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.routes import call, category
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(call.router, prefix="/call")
app.include_router(category.router, prefix="/category")


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>API Testing Page</title>
        </head>
        <body>
            <h1>Welcome to the Audio Call Processing API</h1>
            <p>This API allows you to process and analyze audio calls.</p>
            <p>You can access the interactive API documentation at:</p>
            <ul>
                <li><a href="/docs">Swagger UI</a></li>
                <li><a href="/redoc">ReDoc</a></li>
            </ul>
            <p>Use the links above to explore and test the API endpoints.</p>
        </body>
    </html>
    """

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)


