import aiohttp
import asyncio
from aiohttp import web

routes= web.RouteTableDef()

@routes.get("/getFact")
async def get_fact(request):  
        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(20):
                tasks.append(asyncio.create_task(session.get('https://catfact.ninja/fact')))
                res= await asyncio.gather(*tasks)
                res= [await x.json() for x in res]
                tasks = []
                asyncio with aiohttp.ClientSession
            return web.json_response({'status':'OK'}, status=200)
 



app = web.Application()
app.router.add_routes(routes)
web.run_app(app, port=8080)    