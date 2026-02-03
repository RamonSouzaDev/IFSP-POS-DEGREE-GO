@echo off
echo [EcoCompute] Starting the Green Software Environment... 🌿

:: Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo [Error] Docker is not running. Please start Docker Desktop.
    pause
    exit /b
)

:: Build and Run
echo [EcoCompute] Building and Starting Containers...
docker-compose up --build -d

echo.
echo [EcoCompute] API is running at http://localhost:8000/docs
echo [EcoCompute] Use 'docker-compose down' to stop.
pause
