# DFW Premium Website Builder Section State Machine v1.0.0

## 1. Controlled Action

This file locks the section approval state machine for the DFW AI-Governed Premium Website Builder Module.

This state machine governs every homepage section before any page composition, final content insertion, PDF capture, DreamHost deployment, QR activation, or production approval.

## 2. Status

Status: CREATED FOR MAIN BRANCH GOVERNED MODULE BUILD

No section may skip states. No acting session may self-approve a state that requires user approval.

## 3. Scope

The state machine applies to these required homepage sections:

1. Header.
2. Navigation.
3. Hero.
4. Section 1.
5. Section 2.
6. Section 3.
7. Section 4.
8. Footer.

## 4. Locked States

Every section must pass through these states in order:

1. Not Started.
2. Research Complete.
3. Defined.
4. Options Presented.
5. Option Selected.
6. Skeleton Rendered.
7. CSS Reviewed.
8. Mobile Reviewed.
9. Under User Review.
10. Revision Required.
11. Approved.
12. Locked.
13. Content Authorized.
14. Content Inserted.
15. Final Section Approved.
16. Page Composition Authorized.

## 5. State Definitions

| State | Definition | Entry requirement | Exit requirement | Approval authority |
|---|---|---|---|---|
| Not Started | Section has no active execution record. | Section is listed in required section model. | Acting session confirms section exists in scope. | System governance. |
| Research Complete | Market, standards, and internal builder requirements are available. | Research map exists on `main`. | Research is referenced in section option review. | Acting session may confirm source presence. |
| Defined | Section name, purpose, and skeleton tagline are locked. | Required section model exists. | Section identity is restated exactly. | Acting session may confirm. |
| Options Presented | At least five options are presented for the section type. | Option library exists on `main`. | Options are shown with recommended option. | Acting session may present. |
| Option Selected | One option is selected as execution basis. | Options presented. | User approves or directs selected option. | User only. |
| Skeleton Rendered | Browser-rendered CSS skeleton exists with section name and tagline only. | Option selected. | HTML/CSS committed to approved skeleton path. | Acting session may render after user option selection. |
| CSS Reviewed | CSS tokens, section CSS, spacing, contrast, and boundaries reviewed. | Skeleton rendered. | Review identifies pass or revision requirement. | Acting session may review, user approval still required for lock. |
| Mobile Reviewed | Mobile layout reviewed after desktop and CSS review. | CSS reviewed. | Mobile review identifies pass or revision requirement. | Acting session may review, user approval still required for lock. |
| Under User Review | Section is ready for user judgment. | CSS and mobile review complete. | User approves, rejects, or requests revision. | User only. |
| Revision Required | User or audit identifies a needed change. | Issue found in any prior state. | Section returns to earliest affected state. | User or audit trigger. |
| Approved | User approves the section skeleton and behavior. | Under User Review. | Approval recorded. | User only. |
| Locked | Section skeleton is frozen for page composition stage. | Approved. | Lock recorded. | User only. |
| Content Authorized | User authorizes final content work for the locked section. | Locked. | Content scope confirmed. | User only. |
| Content Inserted | Final approved content is inserted into section. | Content Authorized. | Content passes claim, accessibility, mobile, and sponsor review. | Acting session may insert after authorization. |
| Final Section Approved | User approves final content-bearing section. | Content Inserted and reviewed. | Final approval recorded. | User only. |
| Page Composition Authorized | Section is eligible to be composed into full page. | Final Section Approved. | All sections reach this state. | User only. |

## 6. Transition Rules

1. State order is mandatory.
2. No section may skip states.
3. No section may lock without user approval.
4. No content may be inserted before `Content Authorized`.
5. No full page may be composed until every section reaches `Page Composition Authorized`.
6. A failed review returns the section to the earliest affected state.
7. A mobile failure returns the section to `Skeleton Rendered` or `CSS Reviewed`, depending on root cause.
8. A claim failure returns the section to `Content Authorized` or `Content Inserted`, depending on whether the issue is scope or copy.
9. A sponsor failure returns the section to `Options Presented`, `Skeleton Rendered`, or `Content Inserted`, depending on whether the issue is layout, surface, or copy.
10. Any attempt to create final homepage content before state authorization fails the workflow.

## 7. Required State Evidence

| State | Required evidence |
|---|---|
| Not Started | Section listed in required section model. |
| Research Complete | Research map file path and commit verified. |
| Defined | Section name and tagline restated exactly. |
| Options Presented | Five options visible for that section type. |
| Option Selected | User-selected option recorded. |
| Skeleton Rendered | HTML/CSS skeleton path committed and fetched from `main`. |
| CSS Reviewed | Desktop CSS notes recorded. |
| Mobile Reviewed | Mobile notes recorded. |
| Under User Review | Preview link or file path presented. |
| Revision Required | Revision note and affected state recorded. |
| Approved | User approval recorded in chat. |
| Locked | Lock standing recorded in chat and, when appropriate, file notes. |
| Content Authorized | User content authorization recorded. |
| Content Inserted | Content diff committed and verified. |
| Final Section Approved | User final approval recorded. |
| Page Composition Authorized | All sections reach final approval and user authorizes composition. |

## 8. Section State Tracking Table

| Section | Current starting state after module creation | Next permitted state |
|---|---|---|
| Header | Research Complete | Defined |
| Navigation | Research Complete | Defined |
| Hero | Research Complete | Defined |
| Section 1 | Research Complete | Defined |
| Section 2 | Research Complete | Defined |
| Section 3 | Research Complete | Defined |
| Section 4 | Research Complete | Defined |
| Footer | Research Complete | Defined |

## 9. User Approval Gates

User approval is mandatory for these states:

1. Option Selected.
2. Approved.
3. Locked.
4. Content Authorized.
5. Final Section Approved.
6. Page Composition Authorized.

The acting session may recommend, render after authorization, review, and report. It may not approve or lock on the user's behalf.

## 10. Failure Triggers

The state machine fails if any execution allows:

1. A section to skip a state.
2. A full homepage build before all sections are composition-authorized.
3. Final content before content authorization.
4. Skeleton content beyond section name and tagline.
5. Browser review replaced by a PDF, image, document, or board.
6. Mobile review omitted.
7. Accessibility review omitted.
8. Sponsor review omitted where sponsor surface exists.
9. Claim review omitted where content exists.
10. Acting-session self-approval.
11. DreamHost deployment before validation and user approval.
12. QR activation before production approval.

## 11. Final Determination

The section state machine is locked for all DFW homepage section execution.

Final standing for this file:

`SECTION APPROVAL STATE MACHINE CREATED / NO SECTION MAY SKIP STATES / USER APPROVAL REQUIRED FOR SELECTION, APPROVAL, LOCK, CONTENT AUTHORIZATION, FINAL SECTION APPROVAL, AND PAGE COMPOSITION AUTHORIZATION`.
