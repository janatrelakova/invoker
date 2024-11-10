# Invoker

This tool is a part of `microshift` inicitiave. Invoker pings all defined endpoints to create a artificial load. Microshift scraper for spring project can generate similar output to be used by Invoker (pressuming your Spring project is using `@GetMapping`, `@RequestMapping`, `@RequestBody` and similar annotations). However, feel free to use this tool for any HTTP-based project.

:warning: Links to be added.

Run `invoker.py <path-to-endpoints-definition> <host>`.
Example: `invoker.py endpoints.example.yml http://localhost:8080`.

File for endpoints should have following structure:
```
endpoints:
  - url: "/user/1"
    httpMethod: "GET"
    body: null
    formBody: null
```

and accepts following properties for an item of `endpoints` array:
- `url`* is joined with `host`
- `httpMethod`*: GET, POST, PUT, PATCH, DELETE
- `body`: array of key-value
   ```
    body:
    - "price: 123"
    - "name: Jane Doe"
    - "id: 1"
    ```
- `timeout` TBD
- `times` TBD

*(Required)

:warning: Tested on Spring project with `@<Get, Post, Put, Patch, Delete>Mapping`, `@RequestMapping`, `@RequestBody`, `@PathVariable`, Java 22.