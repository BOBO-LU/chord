from log_utils.logger_init import init_log
import logging
init_log("./config/log_config.yaml")


logger = logging.LoggerAdapter(logging.getLogger("chord"), {"ip":"t1", "id":123 })

for i in range(0, 1):
    logger.info("test info message")
    # logger.warning("test warning message")
    # logger.error("test error message")
