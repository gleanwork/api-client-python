# Glean SDK

## Overview

Glean API: # Introduction
In addition to the data sources that Glean has built-in support for, Glean also provides a REST API that enables customers to put arbitrary content in the search index. This is useful, for example, for doing permissions-aware search over content in internal tools that reside on-prem as well as for searching over applications that Glean does not currently support first class. In addition these APIs allow the customer to push organization data (people info, organization structure etc) into Glean.

# Usage guidelines
This API is evolving fast. Glean will provide advance notice of any planned backwards incompatible changes along
with a 6-month sunset period for anything that requires developers to adopt the new versions.

# API Clients
Official API clients for the Glean Indexing API are available in multiple languages:

- [Python](https://github.com/gleanwork/api-client-python)
- [TypeScript](https://github.com/gleanwork/api-client-typescript)
- [Go](https://github.com/gleanwork/api-client-go)
- [Java](https://github.com/gleanwork/api-client-java)

These API clients provide type-safe, idiomatic interfaces for working with Glean IndexingAPIs in your language of choice.


### Available Operations
