curl -X POST http://localhost:8000/api/detect/ \
     -H "Content-Type: application/json" \
     -d '{"mac_addresses": ["AA:BB:CC:DD:EE:01", "AA:BB:CC:DD:EE:02"]}'
