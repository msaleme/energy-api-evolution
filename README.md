# Energy API Evolution

A reference architecture for exposing grid modeling, energy management, and renewable-energy optimization capabilities through consistent enterprise APIs.

> **Project status:** Architecture and API-design reference. Documentation and integration scaffolding are intended for evaluation and extension. Performance, compliance, and operational benefits are design objectives unless accompanied by reproducible evidence.

## Purpose

Energy planning and operations commonly depend on specialized tools with different data models and interaction patterns. This project explores how an API-led architecture can create stable boundaries around three open-source ecosystems:

- [dsgrid](https://github.com/dsgrid/dsgrid) for demand-side grid modeling;
- [OpenEMS](https://github.com/OpenEMS/openems) for energy management and device control;
- [REopt](https://github.com/NREL/REopt_API) for renewable-energy and resilience optimization.

The repository does not replace or redistribute those projects. It documents integration contracts and orchestration patterns around them. Review and honor each upstream project's license before reuse.

## Architecture

| Layer | Responsibility | Examples |
|---|---|---|
| System APIs | Stable access to tools and data sources | Weather, building stock, tariffs, devices, loads and incentives |
| Process APIs | Cross-domain logic | Load profiles, scenarios, optimization, resilience and anomaly analysis |
| Experience APIs | Consumer-oriented interfaces | Grid modeling exports, policy analysis, dashboards and consultant workflows |

## Utility capabilities

- demand and load modeling;
- distributed energy-resource integration;
- device and energy-management interoperability;
- resilience and renewable-energy analysis;
- reusable canonical contracts;
- policy-controlled access and observable orchestration.

## What's actually included

This repository is documentation and integration scaffolding, not a running platform. The artifacts present are:

- `docs/api-catalog.md` — a catalog of the API surface proposed across dsgrid, OpenEMS, and REopt. This is a design-level reference; no endpoints are deployed or implemented in this repository.
- `docs/architecture.md` — API-led layering, integration patterns, data/eventing choices, and security considerations.
- `examples/dsgrid-integration/load-profile-example.py` — a single illustrative Python client showing how a dsgrid load-profile request would be made against the proposed API.
- `docker-compose.yml` — a local development scaffold that wires infrastructure images (Kong, Postgres, Redis, Kafka/ZooKeeper, InfluxDB, Prometheus, Grafana) plus placeholder service entries. The application services referenced are not implemented in this repository.
- `.env.example` — sample environment configuration for that scaffold.
- `CONTRIBUTING.md` and `LICENSE`.

No API specification files (OpenAPI/RAML), server source code, or test suite are included. The endpoints, response times, and capacities described in the catalog and architecture documents are design targets, not measured behavior.

## Evidence and limitations

This repository should be evaluated as a reference design. Claims such as sub-second response, utility-scale throughput, NERC CIP compliance, or quantified savings require environment-specific testing and governance review. Security patterns can support a compliance program but do not provide certification.

## Documentation

- [API catalog](docs/api-catalog.md) — the proposed API surface across the three ecosystems (design-level)
- [Architecture](docs/architecture.md) — API-led layering, integration patterns, and security considerations

## Portfolio context

This repository is part of a broader [utility grid-modernization portfolio](https://github.com/msaleme/utility-ai-mulesoft-api/blob/master/docs/portfolio-guide.md) covering grid intelligence, field operations, smart meters, customer programs, compliance, and governed AI-assisted operations.


## Related projects

- [Utility AI Semantic Layer](https://github.com/msaleme/utility-ai-mulesoft-api)
- [Utility Compliance Management](https://github.com/msaleme/Utilities-Compliance-Management)
- [Utility Field Operations Agent](https://github.com/msaleme/field-operations-support-agent)

## License

See [LICENSE](LICENSE). Upstream components retain their respective licenses.
