from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .utils import update_inapp_posts

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="task_update_inapp_posts",
    ignore_result=True
)
def task_update_inapp_posts():

    update_inapp_posts()
    logger.info("Updated posts from inapp")