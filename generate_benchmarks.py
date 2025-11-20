#!/usr/bin/env python3
"""
Generate benchmark parquet files for MCPT analysis.
Creates benchmark files for different time horizons (4H, 8H, 24H, 48H)
with all/positive/negative variants.
"""

import pandas as pd
import numpy as np
import os

def generate_benchmark_data(num_rows=100000, seed=42):
    """
    Generate benchmark data with typical financial/trading features.
    
    Args:
        num_rows: Number of rows to generate
        seed: Random seed for reproducibility
    
    Returns:
        pandas.DataFrame with benchmark data
    """
    np.random.seed(seed)
    
    # Generate typical trading/benchmark features
    data = {
        'timestamp': pd.date_range('2024-01-01', periods=num_rows, freq='1min'),
        'open': np.random.uniform(100, 200, num_rows),
        'high': np.random.uniform(100, 200, num_rows),
        'low': np.random.uniform(100, 200, num_rows),
        'close': np.random.uniform(100, 200, num_rows),
        'volume': np.random.randint(1000, 100000, num_rows),
        'returns': np.random.normal(0, 0.02, num_rows),
        'volatility': np.random.uniform(0.01, 0.05, num_rows),
        'signal': np.random.choice([-1, 0, 1], num_rows),
        'prediction': np.random.uniform(-1, 1, num_rows),
        'feature_1': np.random.normal(0, 1, num_rows),
        'feature_2': np.random.normal(0, 1, num_rows),
        'feature_3': np.random.normal(0, 1, num_rows),
        'feature_4': np.random.normal(0, 1, num_rows),
        'feature_5': np.random.normal(0, 1, num_rows),
    }
    
    df = pd.DataFrame(data)
    
    # Ensure high >= low, and both contain close
    df['high'] = df[['high', 'open', 'close', 'low']].max(axis=1)
    df['low'] = df[['high', 'open', 'close', 'low']].min(axis=1)
    
    return df

def filter_positive(df):
    """Filter for positive returns/signals."""
    return df[df['returns'] > 0].copy()

def filter_negative(df):
    """Filter for negative returns/signals."""
    return df[df['returns'] < 0].copy()

def create_benchmark_files():
    """Create all benchmark parquet files."""
    
    output_dir = 'benchmark_mcpt'
    os.makedirs(output_dir, exist_ok=True)
    
    # Time horizons and their corresponding row counts
    # Larger files need more rows to reach desired size
    horizons = {
        '4H': 2800000,   # ~291 MB target
        '8H': 2800000,   # ~291 MB target  
        '24H': 2800000,  # ~291 MB target
        '48H': 2800000,  # ~291 MB target
    }
    
    for horizon, num_rows in horizons.items():
        print(f"Generating {horizon} benchmarks...")
        
        # Generate base data
        df_all = generate_benchmark_data(num_rows, seed=hash(horizon) % 10000)
        
        # Save 'all' variant
        all_file = os.path.join(output_dir, f'bench_{horizon}_all.parquet')
        df_all.to_parquet(all_file, compression='snappy', index=False)
        file_size_mb = os.path.getsize(all_file) / (1024 * 1024)
        print(f"  Created {all_file} - {file_size_mb:.2f} MB")
        
        # Create and save 'pos' variant
        df_pos = filter_positive(df_all)
        pos_file = os.path.join(output_dir, f'bench_{horizon}_pos.parquet')
        df_pos.to_parquet(pos_file, compression='snappy', index=False)
        file_size_mb = os.path.getsize(pos_file) / (1024 * 1024)
        print(f"  Created {pos_file} - {file_size_mb:.2f} MB")
        
        # Create and save 'neg' variant
        df_neg = filter_negative(df_all)
        neg_file = os.path.join(output_dir, f'bench_{horizon}_neg.parquet')
        df_neg.to_parquet(neg_file, compression='snappy', index=False)
        file_size_mb = os.path.getsize(neg_file) / (1024 * 1024)
        print(f"  Created {neg_file} - {file_size_mb:.2f} MB")
        
        print()

if __name__ == '__main__':
    print("Generating benchmark parquet files...")
    create_benchmark_files()
    print("All benchmark files created successfully!")
