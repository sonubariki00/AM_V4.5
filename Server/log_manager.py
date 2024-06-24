import logging

class LogManager:
    def __init__(self):
        logging.basicConfig(filename='app.log', level=logging.INFO, 
                format='%(asctime)s - %(levelname)s - %(message)s')
    
    def add_log(self, level, component, message, admin_id=None):
        log_message = f"[{component}] {message}"
        if admin_id:
            log_message += f" | Admin ID: {admin_id}"
        if level == 'INFO':
            logging.info(log_message)
        elif level == 'WARNING':
            logging.warning(log_message)
        elif level == 'ERROR':
            logging.error(log_message)
        else:
            logging.debug(log_message)
