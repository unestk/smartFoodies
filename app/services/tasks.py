from worker import celery

@celery.task
def process_data(data):
    return {"status": "processed", "data": data}
