# Central Contract Repository for the Order API

This repository stores the contracts for the [Order UI](http://github.com/znsio/specmatic-order-ui) client project and the [Order API](http://github.com/znsio/specmatic-order-api).

The [api_order_v1.yaml](https://github.com/znsio/specmatic-order-contracts/blob/main/in/specmatic/examples/store/api_order_v1.yaml) contract in this repository governs the integration of the client and API.


# Linting

* Install [spectral](https://github.com/stoplightio/spectral#-installation-and-usage)
* Run below command inside the repo
```
spectral lint **/*.yaml 
```
* Above command leverages .spectral.yaml