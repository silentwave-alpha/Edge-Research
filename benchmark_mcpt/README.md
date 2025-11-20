# MCPT Benchmark Dataset

This directory contains benchmark parquet files for Multi-Currency Portfolio Trading (MCPT) analysis across different time horizons.

## Files

The benchmark dataset is organized by time horizon (4H, 8H, 24H, 48H) with three variants for each:

### 4-Hour Horizon
- `bench_4H_all.parquet` (293.14 MB) - Complete dataset
- `bench_4H_pos.parquet` (148.47 MB) - Positive returns only
- `bench_4H_neg.parquet` (148.62 MB) - Negative returns only

### 8-Hour Horizon
- `bench_8H_all.parquet` (293.14 MB) - Complete dataset
- `bench_8H_pos.parquet` (148.58 MB) - Positive returns only
- `bench_8H_neg.parquet` (148.51 MB) - Negative returns only

### 24-Hour Horizon
- `bench_24H_all.parquet` (293.14 MB) - Complete dataset
- `bench_24H_pos.parquet` (148.60 MB) - Positive returns only
- `bench_24H_neg.parquet` (148.50 MB) - Negative returns only

### 48-Hour Horizon
- `bench_48H_all.parquet` (293.14 MB) - Complete dataset
- `bench_48H_pos.parquet` (148.49 MB) - Positive returns only
- `bench_48H_neg.parquet` (148.60 MB) - Negative returns only

## Data Structure

Each parquet file contains the following columns:

- `timestamp`: Date and time of the observation
- `open`: Opening price
- `high`: Highest price
- `low`: Lowest price
- `close`: Closing price
- `volume`: Trading volume
- `returns`: Price returns (used for pos/neg filtering)
- `volatility`: Price volatility
- `signal`: Trading signal (-1, 0, 1)
- `prediction`: Model prediction value
- `feature_1` through `feature_5`: Additional features for analysis

## Usage

Load the benchmark data using pandas:

```python
import pandas as pd

# Load complete 4H benchmark
df_all = pd.read_parquet('benchmark_mcpt/bench_4H_all.parquet')

# Load only positive returns
df_pos = pd.read_parquet('benchmark_mcpt/bench_4H_pos.parquet')

# Load only negative returns
df_neg = pd.read_parquet('benchmark_mcpt/bench_4H_neg.parquet')
```

## Data Characteristics

- **Total rows per 'all' file**: ~2,800,000
- **Total rows per 'pos' file**: ~1,400,000
- **Total rows per 'neg' file**: ~1,400,000
- **File format**: Apache Parquet with Snappy compression
- **Git LFS**: All parquet files are tracked using Git LFS

## Generation

The benchmark files were generated using the `generate_benchmarks.py` script in the repository root. The script creates synthetic financial data with realistic characteristics for testing and benchmarking purposes.

## Note

These files are stored using Git LFS (Large File Storage) due to their size. When cloning the repository, ensure you have Git LFS installed and initialized:

```bash
git lfs install
git lfs pull
```
