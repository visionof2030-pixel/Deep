services:
  - type: web
    name: educational-reports-system
    env: python
    region: frankfurt  # أو أي منطقة قريبة منك
    plan: free  # أو starter/pro للتجارة
    
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
    
    envVars:
      - key: ADMIN_TOKEN
        generateValue: true
      - key: SECRET_KEY
        generateValue: true
      - key: DATABASE_URL
        fromDatabase:
          name: reports_db
          property: connectionString
    
    autoDeploy: true
    healthCheckPath: /health
    
    disk:
      name: data
      mountPath: /data
      sizeGB: 1

databases:
  - name: reports_db
    plan: free
    databaseName: reports
    user: reports_user