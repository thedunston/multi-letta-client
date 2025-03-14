# multi-letta-client

**Status: Actively supported.**

Pair programmed with AI to help with CSS and JS bugs. 

## Intro

Displays multiple letta agents, refreshes the messages sent between agents, and allows sending messages.

**Motivation**: While learning to create multipl-agent workflows with Letta, I wanted to see each agent on one screen.

## Setup

You'll need a proxy to handle the requests. This program is designed to work with [letta-py-proxy](https://github.com/thedunston/letta-py-proxy)

```
git clone https://github.com/thedunston/multi-letta-client
cd multi-letta-client
python multi_agent_server.py
```
Run the multi-agent chat server.
```
python multi_agent_server.py -h
usage: multi_agent_server.py [-h] [--host HOST] [--port PORT]
options:
  -h, --help   show this help message and exit
  --host HOST  Host address to bind to (default: 0.0.0.0)
  --port PORT  Port to run the server on (default: 5051)
```

## Connecting

The default port is 5051 and listens on all interfaces unless provided above.

Open your browser and connect to the host and port where you started the `multi_agent_server.py` script and enter the proxy (http://IP_OF_PROXY) and click "Connect."

Select the agents from the list. You can hide them or click the `x` to remove them.

Hiding the agent keeps the page querying for new agents.  Clicking `x` removes them and they won't query anymore.
