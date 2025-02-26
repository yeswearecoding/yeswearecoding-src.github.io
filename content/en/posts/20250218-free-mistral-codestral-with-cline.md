---
title: "Using Mistral Codestral for Free"
slug: "free-mistral-codestral"
date: 2025-02-18T18:54:43+01:00
draft: false
tags: ["ai", "LLM"]
categories: ["ai"]
---

Hello! 👋

I found a way to use Codestral, Mistral AI's code-focused model, for free. Let me show you how to set it up with Cline, an AI-powered code generation tool.

## What is Codestral? 🤔

Codestral is Mistral AI's first model specifically designed for code generation. It supports over 80 programming languages, ranging from popular ones like Python, Java, and JavaScript to more niche ones like Swift or Fortran.

In practice, it enables you to:
- Complete code functions
- Generate tests
- Fill in partial code using a "fill-in-the-middle" mechanism

## The tool that will help us: Cline 🛠️

To use Codestral easily, we’ll rely on Cline, a VSCode extension that simplifies the process. It’s a comprehensive coding assistant that can (according to the [project's GitHub documentation](https://github.com/cline/cline)):

- Intelligently analyze your projects by understanding file structures
- Create and edit files (with your permission, of course)
- Execute commands in the terminal
- Even debug visual issues for web development!

Cline always asks for your permission before making changes unless you allow it to act freely (which I don’t recommend). Personally, I’ve granted it access to read all local files while manually approving code modifications and shell commands (*Auto-approve: Read files and directories*).

By the way, if you encounter shell integration issues like I did (yes, Cline doesn’t get along well with verbose shells full of emojis like Zsh + Oh-my-zsh ^^), here’s the link to the doc to fix it: [shell-integration-problems](https://github.com/saoudrizwan/shell-integration-problems). I now use a plain Bash shell without any frills.

## Step-by-step setup ⚙️

Although Cline offers direct usage of a Mistral API key, it doesn’t currently work with the Codestral key (hopefully this will be fixed someday). The method relies on [liteLLM](https://github.com/BerriAI/litellm), which acts as a proxy.

I’ll show you how to set it up for Codestral, but this proxy-based method can be used with any provider supported by **LiteLLM**, making it useful in many scenarios :).

### 1. Get a Mistral API key

The first essential step is obtaining a Mistral API key:

1. Create an account on the [Mistral platform](https://console.mistral.ai/codestral);
2. Accept the terms of use;
3. Retrieve your API key from the settings (Codestral Menu -> Codestral).

Note that the code you send may be used by Mistral’s team (so don’t send anything sensitive or secret!).

### 2. Install litellm

Start by installing [liteLLM](https://github.com/BerriAI/litellm), which will serve as our bridge to Codestral:

```bash
pip install 'litellm[proxy]'
```

### 3. Configure and launch litellm

Once installed:

```bash
# Exportez votre clé API
export CODESTRAL_API_KEY=[votre_clé_API]

# Lancez le serveur
litellm --model codestral/codestral-latest
```

### 4. Install and configure Cline in VSCode

#### Installation

Since it’s an extension, simply search for it in the marketplace.

#### Configuration

Open the Cline extension added to your sidebar and:

1. Access its settings (the classic gear icon);
2. For the values:
   - Provider: "OpenAPI Compatible"
   - Base URL: `http://0.0.0.0:4000`
   - API Key: enter at least one character (it’s mandatory but not used)
   - Model ID: `codestral-latest`

Since I’m not fluent in English, I set *Custom Instructions* to `Speak in French` so I can interact in French.

Click **Done** to save your settings.

## And there you go! 🎉

You now have an AI-powered development environment for free.

I’m still exploring Cline and using it in *Act* mode (selectable at the bottom right), with permission to read files while manually approving its suggestions.

I’ve been using these tools for a few days now, and I must say I’m quite impressed—it’s a real productivity booster. The fact that it's free and integrates seamlessly with VSCode makes it a very compelling solution for developers; AI is making incredible strides in this field 😱!

Happy coding sessions! 🚀
