# Contributing to Mautic developer documentation

Contributions are always welcome, no matter how large or small, or at whatever skill level you are. Before contributing, please read the [Code of Conduct](https://mautic.org/code-of-conduct/) and follow the directions in this guide.

---

## Table of contents

- [Communication expectation](#communication-expectation)
- [Issues](#issues)
- [Pull requests](#pull-requests)
   - [Before submitting a PR](#before-submitting-a-pr)
   - [Submitting a PR](#submitting-a-pr)
   - [After submitting a PR](#after-submitting-a-pr)
- [Contributing workflow](#contributing-workflow)
   - [Forking the repository](#forking-the-repository)
   - [Clone the repository](#clone-the-repository)
   - [Create a new branch](#create-a-new-branch)
      - [Ensure the correct base branch](#ensure-the-correct-base-branch)
      - [Ways to create a new branch](#ways-to-create-a-new-branch)
   - [Push changes to the remote repository](#push-changes-to-the-remote-repository)
   - [Create a PR](#create-a-pr)
      - [Git cherry-pick](#git-cherry-pick)
- [Getting started](#getting-started)
   - [1. On GitHub](#1-on-github)
   - [2. Local development](#2-local-development)
      - [Prerequisite](#prerequisite)
      - [Setting up local environment](#setting-up-local-environment)
   - [3. GitHub Codespaces](#3-github-codespaces)
      - [Setting up a codespace](#setting-up-a-codespace)
      - [Live preview on codespace](#live-preview-on-codespace)
- [Working with links](#working-with-links)
   - [Create a new link](#create-a-new-link)
   - [Check broken links](#check-broken-links)
- [Working with Vale](#working-with-vale)
- [Adding a code sample](#adding-a-code-sample)
- [Updating contents and UI images](#updating-contents-and-ui-images)
- [Credit](#credit)

---

## Communication expectation

1. Always leave a detailed description in the pull request. Leave nothing ambiguous for the reviewers.
2. Provide screenshots for visual changes.
3. Always review your code first. Be sure to run the project locally and test it thoroughly before requesting a review.
4. Communicate in the GitHub repository first before Slack. Whether it's in the issue or the PR, keeping the lines of communication open and visible to everyone on the team helps everyone around you.

## Issues

- When you contribute to the project for the first time, please consider checking the [good first issue](https://github.com/mautic/developer-documentation-new/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) or [help wanted](https://github.com/mautic/developer-documentation-new/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22help%20wanted%22) labels.

- If you want to work on an open issue, please comment on it so a maintainer can assign it to you.

  If an issue isn't assigned, it's assumed to be available for anyone to work on. So, ensure that you're assigned to an issue **before** beginning work to avoid conflicts.

- Don’t ask maintainers to assign you to another issue before you finish working on your current one and create a PR. Also, avoid requesting assignment to an issue that already has someone assigned. However, if the assignee hasn’t addressed the issue for a while and you’re interested in working on it, leave a comment to ask about its status and progress.

- Did you spot a typo, missing instructions, or have an idea for enhancing the Mautic developer documentation? You can [create an issue](https://github.com/mautic/developer-documentation-new/issues/new/choose) to address it.

  However, the Education Team needs to triage the issue before you can work on it. If you wish to work on the issue you submitted, please inform and tag the `@mautic/education-team-leaders` in the comment.

## Pull requests

Pull requests - PRs - are always welcome. However, before working on changes, you must ensure that a maintainer **assigns you** to an existing issue, and always **link your work to the issue in your PR**.

### Submitting a PR

<!-- vale on -->

1. Ensure that you address one issue in one PR. If you work on multiple issues, work on them separately and create one PR to address each issue.

<!-- vale off -->

### After submitting a PR

<!-- vale on -->

<!-- vale off -->

2. Please don't DM maintainers on Slack to review or ask feedback and questions about your PR.

   If you'd like feedback or ask questions about your PR, tag `@mautic/education-team-leaders` in the comment of your PR or use the `#t-education` channel on Slack. That way, not only maintainers, but the community can help you get unstuck. The team always receives a notification on new PR creation. If you haven't received a review within a week, you can tag them in the PR comments to ask for an estimated review time.

<!-- vale on -->

## Credit

Mautic adapted these contributing guidelines from [OpenSource-Communities/intro](https://github.com/OpenSource-Communities/intro/blob/main/contributing/CONTRIBUTING.md) repository.

---

Thank you for contributing to improving the Mautic developer documentation.