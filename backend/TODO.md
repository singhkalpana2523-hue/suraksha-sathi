- [x] Locate FastAPI entrypoint (created backend/app/main.py placeholder)

- [x] Update backend/requirements.txt with MongoDB + env support dependencies

- [x] Create backend/.env template for MongoDB

- [x] Installed required packages (pymongo, python-dotenv)

- [x] Create app/database/mongodb.py for MongoDB users collection access

- [x] Create app/schemas/auth_schema.py with SignupRequest validations

- [x] Create app/models/user.py for user document schema

- [x] Create app/services/auth_service.py signup logic + duplicate phone check

- [x] Create app/routes/auth.py POST /auth/signup endpoint

- [x] Register auth router in FastAPI entrypoint (include_router)

- [ ] Run FastAPI and manually test POST /auth/signup in Swagger

- [ ] Verify MongoDB users collection document format and duplicate behavior

