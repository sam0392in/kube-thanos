import os
import shutil
import time
import logging


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
        datefmt='%Y-%m-%dT%H:%M:%S%z'
    )


def clean_old_directories(directory, days_to_keep):
    total_chunks_cleaned = 0
    current_time = time.time()
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        if not os.path.isdir(entry_path):
            continue
        creation_time = os.path.getctime(entry_path)
        age_in_days = (current_time - creation_time) / (24 * 3600)
        if age_in_days > days_to_keep:
            logging.info(f"Found chunks older than %s days", days_to_keep)
            logging.info(f"Deleting directory: {entry_path}")
            shutil.rmtree(entry_path)
            total_chunks_cleaned += 1
    return total_chunks_cleaned


def main():
    configure_logging()

    path = os.getenv('THANOS_DATA_DIR', '/var/thanos/store')
    frequency = int(os.getenv('CLEANUP_FREQUENCY', '24'))
    retention = int(os.getenv('RETENTION_PERIOD', '90'))

    logging.info("Starting thanos store garbage collector")
    logging.info("frequency: %s hours", frequency)
    logging.info("retention period: %s days", retention)
    logging.info("Data Path: %s", path)

    logging.info("Initiating initial cleanup on server startup")
    chunks_cleaned = clean_old_directories(path, retention)
    logging.info("Initial chunks cleaned: %s", chunks_cleaned)
    while True:
        logging.info("Initiating scheduled cleanup")
        time.sleep(frequency * 3600)
        chunks_cleaned = clean_old_directories(path, retention)
        logging.info("total chunks cleaned: %s", chunks_cleaned)


if __name__ == "__main__":
    main()
