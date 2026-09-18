# ai-videos

AI image and video generation driven from Claude Code, using the
[Higgsfield](https://higgsfield.ai) MCP server.

## Higgsfield MCP

The Higgsfield MCP server is configured for this project in `.mcp.json`:

```json
{
  "mcpServers": {
    "higgsfield": {
      "type": "http",
      "url": "https://mcp.higgsfield.ai/mcp"
    }
  }
}
```

It is pre-approved for this project in `.claude/settings.json`, so Claude Code
loads it automatically when you open this repository. No API key is needed:
the server authenticates with your Higgsfield account over OAuth.

### Sign in (one time per machine)

1. Open Claude Code in this repository (terminal, desktop app, or a cloud
   session on claude.ai/code).
2. Run `/mcp`, select **higgsfield**, and choose **Authenticate**.
3. Sign in to your Higgsfield account in the browser window that opens.
4. Back in Claude Code, `/mcp` should now show **higgsfield** as connected.

From a plain terminal you can do the same with:

```bash
claude mcp login higgsfield
```

Tokens are stored by Claude Code and refreshed automatically (the server grants
`offline_access`), so you only sign in once per machine.

### What you get

Once connected, Claude can call Higgsfield's tools directly, for example
text-to-image and image/text-to-video across Higgsfield's model library
(Veo, Kling, Sora, Seedance, Soul, Flux, Nano Banana, and others), character
training, and post-production steps such as upscaling and reframing.

Try asking:

> Generate a 5 second cinematic drone shot of a coastal city at sunrise.

### Notes

- Generations draw from the credits on your Higgsfield account.
- On managed Anthropic plans, an admin may need to allowlist
  `mcp.higgsfield.ai`. Cloud sessions must run in an environment whose network
  policy allows that host (the default **Trusted** policy does).
- If `/mcp` does not list the server, run `claude mcp list` in this directory
  and accept the workspace trust prompt if shown.
- Higgsfield also ships a standalone CLI (`npm i -g @higgsfield/cli`) with
  companion skills (`npx skills add higgsfield-ai/skills`). That is optional
  and independent of the MCP connection above.
