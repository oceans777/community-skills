import sys
import os
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from core import BM25, _build_index, _search_csv, detect_domain, search, search_stack  # noqa: E402


class SearchBehaviorTests(unittest.TestCase):
    def test_short_ui_ux_terms_are_searchable(self):
        result = search("UI UX", domain="style")
        self.assertNotIn("error", result)
        self.assertGreater(result["count"], 0)

    def test_domain_detection_uses_token_boundaries(self):
        self.assertEqual(detect_domain("sidebar navigation"), "ux")

    def test_max_results_is_bounded_for_library_callers(self):
        self.assertIn("error", search("dashboard", max_results=-1))
        self.assertIn("error", search("dashboard", max_results=21))
        self.assertIn("error", search_stack("state", "react", max_results=True))

    def test_unknown_domain_does_not_silently_search_style(self):
        self.assertIn("error", search("dashboard", domain="unknown"))

    def test_empty_query_is_rejected(self):
        self.assertIn("error", search("   "))

    def test_refitting_resets_index_state(self):
        bm25 = BM25()
        bm25.fit(["alpha beta", "beta gamma"])
        bm25.fit(["delta epsilon"])
        self.assertNotIn("alpha", bm25.idf)
        self.assertEqual(bm25.N, 1)

    def test_index_is_reused_in_long_lived_processes(self):
        search("dashboard", domain="product")
        before = _build_index.cache_info().hits
        search("fintech", domain="product")
        self.assertGreater(_build_index.cache_info().hits, before)

    def test_cache_invalidates_when_csv_changes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            csv_path = Path(temp_dir) / "data.csv"
            csv_path.write_text("term,result\nalpha,old\n", encoding="utf-8")
            first = _search_csv(csv_path, ["term"], ["result"], "alpha", 1)
            self.assertEqual(first, [{"result": "old"}])

            old_mtime = csv_path.stat().st_mtime_ns
            csv_path.write_text("term,result\nbeta,new\n", encoding="utf-8")
            os.utime(csv_path, ns=(old_mtime + 1_000_000_000, old_mtime + 1_000_000_000))
            second = _search_csv(csv_path, ["term"], ["result"], "beta", 1)
            self.assertEqual(second, [{"result": "new"}])


if __name__ == "__main__":
    unittest.main()
