# Mossarium Memory System

## Introduction

The memory system in Mossarium provides a structured way for AI agents to store and retrieve information about project context, decisions, and history.

## Memory Types

### Project Memory
Stores information about ongoing work, goals, initiatives, bugs, or incidents within the project.

### User Memory
Contains information about the user's role, goals, responsibilities, and knowledge.

### Feedback Memory
Guidance the user has given about how to approach work - both what to avoid and what to keep doing.

### Reference Memory
Stores pointers to where information can be found in external systems.

## Memory Management

### Storing Memory
Memory should be stored in the `.mossarium/memory/` directory with appropriate file naming conventions.

### Retrieving Memory
AI agents should be able to access memory files when making decisions about code changes.

## Memory Lifecycle

1. **Creation** - New memories are created during project development
2. **Usage** - Memories are accessed and referenced during AI agent operations
3. **Update** - Memories are updated as project knowledge evolves
4. **Archiving** - Obsolete or outdated memories are archived appropriately

## Best Practices

- Keep memory content specific and actionable
- Update memories regularly to reflect current project state
- Use clear, descriptive file names for easy identification
- Maintain consistency in memory structure and format