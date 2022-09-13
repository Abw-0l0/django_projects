from celery import shared_task

@shared_task(bind=True)
def test_func(Self):
    for i in range(10):
        print(i)
    return 'Done'