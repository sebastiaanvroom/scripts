import requests
import string
import os

url = 'https://freenanofaucet.com/faucet'
wallet = 'nano_17wai6q4gxm58uco1jmtytrt786ryigs7q11n5rqeohz7bj4zznaqyp9hmje'

captchaToken = '03AGdBq26yIpScgYVXIXN0TFda5FB04goQYQ94FzYHvHDq_YErvImYkTi64K2tWS-yhhnJp2i0GKIXzhPfKZXS8bLD0YM2QPoxtqH5poDlTa4bBiHcKRQ4Pmod9PFE4dHi5_FPMmwXuRNS173lLhAGmLs4cDYhmv18xLLsZ1Jvrb5Bvpas-xCcKbAL0ZnjIs7bgrgP-6ulVRR9fFs__PVH3lTqEhwVazTy_ExttFSbg0TjMMzdynwnVP0lcNEdCkhNwMM5XY7Yt-sAbRjnRox4iGKsLDdJBIQ8uCgfzOmSw-PA2tvwnb1ZmqV-zTw-MeQ6JM0288-wTonhB57mlvkAZbkw0FBEtKhAbStVSSZ_EaKOKy33eCEkEiwZvTKQHjxHJUR_9UlHoH7MsdbzN_zLQ7l_HtgqYkQ3lo7Y2oD9Thf3rMU7KTM-x0_RCFpH_20vOM_Fp5fObBwa'

req=requests.get(url, allow_redirects=False, data={
    'address': wallet,
    'captchaToken': captchaToken
    })
print(req)
