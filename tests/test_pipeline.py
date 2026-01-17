from app import pipeline


def test_pipeline_runs():
    out = pipeline.run_pipeline('a\n\n b\n')
    assert isinstance(out, list)

