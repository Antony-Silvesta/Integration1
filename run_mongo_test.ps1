# Set the MongoDB URI for connecting to the database
$env:MONGO_URI = "mongodb://localhost:27017"
Write-Host "MongoDB URI set to $env:MONGO_URI"

# Define the path to the script
$scriptPath = "C:\Users\shinba\Integration1"

# Step 1: Check if MongoDB is running
$mongoRunning = Get-Process -Name "mongod" -ErrorAction SilentlyContinue

if ($mongoRunning -eq $null) {
    Write-Host "MongoDB is not running. Starting MongoDB..."
    # Start MongoDB locally if it's not running
    Start-Process "C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --ArgumentList "--dbpath=C:\data\db" -NoNewWindow
    Start-Sleep -Seconds 5
} else {
    Write-Host "MongoDB is already running."
}

# Step 2: Run python app/seed.py to seed MongoDB
Write-Host "Running python app/seed.py to seed MongoDB..."
python "$scriptPath\app\seed.py"

# Step 3: Run the test script to list entries with app/app.py
Write-Host "Running python app/app.py to test listing entries..."
python "$scriptPath\app\app.py"

Write-Host "MongoDB seeding and testing completed."

# Optionally, stop MongoDB if it was started by this script
# Uncomment the following lines if you want to stop the MongoDB instance after tests
# Get-Process -Name "mongod" | Stop-Process
# Write-Host "Stopping MongoDB..."
