import logging
import logging.config
from datetime import datetime

import yaml
from pytz import timezone, utc


def init_log(config_file_path: str):
    def custom_time(*args):
        utc_dt = utc.localize(datetime.utcnow())
        my_tz = timezone("Asia/Taipei")
        converted = utc_dt.astimezone(my_tz)
        return converted.timetuple()


    with open(config_file_path, "r") as f:
        try:
            logging_config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print("Error when loading logger config: ", e)

    # Load Logging configs
    logging.config.dictConfig(logging_config)

    # Get logger for the module
    logger = logging.getLogger(__name__)

    # Convert timezone
    logging.Formatter.converter = custom_time

    # Start logging
    logger.info("Start logging ...")
