### Suspicious Outbound Connection
```index=main sourcetype="reverse_shell"
| table src_ip, src_port, dest_ip, dest_port, protocol, bytes_sent, bytes_recv
| where protocol="tcp" AND NOT (dest_port IN (80,443,22,53,25,21))
```
### Data Exfilteration Volume
```index=main sourcetype="reverse_shell"
| where bytes_sent!="-" AND NOT match(src_ip, "^fe80")
| table src_ip, bytes_sent
```

### High-Duration Connections
```index=main sourcetype="reverse_shell"
| where protocol="tcp" AND duration > 10 AND (dest_port!=9997 AND dest_port!=443)
| table src_ip, dest_ip, dest_port, duration, bytes_sent
| sort - duration
```