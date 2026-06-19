# DFW Matchday Concierge — Handoff Rules Authority

## Status

This file defines required handoffs between execution platforms.

It is a governing source-authority file.

## Handoff Principle

No phase is complete until its required handoff artifact is produced and reviewed.

Each platform must provide the correct output before the next platform acts.

## Handoff 1 — Owner to ChatGPT Mission Control

Owner provides field observations, approved business model, approved vehicle details, approved driver details, approved service lanes, known conversion gaps, approved design standard, business constraints, current priorities, platform limitations, and final decision authority.

ChatGPT Mission Control outputs the source-authority file package, platform responsibility matrix, handoff rules, Claude placement prompt, Claude implementation prompts, QA checklist, and correction process.

Completion requirement: Owner reviews and locks source-authority package before Claude receives it.

## Handoff 2 — ChatGPT Mission Control to Claude for Source File Placement

Claude receives owner-approved source-authority files, exact placement instructions, explicit instruction to place files verbatim, explicit instruction not to rewrite/summarize/expand/modify, explicit instruction not to edit public site pages, and explicit instruction not to implement site changes.

Claude output must include files created, directory used, confirmation contents were placed verbatim, any file path conflicts, confirmation no public site pages were changed, and recommended next phase.

Completion requirement: Owner/ChatGPT reviews file placement report before implementation begins.

## Handoff 3 — ChatGPT Mission Control to Claude for Site Implementation

Claude receives relevant locked source files for the phase, one implementation prompt, clear boundaries, explicit non-authorizations, and expected output format.

Claude output must include files changed, summary of changes, CTA/path changes if applicable, in-app review notes, risks, unresolved issues, and recommended next phase.

Completion requirement: Owner/ChatGPT reviews Claude report before next phase.

## Handoff 4 — Claude to GitHub / Repository Review

Input includes changed files, source files, implementation notes, and Claude risks/unresolved issues.

Repository review output includes diff summary, branch name, commit hash if committed, pull request link if used, changed files list, rollback note, and open issues.

Completion requirement: No deployment should occur until the diff is reviewed or explicitly approved by the owner.

## Handoff 5 — GitHub / Repository Review to Hosting

Input includes approved branch or commit, build instructions, deployment target, and owner approval status.

Hosting output includes preview URL, build log result, deployment status, errors if any, Reserve page URL, and mobile load test result.

Completion requirement: Preview must be reviewed before production unless owner explicitly approves direct production deployment.

## Handoff 6 — Hosting to QR / Field Materials

Input includes stable Reserve a Ride URL, production or approved preview URL, campaign source URLs if used, and mobile test result.

QR/field materials output includes QR target URL, QR image file, print file if applicable, scan test result, mobile reservation page result, and test submission result if included.

Completion requirement: QR must scan directly to Reserve a Ride page and must not route to the homepage or fan hub unless owner changes the rule.

## Handoff 7 — Site to Booking Intake System

Input includes reservation form, submission destination, notification settings, required fields, confirmation message, and failure state behavior.

Booking intake output includes test submission, owner notification confirmation, guest confirmation behavior, required field validation, source capture status, and failure state test.

Completion requirement: Booking intake is not ready for field use until owner notification and guest confirmation are verified.

## Handoff 8 — Booking Intake to Owner Field Operations

Input includes submitted ride request, guest contact, pickup details, drop-off details, return need, passenger count, luggage count, ride type, add-ons, airport return need, alternate driver permission, and source/campaign if available.

Owner field operations output includes accepted booking, rejected/unavailable response, alternate driver attempt if approved, waitlist status, follow-up needed, and missed conversion note.

Completion requirement: Every request must produce a clear operational status.

## Handoff 9 — Field Operations to ChatGPT Mission Control

Owner provides what converted, what failed, where users were confused, which QR sources worked, which routes performed, which gaps remain, new field observations, and urgent corrections.

ChatGPT Mission Control outputs correction package, updated source-authority recommendations if needed, next Claude prompt, booking-flow improvement, and new field rules if approved.

Completion requirement: Field intelligence must be converted into controlled updates, not ad hoc redesign.

## Handoff 10 — Sponsor Approval Handoff

Owner provides sponsor approval, category, assets, placement date, target page, ad copy or URL, and approval status.

Sponsor system outputs sponsor placement preview, inventory table update, approval confirmation, and removal date if applicable.

Completion requirement: Sponsor content must not go live without owner approval.

## Handoff 11 — Payment Approval Handoff

Owner provides payment method approval, deposit policy, refund/cancellation policy, quote/payment workflow, and payment link rules.

Payment system outputs payment link or collection method, confirmation behavior, owner notification, and guest receipt if applicable.

Completion requirement: Do not add payment/deposit features before owner approval.

## Non-Authorization Rules

Unless explicitly approved, do not publish to production, change DNS, change domain routing, add payment collection, add sponsor content, add official marks, add public partnership claims, add public rideshare accusations, add unverified pickup instructions, add unverified event data, redesign the site, or use rejected vehicle images.

## Phase Completion Rule

Each phase must end with what changed, what did not change, what files were touched, what risks remain, what handoff is next, and whether owner approval is required before proceeding.
