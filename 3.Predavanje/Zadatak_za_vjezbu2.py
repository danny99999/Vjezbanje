import asyncio
import numpy as np

async def fun1(x):
    assert isinstance(x, list)
    return [{"korisnik":e, "id":i} for i,e in enumerate(x)]

async def fun2():
    for x in range(10):
        await asyncio.sleep(0.01)
        print(x)
    pass

async def fun3(x):
    assert isinstance(x, list) and all([isinstance(d, dict)] for d in x)
    assert ([(d["korisnik"] and d["id"]) for d in x])
    await asyncio.sleep(0.05)
    return [(d.get("korisnik"), d.get("id"), len(d.get("korisnik"))) for d in x]
    
async def main():
    imena=["Ivan", "Pero", "Ana"]
    mid_res= await fun1(imena)
    asyncio.create_task(fun2())
    final= await fun3(mid_res)
    print(final)


if __name__== "__main__":
    asyncio.run(main())