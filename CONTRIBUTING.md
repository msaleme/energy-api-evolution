# Contributing to Energy API Evolution Platform

First off, thank you for considering contributing to the Energy API Evolution Platform! It's people like you that make this platform a great tool for advancing the energy transition.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to conduct@energyapi.io.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and expected**
- **Include logs and screenshots if relevant**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the proposed enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other platforms**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Write a clear commit message

## Development Process

### Setting Up Your Environment

```bash
# Clone your fork
git clone https://github.com/your-username/energy-api-evolution.git
cd energy-api-evolution

# Add upstream remote
git remote add upstream https://github.com/original/energy-api-evolution.git

# Install dependencies
docker-compose up -d
```

### API Development Guidelines

#### System APIs
- Focus on data access and abstraction
- Keep business logic minimal
- Ensure idempotency
- Document all endpoints

#### Process APIs
- Implement reusable business logic
- Keep stateless where possible
- Use appropriate caching
- Handle errors gracefully

#### Experience APIs
- Optimize for specific use cases
- Aggregate data efficiently
- Provide clear error messages
- Include usage examples

### Testing

```bash
# Run all tests
npm test

# Run specific test suite
npm test -- --grep "Weather API"

# Run with coverage
npm run test:coverage
```

### Code Style

- **JavaScript/TypeScript**: Use ESLint with our config
- **Python**: Follow PEP 8
- **Java**: Use Google Java Style Guide
- **API Design**: Follow RESTful principles

### Documentation

- Update API documentation for any endpoint changes
- Include code examples
- Document any new environment variables
- Update architecture diagrams if needed

## Project Structure

```
energy-api-evolution/
├── services/          # Microservices
│   ├── system/       # System APIs
│   ├── process/      # Process APIs
│   └── experience/   # Experience APIs
├── docs/             # Documentation
├── tests/            # Test suites
├── kubernetes/       # K8s manifests
└── monitoring/       # Monitoring configs
```

## Commit Message Guidelines

We follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes
- `refactor:` Code refactoring
- `perf:` Performance improvements
- `test:` Test additions/changes
- `chore:` Build process/auxiliary changes

Example:
```
feat: add real-time pricing to Energy Optimization API

- Implement WebSocket endpoint for price updates
- Add price forecasting using ML model
- Include test coverage for new endpoints
```

## API Versioning

- Use semantic versioning
- Maintain backward compatibility
- Deprecate features with notice
- Document breaking changes

## Review Process

1. All submissions require review
2. Core maintainers will review PRs
3. Address review feedback
4. Maintain professional communication

## Community

- Join our [Discord server](https://discord.gg/energyapi)
- Subscribe to our [mailing list](https://groups.google.com/g/energy-api-evolution)
- Follow us on [Twitter](https://twitter.com/energyapi)

## Recognition

Contributors will be recognized in:
- The project README
- Release notes
- Our website

Thank you for contributing to a cleaner energy future! 🌍⚡