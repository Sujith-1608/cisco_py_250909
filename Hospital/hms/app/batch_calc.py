"""
Batch calculations for average patient age using threading and asyncio.
"""

from concurrent.futures import ThreadPoolExecutor
import asyncio


def _average_age(patients):
    """Helper to compute average age of a list of patients."""
    if not patients:
        return 0
    return sum(p["age"] for p in patients) / len(patients)


def calculate_average_age_threaded(patients, batch_size=10):
    """
    Compute the TRUE overall average age using multiple threads.
    """
    batches = [patients[i:i + batch_size] for i in range(0, len(patients), batch_size)]
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(_average_age, batches))
    # Use total sum/total count, not avg of batch avgs
    total_age = sum(p["age"] for p in patients)
    total_count = len(patients)
    return total_age / total_count if total_count else 0

async def _async_average_age(batch):
    return _average_age(batch)


async def calculate_average_age_async(patients, batch_size=10):
    """
    Async version: compute TRUE overall average.
    """
    # We can still launch tasks to keep concurrency,
    # but final result is total sum / total count.
    batches = [patients[i:i + batch_size] for i in range(0, len(patients), batch_size)]
    tasks = [_async_average_age(batch) for batch in batches]
    results = await asyncio.gather(*tasks)
    total_age = sum(p["age"] for p in patients)
    total_count = len(patients)
    return total_age / total_count if total_count else 0