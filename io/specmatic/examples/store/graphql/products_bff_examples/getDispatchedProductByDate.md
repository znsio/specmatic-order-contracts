# Get dispatched product by date

Request

```graphql
query {
    getDispatchedProductByDate(date: "2020/12/12") { id, dispatchDate }
}
```

Response

```json
{
  "id": "100",
  "dispatchDate": "2020/12/12"
}
```
