# Find offers for date

Request

```graphql
query {
    findOffersForDate(date: "2024/12/31") { offerCode, validUntil }
}
```

Response

```json
[
  {
    "offerCode": "WKND30",
    "validUntil": "2024/12/12"
  },
  {
    "offerCode": "SUNDAY20",
    "validUntil": "2024/12/25"
  }
]
```
