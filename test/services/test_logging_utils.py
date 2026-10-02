import io

from app.utils.logging_utils import _prepare_text_stream_for_unicode


def test_prepare_text_stream_for_unicode_upgrades_cp1252_stream():
    raw = io.BytesIO()
    stream = io.TextIOWrapper(raw, encoding="cp1252", errors="strict")

    result = _prepare_text_stream_for_unicode(stream)

    assert result is stream
    assert stream.encoding.lower().replace("_", "-") == "utf-8"
    assert stream.errors == "backslashreplace"

    stream.write("① non‑breaking 漢字")
    stream.flush()
    assert raw.getvalue().decode("utf-8") == "① non‑breaking 漢字"


def test_prepare_text_stream_for_unicode_leaves_non_stream_sink_unchanged():
    sink = []
    assert _prepare_text_stream_for_unicode(sink) is sink
