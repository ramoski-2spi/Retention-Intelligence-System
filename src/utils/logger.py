from pathlib import Path
import logging

LOG_DIR = Path("reports/logs") #gives the folder path for the logs.

LOG_DIR.mkdir(parents=True, exist_ok=True) #creates the folder if it does not exist.

LOG_FILE = LOG_DIR/"project.log" #gives the path for the file with logs.

#This is how logging behaves:
logging.basicConfig(filename=LOG_FILE,
                    format="%(asctime)s - %(levelname)s - %(message)s", 
                    level= logging.INFO) #records severity level.

logger = logging.getLogger(__name__) #gives name of the file in which the log message came from.