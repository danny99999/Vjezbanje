import asyncio
import numpy as np

async def fun1():
    return[{"artikl":v} for v in ["Kava", "Voda"]]

async def fun2(x):
    assert isinstance(x, list) and all([isinstance(d, dict)] for d in x)
    return [{**d, **{"cijena":np.random.randint(1,10)}} for d in x]

async def main():
    artikli= await fun1()
    final= await fun2(artikli)
    print(final)

if __name__=="__main__":
    asyncio.run(main())