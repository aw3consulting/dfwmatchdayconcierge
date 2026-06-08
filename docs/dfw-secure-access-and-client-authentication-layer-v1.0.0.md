# DFW Secure Access and Client Authentication Layer v1.0.0

## 1. Purpose

This file governs secure access and client authentication for DFW Matchday Concierge. It defines the minimum access controls required before any AI-assisted intake platform, Personal Matchday Command Hub Preview, Activated Personal Matchday Command Hub, personal itinerary, guest details, budget details, payment workflow, or operator communication layer is exposed.

This layer protects privacy-sensitive VIP, Team Family, Media / Corporate, and Team Fan inquiry data while preserving a fast inquiry-first funnel.

## 2. Core Determination

The public website may collect a basic inquiry, but the AI-assisted intake platform and personal command hub require a security gate before private or sensitive details are stored, displayed, edited, or shared.

Secure access is required for:

- AI-assisted intake continuation
- Personal Matchday Command Hub Preview access
- Activated Personal Matchday Command Hub access
- personal details entry
- guest details entry
- itinerary editing
- payment detail handling
- budget details
- privacy-sensitive status disclosure
- VIP or Team Family context
- operator communication history

## 3. Access States

The platform must support four access states.

### 3.1 Public Visitor

A public visitor may view:

- homepage
- public service lanes
- public team hubs
- public Media / Corporate page
- public VIP inquiry information
- public contact information
- basic inquiry entry point

A public visitor must not view:

- private hub
- client-specific itinerary
- guest details
- payment status
- operator notes
- sensitive status
- verification details

### 3.2 Verified Inquiry Visitor

A verified inquiry visitor has completed email or mobile verification.

They may access:

- AI-assisted intake continuation
- limited command hub preview
- secure inquiry continuation link
- partial itinerary preview
- saved inquiry state

They may not access:

- full activated hub
- payment workflows requiring processor integration
- confirmed operator assignment
- confirmed vehicle assignment

### 3.3 Activated Hub Client

An activated hub client has completed the required activation step, which may include operator approval, access fee/planning deposit, or manual activation.

They may access:

- personal command hub
- detailed itinerary builder
- guest detail entry
- payment status page
- concierge request list
- operator-confirmed next steps
- status workflow

### 3.4 Operator / Admin

Operator/admin access is restricted to authorized internal users.

Operator/admin may access:

- full inquiry record
- scoring inputs
- privacy flags
- payment state
- itinerary records
- assignment records
- driver/vehicle allocation notes
- internal client notes

## 4. Authentication Methods

Launch-safe authentication methods may include:

- email verification code
- mobile verification code
- secure magic link
- one-time passcode
- manually issued private access link
- future authenticated client portal

Recommended first-stage implementation:

1. collect email and mobile number
2. issue verification code or secure link
3. allow AI-assisted intake continuation only after verification
4. create inquiry ID
5. generate command hub preview behind secure link

## 5. Verification Requirements

A secure access event should record:

- inquiry ID
- email
- phone if provided
- verification method
- verification timestamp
- IP / device metadata if legally and technically appropriate
- access state
- expiration timestamp

No sensitive details should be displayed through an unverified public URL.

## 6. Session and Link Expiration

Secure access links and sessions must expire.

Recommended launch rules:

- verification code expires within a short window
- command hub preview link expires or requires re-verification
- activated hub requires stronger access control
- inactive sessions expire automatically
- re-authentication required for payment or sensitive edits

Exact time windows may be determined during technical implementation.

## 7. Sensitive Data Handling

Sensitive data includes:

- VIP status
- Team Family status
- celebrity-adjacent status
- credential/access status
- hotel / housing location
- arrival/departure details
- guest names
- payment details
- budget
- private security interest
- operator notes
- driver/vehicle assignment details

Sensitive data must remain behind verified access and operator-controlled workflows.

## 8. Non-Disclosure Option

