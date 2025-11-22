# Clean Architecture Instructions

## Core Concept

Center the system on business rules. Keep them independent of frameworks, databases, and UI concerns. Treat these rules as the most stable part of the system.

## Dependency Rule

All dependencies must flow inward.

* Inner layers must not reference outer layers.
* Inner layers must not import anything from outer layers.

## Layers (Innermost → Outermost)

1. **Entities**
   Core business objects and rules. Contain no infrastructure or framework code.

2. **Use Cases**
   Application-specific business logic. Coordinate interactions between entities and external boundaries.

3. **Interface Adapters**
   Translate data between the formats needed by the core and those used by external systems. Includes controllers, presenters, and ORM models.

4. **Frameworks & Drivers**
   External tools such as web frameworks, databases, and CLIs.

## Python Implementation

* Organize directories by layer:
  - `core/` (entities, use cases), 
  - `adapters/` (controllers, repositories, presenters), 
  - `infrastructure/` (frameworks, API's, database setups).
* Define abstract interfaces in the inner layers, such as repository ABCs.
* Implement those interfaces in the outer layers.
* Apply dependency injection so use cases receive concrete implementations without coupling to infrastructure.
