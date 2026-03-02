# Humanitarian Proof Infrastructure (HPI) 

[![Python Tests](https://github.com/AbidHossen-CS/hpi-core/actions/workflows/python-tests.yml/badge.svg)](https://github.com/AbidHossen-CS/hpi-core/actions/workflows/python-tests.yml)
![License](https://img.shields.io/badge/License-AGPLv3-blue.svg)

HPI is an open-source, trust-minimized framework designed to secure global aid delivery. By replacing narrative-based reporting with a **Proof-of-Impact (POI) engine**, HPI ensures that humanitarian resources are cryptographically verifiable from the field to the funder.

---

## Core Feature: Proof-of-Impact (POI) Engine

The heart of HPI is the **POI Engine** (located in `/src`). It addresses the "Byzantine Oracle" problem—ensuring real-world events are accurately recorded in a digital system without relying on a single source of truth.

### Key Capabilities:
* **Multi-Party Attestation:** Requires $n$ signatures (e.g., Worker + Community Witness) to transition a claim into a "Verified Proof."
* **Spatio-Temporal Anchoring:** Uses location and time data to create unique, tamper-evident event hashes.
* **Byzantine Fault Tolerance (BFT):** Designed to resist collusion between field actors.

---

## Technical Architecture

HPI follows a modular, "Privacy-First" design:

* **`/src`**: Contains the core Python logic for proof generation and validation.
* **`/tests`**: A comprehensive unit testing suite ensuring logic integrity.
* **`/docs`**: Formal technical specifications and cryptographic research.



---

## Getting Started

### Installation
Clone the repository:
```bash
git clone [https://github.com/AbidHossen-CS/hpi-core.git](https://github.com/AbidHossen-CS/hpi-core.git)
cd hpi-core
