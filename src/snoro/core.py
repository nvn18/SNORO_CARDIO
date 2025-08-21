import time
import logging
from collections import Counter
from typing import Dict, Any, Iterable

logger = logging.getLogger(__name__)

class SNORO:
    """
    Simple processor example:
      - counts lines
      - counts words
      - counts unique tokens and top tokens
    """

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.batch_size = int(self.config.get("performance", {}).get("batch_size", 1000))
        self.threads = int(self.config.get("performance", {}).get("threads", 1))
        logger.debug("SNORO initialized with config: %s", self.config)

    def _tokenize(self, line: str) -> Iterable[str]:
        return (tok.strip() for tok in line.lower().split())

    def run_from_path(self, path: str) -> Dict[str, Any]:
        start = time.time()
        line_count = 0
        word_count = 0
        token_counter = Counter()
        errors = 0

        try:
            with open(path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line_count += 1
                    try:
                        tokens = list(self._tokenize(line))
                        word_count += len(tokens)
                        token_counter.update(tokens)
                    except Exception:
                        errors += 1
                        logger.exception("Failed processing line %d", line_count)
        except FileNotFoundError:
            logger.exception("Input file not found: %s", path)
            raise

        elapsed = time.time() - start
        top_tokens = token_counter.most_common(10)

        result = {
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "processed_lines": line_count,
            "processed_words": word_count,
            "unique_tokens": len(token_counter),
            "top_tokens": top_tokens,
            "errors": errors,
            "time_s": round(elapsed, 6),
        }
        return result

    @staticmethod
    def one_line_output(stats: Dict[str, Any]) -> str:
        status = "OK" if stats.get("errors", 0) == 0 else "ERR"
        return (
            f"{stats.get('timestamp')} | {status} | "
            f"processed_lines={stats.get('processed_lines')}; "
            f"processed_words={stats.get('processed_words')}; "
            f"errors={stats.get('errors')}; "
            f"time={stats.get('time_s')}s; "
            f"unique_tokens={stats.get('unique_tokens')}"
        )
