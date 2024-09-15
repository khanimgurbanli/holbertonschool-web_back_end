# Holberton Task - SQL Operations and Procedures

![copy-repo-link](../images/holberton_logo.jpg)

## Description

# SQL Operations and Procedures

This project involves SQL operations to manage indices and stored procedures for optimizing queries and calculating
average scores. This README will guide you through the setup and usage of the provided SQL scripts.

## Table of Contents

- [Index Creation](#index-creation)
- [Stored Procedures](#stored-procedures)
- [Usage](#usage)
- [License](#license)

## Index Creation

To optimize the performance of queries on the `names` table, two indices are created:

1. **Index on `name(1)` and `score`:**
   ```sql
   CREATE INDEX idx_name_first_score
   ON names (name(1), score);
