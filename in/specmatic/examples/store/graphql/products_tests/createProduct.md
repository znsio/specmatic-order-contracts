# Create a new product

Request

```graphql
mutation {
    createProduct(newProduct: {
        name: "The Almanac",
        inventory: 10,
        type: book
    }) { id name inventory type }
}
```

Response

```json
{
  "id": 10,
  "name": "The Almanac",
  "inventory": 10,
  "type": "book"
}
```
