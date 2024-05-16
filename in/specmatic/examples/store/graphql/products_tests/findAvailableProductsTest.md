# Find Available Products

Request

```graphql
query {
    findAvailableProducts(type: gadget, pageSize: 10) { id name inventory type }
}
```
Response

```json
[
  {
    "id": 10,
    "name": "The Almanac",
    "inventory": 10,
    "type": "book"
  },
  {
    "id": 20,
    "name": "iPhone",
    "inventory": 15,
    "type": "gadget"
  }
]
```
