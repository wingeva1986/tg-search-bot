import yaml
import os
myyml = {'tg_bot_token': os.getenv('TG_BOT_TOKEN'),'tg_chat_id': os.getenv('TG_CHAT_ID'),'use_proxy':0,'use_proxy_dmm':0,'proxy_addr':'','tg_api_id':'','tg_api_hash':'','use_pikpak':0,'use_cache':'1','redis_host':os.getenv('REDIS_HOST'),'redis_port':35606,'enable_nsfw':'1','javbus_auth':'','use_jvav_cache':'0'}
with open("/root/.tg_search_bot/config.yaml", 'w') as f:
    f.write(yaml.dump(myyml))


