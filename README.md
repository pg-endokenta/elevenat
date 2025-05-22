# elevenat

requirements.txtへ書き出し

```bash
uv pip compile pyproject.toml -o requirements.txt
```


## MACアドレスを送信する際の形式

```bash
curl -X POST http://localhost:8000/api/detect/ \
     -H "X-API-Key: xxxxx" \
     -H "Content-Type: application/json" \
     -d '{"mac_addresses": ["AA:BB:CC:DD:EE:01", "AA:BB:CC:DD:EE:02"]}'
```