VIP and Team Family users must have a non-disclosure option.

Allowed public intake option:

`I prefer not to disclose sensitive status until verified or contacted directly.`

System handling:

- mark inquiry as privacy-sensitive
- avoid forcing credential, family, or celebrity context in public form
- allow representative/assistant contact
- route to operator review

## 9. AI Intake Security Boundary

AI may guide intake only inside the permitted access state.

Public AI intake may ask non-sensitive starter questions.

Sensitive AI intake must require verified access before asking for:

- exact hotel/housing location
- full itinerary obligations
- guest names
- VIP status details
- Team Family relationship details
- private security requirements
- payment information
- budget details if treated as sensitive

## 10. Personal Command Hub Security Boundary

A Personal Matchday Command Hub must not be publicly indexed, publicly discoverable, or accessible through guessable URLs.

Required controls:

- unique inquiry ID or hub ID
- secure access token or authenticated session
- expiration or re-verification
- no public directory listing
- no search indexing
- no client data in static public files

## 11. Payment Security Boundary

DFW Matchday Concierge must not collect raw payment card details directly unless a compliant payment provider and appropriate security controls are implemented.

Allowed launch approach:

- payment link after operator quote
- third-party checkout/payment request
- invoice/payment processor page
- confirmation recorded after payment provider confirmation

Prohibited:

- storing card numbers in site forms
- emailing card numbers
- collecting CVV in custom form
- claiming payment confirmation before processor confirmation

## 12. Access Fee / Planning Deposit Security

If a command hub access fee or planning deposit is implemented, it must use a secure payment process.

Rules:

- fee/payment page must be provider-handled or securely implemented
- hub activation should occur only after payment confirmation or operator override
- refund/credit terms must be disclosed before payment
- payment does not guarantee VIP acceptance unless explicitly confirmed

## 13. Operator Override

Operator may manually activate or restrict access.

Override reasons:

- VIP referral
- Team Family privacy case
- Media / Corporate approved account
- payment handled offline
- security concern
- duplicate inquiry
- restricted request
- abusive or unsafe inquiry

## 14. Public Copy Rules

Allowed public language:

- Secure access required for your personal matchday plan.
- Verify by email or mobile to continue your AI-assisted intake.
- Your personal command hub is accessible only through a secure link or authenticated session.
- Payment details are handled through approved payment methods after quote.

Avoid:

- guaranteed account security
- bank-level security unless verified
- encrypted payment claim unless implementation verifies it
- full portal claim before portal exists
- instant account creation if not implemented

## 15. Technical Implementation Direction

Static site phase may use:

- public inquiry form only
- no client-sensitive hub display
- operator-managed follow-up
- external form/auth provider if selected

Dynamic phase may use:

- DreamHost PHP endpoint
- secure tokenized links
- email verification
- SMS verification provider
- database-backed inquiry state
- authenticated client hub
- payment provider integration

Future advanced phase may use:

- full client portal
- role-based access control
- encrypted data storage
- audit logs
- AI-assisted secure intake session

## 16. Required Future Data / Config Files

Future data/config files should include:

- `data/auth-states.json`
- `data/secure-access-rules.json`
- `data/sensitive-fields.json`
- `data/hub-access-rules.json`
- `data/payment-security-rules.json`

## 17. Validation Requirements

Before any secure hub launch:

- confirm authentication method
- confirm where data is stored
- confirm payment provider
- confirm privacy-sensitive fields
- confirm access expiration rules
- confirm no client data is exposed in public static files
- confirm no search indexing of private hub URLs
- confirm operator/admin access process

## 18. Final Determination

Secure access is mandatory before any AI-assisted intake continuation, Personal Matchday Command Hub Preview, activated hub, guest details, payment state, budget details, sensitive status, itinerary obligations, or operator communication layer is exposed.

The platform may launch public marketing and basic inquiry collection first, but the AI-assisted personal command hub must remain blocked until secure access controls are selected and implemented.
