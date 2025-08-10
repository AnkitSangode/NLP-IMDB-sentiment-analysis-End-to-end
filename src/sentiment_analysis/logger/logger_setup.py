import logging
import os
from datetime import datetime

# Generate log file path
LOG_FILE = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ✅ Create and export the logger object
logger = logging.getLogger("sentiment-analysis")
