# Store Project

## Configuration
### Redis service launches
```sudo service redis-server start```

### Launches Celery
```celery -A store worker --loglevel=info -P eventlet```

### Listening to Stripe events
```stripe listen --forward-to localhost:8000/webhook/stripe/```