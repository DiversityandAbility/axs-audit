# AXS Audit

AXS Audit is an open source tool that helps people run WCAG 2.2 web accessibility audits.

We have two aims for this project:

1. Build a tool that guides a person through an audit. It should automate as much as possible, but it should be able to defer decisions to the auditor when needed. This should make a tool that can deeply adhere to the WCAG spec. It's not just "this img has alt text", it's producing a full understanding of the context of the image and whether or not the alt text does what it needs to.

2. Have a code base and documentation that makes WCAG easy to learn. We want a tool that can produce non-technical descriptions of failures and warnings. That can link to the relevant WCAG spec, but can also provide enough information and examples to make the report understandable for everyone.

It's very early days for this tool. We'd really love some help in building it. If you're interested, get in touch with us at https://diversityandability.com/contact.


## Running Locally

You'll need to clone (or otherwise download) this source code to your local machine.

You'll then need to make sure you've installed the following dependendcies:

- A terminal emulator capable of running `sh` (i.e. most unix systems, not Windows)
- python3.10

Then open a terminal, `cd` into the axs-audit folder, and run the following set up commands:

```
$ ./scripts/bootstrap.sh
```

You should only have to do this when you first set up a clean installation. Or if the requirements radically change and you reset your virtual environment.

From this point on you can run an audit by activating the venv and running `python run.py PATH_TO_CONFIG_FILE`. This is made slightly easier by the helper script `run.sh` which means you can run `./scripts/run.sh PATH_TO_CONFIG_FILE` without having to remember about the venv.

There are example configs in `audit/examples` that show you how to describe how an audit should be run. You can also just use those examples when you're testing things locally.