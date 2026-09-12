# llm-trace-normalizer

Normalize trace events into a stable event shape for local comparison and test fixtures.

The normalizer preserves timestamp, kind, name, status, and input order for timestamp ties.

```bash
python -m unittest -v
```

MIT licensed.