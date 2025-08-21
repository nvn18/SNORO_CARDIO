#!/usr/bin/env python3
import argparse
import logging
import sys
import yaml
from .core import SNORO

LOG_FMT = "%(asctime)s %(levelname)s %(name)s: %(message)s"

def load_config(path: str):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return yaml.safe_load(fh) or {}
    except FileNotFoundError:
        logging.getLogger(__name__).warning("Config file not found: %s (using defaults)", path)
        return {}
    except Exception:
        logging.getLogger(__name__).exception("Failed to load config, using defaults")
        return {}

def parse_args(argv=None):
    p = argparse.ArgumentParser(prog="snoro", description="SNORO simple processor")
    p.add_argument("--input", "-i", required=True, help="Input text file path")
    p.add_argument("--output", "-o", help="Write detailed JSON output to path")
    p.add_argument("--config", "-c", default="configs/default.yaml", help="Config YAML path")
    p.add_argument("--one-line", action="store_true", help="Print compact one-line output only")
    p.add_argument("--verbose", "-v", action="count", default=0, help="Increase verbosity (repeat for more)")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)

    level = logging.WARNING
    if args.verbose == 1:
        level = logging.INFO
    elif args.verbose >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level, format=LOG_FMT)

    config = load_config(args.config)
    sn = SNORO(config=config)
    try:
        stats = sn.run_from_path(args.input)
    except Exception as e:
        logging.getLogger(__name__).error("Processing failed: %s", e)
        sys.exit(2)

    if args.one_line:
        print(SNORO.one_line_output(stats))
        return 0

    import json
    print("=== SNORO Detailed Report ===")
    print(json.dumps(stats, indent=2))
    if args.output:
        try:
            with open(args.output, "w", encoding="utf-8") as fh:
                json.dump(stats, fh, indent=2)
        except Exception:
            logging.getLogger(__name__).exception("Failed to write output file %s", args.output)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
