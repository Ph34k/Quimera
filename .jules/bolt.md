## 2024-05-27 - Unbounded in-memory dictionaries
**Learning:** Using an unbounded python dictionary for tracking history (`_LEARNING_DB`) can result in memory leaks and unbounded memory scaling (Memory sizes scaling with usage instances, resulting in >3.8MB with just 100000 insertions).
**Action:** Replace unbounded dictionaries with LRU caches utilizing collections.OrderedDict with `.popitem(last=False)` eviction, ensuring an upper bounds memory capacity.
