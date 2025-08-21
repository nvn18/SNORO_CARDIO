import tempfile
from snoro.core import SNORO

def test_run_from_path_basic(tmp_path):
    p = tmp_path / "sample.txt"
    p.write_text("one two three\none two\n")
    s = SNORO()
    stats = s.run_from_path(str(p))
    assert stats["processed_lines"] == 2
    assert stats["processed_words"] == 5
    assert stats["errors"] == 0
    assert stats["unique_tokens"] >= 3
    ol = SNORO.one_line_output(stats)
    assert "processed_lines=2" in ol
