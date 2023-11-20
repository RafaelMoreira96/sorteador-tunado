from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

class Routers:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
        )
    
    def operations_routers(self):
        @self.app.post("/register_participant")
        def register_participant():
            return {'message': 'I need you'}
        
        @self.app.get("/login")
        def login():
            return {'message': 'I need you, baby'}
