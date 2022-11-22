# Central Contract Repository for the Order API

## What is Central Contract Repository? [Documentation Link](https://specmatic.in/documentation/central_contract_repository.html)

---

This repository serves as the Central Contract Repository for the API Specifications / Contracts the govern interactions between below applications
* [Order UI](http://github.com/znsio/specmatic-order-ui) - consumer / client
* [Order API](http://github.com/znsio/specmatic-order-api) - provider / service / API

## Backward Compatibility Testing

To verify [backward compatibility](https://specmatic.in/#backward-compatibility) between API Specifications in your branch and the main branch on your local machine run below command.

```shell
ls **/*.yaml | xargs ./backward_compatibility.sh
echo $?
```

The ```echo $?``` for Specmatic behaves like any other command line tool returning "0" for success and "1" for failure.

## Linting

Below are the instructions to run the linter on your local machine

* Install [spectral](https://github.com/stoplightio/spectral#-installation-and-usage)
* Run below command inside the repo
```
spectral lint **/*.yaml 
```
* Above command leverages .spectral.yaml
