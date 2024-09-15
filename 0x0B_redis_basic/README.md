# Redis Cache Module

This Python module provides a simple caching mechanism using Redis. It supports storing and retrieving data with various
utilities to track method calls and manage function history. The module includes decorators for counting method calls
and storing call histories, as well as methods for interacting with a Redis cache.

## Features

- **Method Call Counting**: Decorator to count the number of times a method is called.
- **Call History**: Decorator to store and retrieve the history of inputs and outputs of a method.
- **Cache Storage**: Store data in Redis and retrieve it with optional data transformation.
- **Replay Function History**: Display the history of calls for a particular function.

## Installation

To use this module, you need to have Redis installed and running on your machine. You can install Redis using the
following instructions:

- **For macOS**: Use Homebrew: `brew install redis`
- **For Ubuntu**: Use APT: `sudo apt-get install redis-server`
- **For Windows**: Follow instructions on the [Redis website](https://redis.io/download).

Install the required Python packages using pip:

```bash
pip install redis
