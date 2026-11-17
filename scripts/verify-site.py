"""Delegate unit verification to the shared implementation."""
from pathlib import Path
import json,sys,runpy,os
root=Path(__file__).resolve().parents[1]
config=json.loads((root/'shared.config.json').read_text())
shared=Path(os.environ['SHARED_SOURCE']).resolve() if os.environ.get('SHARED_SOURCE') else (root/config['localPath']).resolve()
sys.argv=[str(shared/'scripts/unit-site/verify-content.py'),str(root),*sys.argv[1:]]
runpy.run_path(sys.argv[0],run_name='__main__')
