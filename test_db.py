from modules.tool_db import search_tools, suggest_tools

print("--- search_tools(nmap) ---")
results = search_tools("nmap")
print(f"Found {len(results)} results")
for c, t in results[:10]:
    print(f"  [{c}] {t['name']}: {t['description'][:80]}")

print()
print("--- suggest_tools(scan ports on a remote host) ---")
results = suggest_tools("scan ports on a remote host")
print(f"Found {len(results)} results")
cats = set(c for c, t in results)
print(f"Categories: {cats}")
for c, t in list(results)[:10]:
    print(f"  [{c}] {t['name']}: {t['description'][:80]}")

print()
print("--- suggest_tools(crack password hash) ---")
results = suggest_tools("crack password hash")
print(f"Found {len(results)} results")
for c, t in list(results)[:10]:
    print(f"  [{c}] {t['name']}: {t['description'][:80]}")

print()
print("--- get_all_categories() ---")
from modules.tool_db import get_all_categories
cats = get_all_categories()
print(f"{len(cats)} categories")
for c in cats[:10]:
    print(f"  {c}")
